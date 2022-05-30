import unittest

from coding_devops_sdk.openapi.client import coding_openapi_client
from coding_devops_sdk.config import settings


class BaseAPIClientTestCase(unittest.TestCase):
    def test_request_api(self):
        data = coding_openapi_client.request_api(
            action='DescribeProjectByName',
            ProjectName=settings.TEST_PROJECT_NAME,
        )
        self.assertTrue(data)
        self.assertTrue('Project' in data)


if __name__ == '__main__':
    unittest.main()
