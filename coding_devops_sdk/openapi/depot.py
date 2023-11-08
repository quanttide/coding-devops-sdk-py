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
        return self.request_api(action='DescribeProjectDepotInfoList', ProjectId=project_id)['DepotData']['Depots']

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

    def modify_git_transfer(self, depot_id, target_project_id) -> str:
        """
        仓库转移至同团队下的其他项目中
        :return: 转移后Web页面的访问路径
        """
        return self.request_api(action='ModifyGitTransfer', depot_id=depot_id, target_project_id=target_project_id)["NewDepotPath"]


class IntegratedDepotAPIMixin(object):
    def describe_project_depot_info_list_by_name(self, project_name: str) -> list:
        project_id = self.get_project_id_by_name(project_name)
        return self.describe_project_depot_info_list(project_id=project_id)

    def get_depot_id_by_name(self, depot_name, project_name=settings.DEFAULT_PROJECT_NAME):
        """
        :param depot_name:
        :param project_name:
        :return:
        """
        if not project_name:
            raise ValueError("project name should be not empty, please set project_name either directly or on project settings")
        depots = self.describe_project_depot_info_list_by_name(project_name)
        # https://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value
        try:
            return next((depot for depot in depots if depot['Name'] == depot_name))['Id']
        except StopIteration:
            # TODO：临时补丁，优化实现。
            raise Exception(f"项目{project_name}不存在仓库{depot_name}")

    def modify_git_transfer_by_name(self, source_project_name, source_depot_name, target_project_name, target_depot_name=None):
        """

        :param source_project_name:
        :param source_depot_name:
        :param target_project_name:
        :param target_depot_name: 填写时改成新名字
        :return:
        """
        depot_id = self.get_depot_id_by_name(depot_name=source_depot_name, project_name=source_project_name)
        target_project_id = self.get_project_id_by_name(project_name=target_project_name)
        return self.modify_git_transfer(depot_id=depot_id, target_project_id=target_project_id)


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

    def create_git_release(self, depot_id, user_id, tag_name, commit_sha,
                           target_commitish, title, description, pre: bool) -> bool:
        """
        https://coding.net/help/openapi#fa6fe573f5adbfd00c0f1e8e742f4730

        :param depot_id: 仓库 Id
        :param pre: 是否预发布
        :return:
        """
        pass


class IntegratedReleaseAPIMixin(object):
    def describe_git_releases_by_name(self, depot_name, project_name=settings.DEFAULT_PROJECT_NAME, **kwargs):
        if not project_name:
            raise ValueError("project name should be not empty, please set project_name either directly or on project settings")
        depot_id = self.get_depot_id_by_name(depot_name=depot_name, project_name=project_name)
        return self.describe_git_releases(depot_id)
