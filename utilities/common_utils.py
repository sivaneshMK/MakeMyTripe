from conftest import config


class CommonUtils:

    @staticmethod
    def get_config(config, key):
        return config[key]