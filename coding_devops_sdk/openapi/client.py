# -*- coding: utf-8 -*-

import requests

from coding_devops_sdk.config import settings
from coding_devops_sdk.openapi.exceptions import CodingOpenAPIException


class BaseAPIClient(object):
    def __init__(self, team=None, token=None):
        """
        暂时只支持个人令牌，未来会支持OAuth2
        :param token:
        """
        self.team = team or settings.TEAM
        self.token = token or settings.AUTH_TOKEN

    def request_api(self, action, **kwargs):
        data = {'Action': action}
        data.update(kwargs)
        headers = {
            'Authorization': f"token {self.token}"
        }
        r = requests.post('https://e.coding.net/open-api', json=data, headers=headers)
        r.raise_for_status()
        return_data = r.json()
        if 'Error' in return_data['Response']:
            raise CodingOpenAPIException(code=return_data['Response']['Error']['Code'],
                                         message=return_data['Response']['Error']['Message'],
                                         request_id=return_data['Response']['RequestId'])

        return return_data['Response']


class CodingDevOpsAPIClient(
    BaseAPIClient,
):
    """
    Coding DevOps OpenAPI Client
    """
    pass


if settings.AUTH_TOKEN:
    coding_openapi_client = CodingDevOpsAPIClient()
