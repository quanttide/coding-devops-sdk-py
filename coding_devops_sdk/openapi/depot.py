"""
代码仓库API
"""

from typing import Union


class DepotAPIMixin(object):
    # ----- 仓库列表API -----
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
        project_id = self.describe_project_by_name(project_name=project_name)['Id']
        return self.describe_project_depot_info_list(project_id=project_id)
