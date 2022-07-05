"""
APIClient
"""

import requests

from coding_devops_sdk.config import settings
from coding_devops_sdk.openapi.depot import DepotAPIMixin, IntegratedDepotAPIMixin, ReleaseAPIMixin, \
    IntegratedReleaseAPIMixin
from coding_devops_sdk.openapi.exceptions import raise_if_error
from coding_devops_sdk.openapi.project import ProjectAPIMixin, IntegratedProjectAPIMixin


class BaseAPIClient(object):
    def __init__(self, team=None, token=None):
        """
        暂时只支持个人令牌，未来会支持OAuth2
        :param token:
        """
        self.team = team or settings.TEAM
        self.token = token or settings.AUTH_TOKEN
        if not self.token:
            raise ValueError("鉴权令牌不可为空，请设置token参数或传入AUTH_TOKEN配置项。")

    def request_api(self, action, **kwargs):
        data = {'Action': action}
        data.update(kwargs)
        headers = {
            'Authorization': f"token {self.token}"
        }
        r = requests.post('https://e.coding.net/open-api', json=data, headers=headers)
        # 抛出网络请求异常
        r.raise_for_status()
        return_data = r.json()
        # 抛出Coding服务器返回异常
        raise_if_error(return_data)
        return return_data['Response']


class CodingDevOpsAPIClient(
    BaseAPIClient,
    ProjectAPIMixin, IntegratedProjectAPIMixin,
    DepotAPIMixin, IntegratedDepotAPIMixin,
    ReleaseAPIMixin, IntegratedReleaseAPIMixin,
):
    """
    Coding DevOps OpenAPI Client
    """
    pass


if settings.AUTH_TOKEN:
    coding_openapi_client = CodingDevOpsAPIClient()
