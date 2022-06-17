"""
代码仓库API
"""

from typing import Union

from coding_devops_sdk.config import settings


# ----- 仓库API -----

class DepotAPIMixin(object):
    def describe_project_depot_info_list(self, project_id: Union[int, str]) -> list:
        """
        查询项目下仓库信息列表

        https://help.coding.net/openapi#04f0f34041e112aabd648c8381f31ca5
        :return:
        """
        return self.request_api(action='DescribeProjectDepotInfoList', project_id=project_id)['DepotData']['Depots']

    def describe_team_depots(self):
        """
        获取团队下仓库列表

        https://help.coding.net/openapi#e0528b125f6eca3d1c5c21bd690c0402

        :return:
        """
        pass

    def describe_git_files(self):
        """
        查询仓库目录下文件和文件夹名字

        https://help.coding.net/openapi#531275c981a3ae91c1aa6a889a114f5c

        :return:
        """
        pass

    def is_path_in_depot(self):
        """
        (high-level API) 仓库下是否存在文件或文件夹
        :return:
        """
        pass


class IntegratedDepotAPIMixin(object):
    def describe_project_depot_info_list_by_name(self, project_name: str) -> list:
        project_id = self.get_project_id_by_name(project_name)
        return self.describe_project_depot_info_list(project_id=project_id)

    def get_depot_id_by_name(self, depot_name, project_name=settings.DEFAULT_PROJECT_NAME):
        """

        :param project_name:
        :param depot_name:
        :return:
        """
        if not project_name:
            raise ValueError("project name should be not empty, please set project_name either directly or on project settings")
        depots = self.describe_project_depot_info_list_by_name(project_name)
        # https://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value
        return next((depot for depot in depots if depot['Name'] == depot_name))['Id']


# ----- 发布API -----

class ReleaseAPIMixin(object):
    def describe_git_releases(self, depot_id, status: int = 0, **kwargs):
        """

        :param depot_id:
        :param status: 版本状态。0:全部；1:已发布；2:预发布。
        :param kwargs:
        :return:
        """
        kwargs['DepotId'] = depot_id
        kwargs['Status'] = status
        return self.request_api(action='DescribeGitReleases', **kwargs)['ReleasePageList']['Releases']


class IntegratedReleaseAPIMixin(object):
    def describe_git_releases_by_name(self, depot_name, project_name=settings.DEFAULT_PROJECT_NAME, **kwargs):
        if not project_name:
            raise ValueError("project name should be not empty, please set project_name either directly or on project settings")
        depot_id = self.get_depot_id_by_name(project_name, depot_name)
        return self.describe_git_releases(depot_id)
