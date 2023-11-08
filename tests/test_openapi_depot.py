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

    def test_get_depot_id_by_name(self):
        depot_id = coding_openapi_client.get_depot_id_by_name(
            depot_name=settings.TEST_DEPOT_NAME,
            project_name=settings.TEST_PROJECT_NAME,
        )
        self.assertEqual(settings.TEST_DEPOT_ID, depot_id)

    @unittest.skip('测试通过，待优化测试使之可复用')
    def test_modify_git_transfer_by_name(self):
        new_depot_path = coding_openapi_client.modify_git_transfer_by_name(
            source_project_name=settings.TEST_SOURCE_PROJECT_NAME,
            source_depot_name=settings.TEST_SOURCE_DEPOT_NAME,
            target_project_name=settings.TEST_TARGET_PROJECT_NAME,
        )
        self.assertTrue(new_depot_path)


class ReleaseAPITestCase(unittest.TestCase):
    def test_describe_git_releases(self):
        data = coding_openapi_client.describe_git_releases(depot_id=settings.TEST_DEPOT_ID)
        self.assertTrue(data)


class IntegratedReleaseAPITestCase(unittest.TestCase):
    def test_describe_git_releases_by_name(self):
        data = coding_openapi_client.describe_git_releases_by_name(
            project_name=settings.TEST_PROJECT_NAME,
            depot_name=settings.TEST_DEPOT_NAME,
            status=1
        )
        self.assertTrue(data)


if __name__ == '__main__':
    unittest.main()
