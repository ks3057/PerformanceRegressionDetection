from pydriller import RepositoryMining
import time
import csv
from datetime import datetime


def initialise():
    # commons_pool()
    # jackson_core()
    # commons_dbcp()
    # commons_fileupload()
    commons_compress()

def commons_pool():
    dt1 = datetime(2007, 12, 10, 00, 50, 7)
    dt2 = datetime(2014, 9, 23, 13, 7, 52)
    count = 0
    commit_classify = {}
    commons_pool_reg = {'16a2ef563c9d87253a2347628f796776d0987851',
                        '094266f6a51a974ffb6dc264bcb6f7c13801fd96',
                        '2113166ed6a359adfcde240310960f1aee3f2607',
                        '1d9e39095ccecdf3668236177bc17b4561382316',
                        '6979917d99021f44432d089588477439bee37d05',
                        'f7a6d7ae57ee0ed9e1da7967730def2c5ffe3e8c',
                        '5392bccc645803a66541ec1e01172a22f50da7d9',
                        '6df9afdb2c5125beb388b67570f73818d660aa12'}

    for commit in RepositoryMining(
            '/Users/kirtanasuresh/Documents/commons-pool',
            only_in_branch="master", only_no_merge=True, since=dt1,
            to=dt2).traverse_commits():
        if commit.hash in commons_pool_reg:
            commit_classify[commit.hash] = "PR"
            count += 1
        else:
            commit_classify[commit.hash] = "NPR"

    with open('outputs/commons-pool.csv', 'w') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(["hashcode", "performance regression"])
        for key, values in commit_classify.items():
            w.writerow([key, values])


def jackson_core():
    dt1 = datetime(2013, 10, 3, 10, 8, 27)
    dt2 = datetime(2019, 2, 16, 00, 23, 00)
    count = 0
    commit_classify = {}
    commit_identified = set()
    jackson_core_reg = {
        '8fc4243d0f15813c9caf37635113489854cbd655',
        'ac956fe5eed337c516beb504aadf82917c26d6ba',
        'ef860da507ef31a604624a434040bde984d310e8',
        '48b57265f6344ccb3ca5b4c57bee2d8db9817a95',
        '1d97b5396e198a05a99508eaf64ece4451526a4e',
        '322accee786d188d2ae25d9a5721508784ecf471',
        'ad3a43eb9ad2f6b26c3a3c8be3c13ed090e5e0aa',
        'e22dbdb8ef603d6bf629c51f4a852a4083779a9b',
        '5e3d980f704ceca91b263ac42efa30bedcf5a76f',
        'b6c54cf06167b7ef8b45a67e8ddfa427e63c6c20',
        '8cd1e24ad7cb031b14d90db64c49ba0a68669463'}

    for commit in RepositoryMining(
            '/Users/kirtanasuresh/Documents/jackson-core',
            only_in_branch="master", only_no_merge=True, since=dt1,
            to=dt2).traverse_commits():
        if commit.hash in jackson_core_reg:
            commit_classify[commit.hash] = "PR"
            count += 1
            commit_identified.add(commit.hash)
        else:
            commit_classify[commit.hash] = "NPR"

    with open('outputs/jackson-core.csv', 'w') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(["hashcode", "performance regression"])
        for key, values in commit_classify.items():
            w.writerow([key, values])

    print(count)
    f = open("outputs/jackson-core-ignored.txt", "w")
    f.write(str(jackson_core_reg.difference(commit_identified)))
    f.close()


def commons_dbcp():
    dt1 = datetime(2014, 2, 5, 22, 30, 34)
    dt2 = datetime(2014, 3, 3, 13, 43, 30)
    count = 0
    commit_classify = {}
    commit_identified = set()
    commons_dbcp_reg = {
        'a3cefc2063d220efdc8a42a66164a5ff0bfd690a',
        'a127eaf6b81f3be06282e4b67692bacc020b8703'}

    for commit in RepositoryMining(
            '/Users/kirtanasuresh/Documents/commons-dbcp',
            only_in_branch="master", only_no_merge=True, since=dt1,
            to=dt2).traverse_commits():
        if commit.hash in commons_dbcp_reg:
            commit_classify[commit.hash] = "PR"
            count += 1
            commit_identified.add(commit.hash)
        else:
            commit_classify[commit.hash] = "NPR"

    with open('outputs/commons-dbcp.csv', 'w') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(["hashcode", "performance regression"])
        for key, values in commit_classify.items():
            w.writerow([key, values])

    print(count)
    f = open("outputs/commons-dbcp-ignored.txt", "w")
    f.write(str(commons_dbcp_reg.difference(commit_identified)))
    f.close()


def commons_fileupload():
    dt1 = datetime(2013, 3, 7, 10, 58, 30)
    dt2 = datetime(2016, 8, 22, 15, 54, 00)
    count = 0
    commit_classify = {}
    commit_identified = set()
    commons_fileupload_reg = {
        '651283e071de6230356af058afe0c0b78e8cb8b6',
        '774ef160d591b579f703c694002e080f99bcd28b',
        'afdedc9580dde03287979607f9ce441b23b6bc90'}

    for commit in RepositoryMining(
            '/Users/kirtanasuresh/Documents/commons-fileupload',
            only_in_branch="master", only_no_merge=True, since=dt1,
            to=dt2).traverse_commits():
        if commit.hash in commons_fileupload_reg:
            commit_classify[commit.hash] = "PR"
            count += 1
            commit_identified.add(commit.hash)
        else:
            commit_classify[commit.hash] = "NPR"

    with open('outputs/commons-fileupload.csv', 'w') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(["hashcode", "performance regression"])
        for key, values in commit_classify.items():
            w.writerow([key, values])

    print(count)
    f = open("outputs/commons-fileupload-ignored.txt", "w")
    f.write(str(commons_fileupload_reg.difference(commit_identified)))
    f.close()


def commons_compress():
    dt1 = datetime(2009, 9, 30, 7, 25, 00)
    dt2 = datetime(2018, 1, 10, 10, 10, 00)
    count = 0
    commit_classify = {}
    commit_identified = set()
    commons_fileupload_reg = {
        '2318ba308b4d36c493330c9286a86878bc24af55',
        '21148e7b5bc4cf6d0c38dc80bed5d7eb709897e1',
        'a2f978e97f13697e7adfddc3f96a9131803db679',
        'f9334473bd9993f38458ecee137ba9e7f7b79abb',
        '87f0f2ec35c600cae7a17621455c00e24256011a',
        'daeb07457183232eb9a9fb71bfb31a3700404427',
        '7d73baf10e435fcaa4927495afc185fb473c416b',
        '7e89c9cc80bc3fd2aab64f25dd816c6d14790988',
        'daa69a5981c7c12e0af5922f0a07653446261b07',
        '135dd48fda61f81d9b8e0aec0661c1d48226ae3c',
        'd2bcb0371967f313aa9710f12725c20a5650dc93',
        'a671a703fe86b69adb8c61495a915065c186362d',
        '840a20e10b88734211f814cec99177e3bcd06a4a',
        '1418705648202405208e3f4d900dfcc81457cbac',
        '516c38fd95fff30841f9af370f50cf1f7733c209'}

    for commit in RepositoryMining(
            '/Users/kirtanasuresh/Documents/commons-compress',
            only_in_branch="master", only_no_merge=True, since=dt1,
            to=dt2).traverse_commits():
        if commit.hash in commons_fileupload_reg:
            commit_classify[commit.hash] = "PR"
            count += 1
            commit_identified.add(commit.hash)
        else:
            commit_classify[commit.hash] = "NPR"

    with open('outputs/commons-compress.csv', 'w') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(["hashcode", "performance regression"])
        for key, values in commit_classify.items():
            w.writerow([key, values])

    print(count)
    f = open("outputs/commons-compress-ignored.txt", "w")
    f.write(str(commons_fileupload_reg.difference(commit_identified)))
    f.close()


def main():
    start_time = time.time()
    initialise()
    print("--- %s seconds to map the file ---" % (time.time() -
                                                  start_time))


if __name__ == '__main__':
    main()
