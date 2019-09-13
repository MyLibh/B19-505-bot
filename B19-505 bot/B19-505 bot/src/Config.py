class Config(object):
    token = None
    group_id = None

    def load(config_filename):
        dic = {}
        with open(config_filename) as cred:
            for line in cred.readlines():
                tmp = line.split('=')
                dic[tmp[0]] = tmp[1].replace('\n', '')

        Config.token    = dic['token']
        Config.group_id = dic['group_id']

