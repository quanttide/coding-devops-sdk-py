import unittest

from coding_devops_sdk.openapi.client import coding_openapi_client
from coding_devops_sdk.config import settings


class DepotAPITestCase(unittest.TestCase):
    def test_describe_project_depot_info_list(self):
        data = coding_openapi_client.describe_project_depot_info_list(project_id=settings.TEST_PROJECT_ID)
        self.assertTrue(data)
        print(data)


class IntegratedDepotAPITestCase(unittest.TestCase):
    def test_describe_project_depot_info_list_by_name(self):
        data = coding_openapi_client.describe_project_depot_info_list_by_name(project_name=settings.TEST_PROJECT_NAME)
        self.assertTrue(data)
        print(data)


if __name__ == '__main__':
    unittest.main()
