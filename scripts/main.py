import sys
import multiprocessing

sys.path.append("D:\\Coding Projects\\gemFinderNotifier\\follow-notifier")

from notifyFollows import schedule

if __name__ == "__main__":
    # Create two processes, one for each script
    p1 = multiprocessing.Process(target=schedule)

    # Start the processes
    p1.start()


