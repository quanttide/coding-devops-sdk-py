import unittest

from coding_devops_sdk.openapi.client import coding_openapi_client
from coding_devops_sdk.config import settings


class ProjectAPITestCase(unittest.TestCase):
    def test_describe_project_by_name(self):
        return_data = coding_openapi_client.describe_project_by_name(project_name=settings.TEST_PROJECT_NAME)
        self.assertTrue(return_data)


if __name__ == '__main__':
    unittest.main()
