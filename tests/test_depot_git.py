"""
Coding代码仓库Git操作
"""

import os
import unittest

from coding_devops_sdk.depot import Git


class GitTestCase(unittest.TestCase):
    def test_git_clone(self):
        project_name = 'demo'
        depot_name = 'demo'
        git = Git(os.path.join('./depots', depot_name))
        git.clone(project_name, depot_name)


if __name__ == '__main__':
    unittest.main()
