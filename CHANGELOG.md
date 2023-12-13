# CHANGELOG

## [v0.1.2] - 2023-12-13

### Add 

- OpenAPI: Add `modify_git_transfer` API.

### Bugfix

- OpenAPI: Fix `describe_project_depot_info_list` and `get_depot_id_by_name` internal parameter usage error.

## [v0.1.1] - 2022-07-05

### Bugfix

OpenAPI:
- Fix internal parameter usage error of `describe_git_releases_by_name`.

## [v0.1.0] - 2022-06-17

Minimal available version. Add `OpenAPIClient`。

### Features

OpenAPI(`OpenAPIClient`):
- low-level API: `request_api`.
- high-level API: `describe_project_by_name`, `describe_project_depot_info_list`, `describe_git_releases`.
- integrated API: `describe_project_depot_info_list_by_name`, `get_depot_id_by_name`, `describe_git_releases_by_name`. 

Workflows:
- PyPI publish