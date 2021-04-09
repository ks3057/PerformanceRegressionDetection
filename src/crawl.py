from pydriller import RepositoryMining
import time
from datetime import datetime


def initialise():
    dt1 = datetime(2007, 12, 10, 00, 50, 7)
    dt2 = datetime(2014, 9, 23, 13, 7, 52)
    count = 0
    for commit in RepositoryMining(
            '/Users/kirtanasuresh/Documents/commons-pool',
            only_in_branch="master", only_no_merge=True, since=dt1,
            to=dt2).traverse_commits():
        print(commit.modifications)
        count += 1
    print(count)


def main():
    start_time = time.time()
    initialise()
    print("--- %s seconds to map the file ---" % (time.time() -
                                                  start_time))


if __name__ == '__main__':
    main()
