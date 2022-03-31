# -*- coding: utf-8 -*-

from dynaconf import Dynaconf


# 默认配置文件
default_settings_files = ['settings.toml']

# 声明式配置实例
settings = Dynaconf(
    settings_files=default_settings_files,
    environments=True,
    envvar_prefix='CODINGSDK',
    load_dotenv=True,
)
