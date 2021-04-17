from pydriller import RepositoryMining
import time
from datetime import datetime


def initialise():
    f = open("outputs/final.csv", "w")
    f.write("Commit hash, Repository name, Author name, Filename, nloc, "
            "cyclomatic complexity, "
            "Num lines added, "
            "Num lines removed, Change type, Label" + "\n")

    commons_pool()
    jackson_core()
    commons_dbcp()
    commons_fileupload()
    commons_compress()
    commons_io()
    # k_9()
    commons_csv()
    commons_text()
    commons_imaging()


def commons_pool():
    dt1 = datetime(2007, 12, 10, 00, 50, 7)
    dt2 = datetime(2014, 9, 23, 13, 7, 52)
    performance_regression_commits_from_peass = {
        '16a2ef563c9d87253a2347628f796776d0987851',
        '094266f6a51a974ffb6dc264bcb6f7c13801fd96',
        '2113166ed6a359adfcde240310960f1aee3f2607',
        '1d9e39095ccecdf3668236177bc17b4561382316',
        '6979917d99021f44432d089588477439bee37d05',
        'f7a6d7ae57ee0ed9e1da7967730def2c5ffe3e8c',
        '5392bccc645803a66541ec1e01172a22f50da7d9',
        '6df9afdb2c5125beb388b67570f73818d660aa12'}

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass,
              "commons-pool",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def jackson_core():
    dt1 = datetime(2013, 10, 3, 10, 8, 27)
    dt2 = datetime(2019, 2, 16, 00, 23, 00)
    performance_regression_commits_from_peass = {
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

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass,
              "jackson-core",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def commons_dbcp():
    dt1 = datetime(2014, 2, 5, 22, 30, 34)
    dt2 = datetime(2014, 3, 3, 13, 43, 30)
    performance_regression_commits_from_peass = {
        'a3cefc2063d220efdc8a42a66164a5ff0bfd690a',
        'a127eaf6b81f3be06282e4b67692bacc020b8703'}

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass,
              "commons-dbcp",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def commons_fileupload():
    dt1 = datetime(2013, 3, 7, 10, 58, 30)
    dt2 = datetime(2016, 8, 22, 15, 54, 00)
    performance_regression_commits_from_peass = {
        '651283e071de6230356af058afe0c0b78e8cb8b6',
        '774ef160d591b579f703c694002e080f99bcd28b',
        'afdedc9580dde03287979607f9ce441b23b6bc90'}

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass,
              "commons-fileupload",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def commons_compress():
    dt1 = datetime(2009, 9, 30, 7, 25, 00)
    dt2 = datetime(2018, 1, 10, 10, 10, 00)
    performance_regression_commits_from_peass = {
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

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass,
              "commons-compress",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def commons_io():
    dt1 = datetime(2006, 12, 29, 13, 45, 00)
    dt2 = datetime(2012, 6, 1, 17, 27, 22)
    performance_regression_commits_from_peass = {
        '6eca4c05986bac88d1b65af83348a754efa36559',
        '59ffcad15d220c2bc1f70f01d58bc31dec04b423'}

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass, "commons-io",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def k_9():
    dt1 = datetime(2017, 1, 15, 17, 48, 4)
    dt2 = datetime(2017, 1, 17, 17, 27, 22)
    performance_regression_commits_from_peass = {
        '79c65d4cff60ef6dd3e452591ae8f8dcec18630a'}

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass, "k-9",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def commons_csv():
    dt1 = datetime(2012, 3, 29, 00, 58, 30)
    dt2 = datetime(2012, 3, 31, 00, 58, 30)
    performance_regression_commits_from_peass = {
        '19ba389fe8194bb6c22102b32e021d8487e1e307'}

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass,
              "commons-csv",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def commons_text():
    dt1 = datetime(2017, 10, 12, 20, 5, 45)
    dt2 = datetime(2017, 10, 14, 20, 5, 45)
    performance_regression_commits_from_peass = {
        '61cbf0afe04d86a546e7094513328c9f7a7363ae'}

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass,
              "commons-text",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def commons_imaging():
    dt1 = datetime(2012, 5, 9, 5, 57, 7)
    dt2 = datetime(2012, 5, 11, 5, 57, 7)
    performance_regression_commits_from_peass = {
        '6d86230edf3bece2e9c06da893d0b08324348b3a'}

    number_of_non_perf_files_required = len(
        performance_regression_commits_from_peass)
    number_of_non_perf_files_current = 0

    build_csv(dt1, dt2, performance_regression_commits_from_peass,
              "commons-imaging",
              number_of_non_perf_files_required,
              number_of_non_perf_files_current)


def build_csv(dt1, dt2, performance_regression_commits_from_peass, project,
              number_of_non_perf_files_required,
              number_of_non_perf_files_current):
    commit_classify = {}
    commit_identified = set()

    for commit in RepositoryMining(
            '/Users/kirtanasuresh/Documents/{}'.format(project),
            only_in_branch="master", only_no_merge=True, since=dt1,
            to=dt2).traverse_commits():
        if commit.hash in performance_regression_commits_from_peass:
            commit_classify[commit.hash] = "PR"
            commit_identified.add(commit.hash)
        else:
            if number_of_non_perf_files_required == \
                    number_of_non_perf_files_current:
                continue
            else:
                commit_classify[commit.hash] = "NPR"

        # if the change is in the test case itself, we ignore the commit
        commit_has_changed_tests = False

        # here we check only for NPR label commits because we excluded
        # Test commits when manually evaluating PR label
        if commit_classify[commit.hash] == "NPR":
            for m in commit.modifications:
                if "Test" in m.filename or "test" in m.filename:
                    commit_has_changed_tests = commit_has_changed_tests or True

        if not commit_has_changed_tests:
            if not contains_only_non_java_files(commit):
                for m in commit.modifications:
                    # ignore non java files
                    if "java" not in m.filename:
                        continue
                    f = open("outputs/final.csv", "a")
                    list1 = [commit.hash, project, commit.author.name,
                             m.filename,
                             m.nloc, m.complexity,
                             m.added, m.removed, m.change_type.name,
                             commit_classify[commit.hash]]
                    list1 = map(str, list1)
                    x = ",".join(list1)
                    x = "\n" + x
                    f.write(x)
                if commit_classify[commit.hash] == "NPR":
                    number_of_non_perf_files_current += 1

        f = open("outputs/{}-ignored.txt".format(project), "w")
        f.write(str(performance_regression_commits_from_peass.difference(
            commit_identified)))
        f.close()


def contains_only_non_java_files(commit):
    for m in commit.modifications:
        if "java" in m.filename:
            return False
    return True


def main():
    start_time = time.time()
    initialise()
    print("--- %s seconds to map the file ---" % (time.time() -
                                                  start_time))


if __name__ == '__main__':
    main()
