import sys

sys.path.append("D:\\Coding Projects\\gemFinderNotifier\\follow-notifier")

print(sys.path)
from classes.TrackedTwitterAccount import TrackedTwitterAccount
from helpers.idsToTrack import readIds

idsToTrack = readIds('4')

accountsToTrack = []

for id in idsToTrack:
    account = TrackedTwitterAccount(id, '4')
    accountsToTrack.append(account)

    usernameList = account.getListUsernameFollows()
    account.writeToFile(usernameList)
