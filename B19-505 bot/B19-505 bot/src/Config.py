import json

class Config(object):
    token = None
    group_id = None

    def load(config_filename):
        dic = {}
        with open(config_filename) as cred:
            data = json.loads(cred.read())

        Config.token    = data['token']
        Config.group_id = data['group_id']

