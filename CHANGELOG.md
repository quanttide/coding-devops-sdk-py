# CHANGELOG

## [v0.1.0] - 2022-06-17

Minimal available version. Add `OpenAPIClient`。

### Features

OpenAPI(`OpenAPIClient`):
- low-level API: `request_api`.
- high-level API: `describe_project_by_name`, `describe_project_depot_info_list`, `describe_git_releases`.
- integrated API: `describe_project_depot_info_list_by_name`, `get_depot_id_by_name`, `describe_git_releases_by_name`. 

Workflows:
- PyPI publish