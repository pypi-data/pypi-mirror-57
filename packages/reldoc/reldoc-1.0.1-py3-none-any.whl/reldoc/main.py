# -*- coding: utf-8 -*-
import git
import re
import sys


def echo_release_doc(tag):
    repo = git.Repo("./")
    lines = []
    for item in repo.iter_commits(tag + '..HEAD', min_parents=2):
        if 'Merged in feature' in item.message and 'pull request #' in item.message and 'Approved-by:' in item.message:
            message = item.message.splitlines()[2]
            result = re.search('#\d+', item.message.splitlines()[0])
            pullreq_no = result.group()[1:]
            lines.append(
                '- [{0}](https://bitbucket.org/uzabase/newspicks-server/pull-requests/{1}) @{2}'.format(message,
                                                                                                        pullreq_no,
                                                                                                        item.author))
    for line in lines:
        print(line)


def main():
    echo_release_doc(sys.argv[1])


if __name__ == '__main__':
    main()
