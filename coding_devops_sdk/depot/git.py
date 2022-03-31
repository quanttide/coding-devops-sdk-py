# -*- coding: utf-8 -*-

import git


class Git(git.cmd.Git):
    def __init__(self):
        super().__init__()

    def clone(self, project_name, depot_name, protocol='https'):
        pass
