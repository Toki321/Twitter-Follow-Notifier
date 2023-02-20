import sys

sys.path.append("D:\\Coding Projects\\gemFinderNotifier\\follow-notifier")

print(sys.path)
from classes.TrackedTwitterAccount import TrackedTwitterAccount
from helpers.idsToTrack import readIds

idsToTrack = readIds()

accountsToTrack = []

for id in idsToTrack:
    account = TrackedTwitterAccount(id)
    accountsToTrack.append(account)

    usernameList = account.getListUsernameFollows()
    account.writeToFile(usernameList)
