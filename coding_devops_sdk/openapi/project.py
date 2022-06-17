# -*- coding: utf-8 -*-

from coding_devops_sdk.config import settings


class ProjectAPIMixin(object):
    def describe_project_by_name(self, project_name):
        kwargs = {'ProjectName': project_name}
        return self.request_api(action="DescribeProjectByName", **kwargs)['Project']


class IntegratedProjectAPIMixin(object):
    def get_project_id_by_name(self, project_name=settings.DEFAULT_PROJECT_NAME):
        if not project_name:
            raise ValueError("project name should be not empty, please set project_name either directly or on project settings")
        return self.describe_project_by_name(project_name=project_name)['Id']
