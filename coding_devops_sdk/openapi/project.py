# -*- coding: utf-8 -*-


class ProjectAPIMixin(object):
    def describe_project_by_name(self, project_name):
        kwargs = {'ProjectName': project_name}
        return self.request_api(action="DescribeProjectByName", **kwargs)['Project']
