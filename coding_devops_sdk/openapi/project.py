# -*- coding: utf-8 -*-


class ProjectAPIMixin(object):
    def describe_project_by_name(self, project_name):
        kwargs = {'ProjectName': project_name}
        return self.request_api(action="DescribeProjectByName", **kwargs)['Project']


class IntegratedProjectAPIMixin(object):
    def get_project_id_by_name(self, project_name):
        return self.describe_project_by_name(project_name=project_name)['Id']
