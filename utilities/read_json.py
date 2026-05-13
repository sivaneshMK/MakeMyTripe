import json
import os.path


class ReadJson:

    @staticmethod
    def get_config(env):

        root_path = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(root_path,
                                 "config",
                                 f"{env}.json")

        with open(file_path) as file:
            return json.load(file)

