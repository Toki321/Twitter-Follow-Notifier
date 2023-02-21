import sys

sys.path.append("D:\\Coding Projects\\gemFinderNotifier\\follow-notifier")

from apscheduler.schedulers.blocking import BlockingScheduler
from helpers.idsToTrack import createToTrackList


def doLogicForOneAccount(account):  # account
    # Read old data from txt
    oldFollows = account.extractIdsFromFile()

    # Get latest follow list
    latestFollows = account.getListUsernameFollows()

    # Write new data to txt
    account.writeToFile(latestFollows)

    # Get follows that weren't in the old list
    newFollows = account.getNewFollows(oldFollows, latestFollows)

    # Remove follows that don't meet conditions
    checkedNewFollows = account.getCheckedNewFollows(newFollows)

    # Send telegram notification to group
    account.sendTelegramMessage(checkedNewFollows)


def runForEveryAccount():
    
    # List of lists. Each list is with a diff bearer token. Twitter api moment..
    listOfListsAccounts = []
    listOfListsAccounts.append(createToTrackList('1'))
    listOfListsAccounts.append(createToTrackList('2'))
    listOfListsAccounts.append(createToTrackList('3'))

    for list in listOfListsAccounts:
        for account in list:
            doLogicForOneAccount(account)


def schedule():
   
    scheduler = BlockingScheduler()
    scheduler.add_job(runForEveryAccount, "interval", minutes=15)

    scheduler.start()

schedule()