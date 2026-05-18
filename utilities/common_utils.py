from conftest import config


class CommonUtils:

    @staticmethod
    def get_config(config, key):
        return config[key]

    @staticmethod
    def split(input="", split_by="|"):

        value = input.split(split_by)
        return value
