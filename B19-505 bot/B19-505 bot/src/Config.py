class Config(object):
    def __init__(self, config_filename):
        dic = {}
        with open(config_filename) as cred:
            for line in cred.readlines():
                tmp = line.split('=')
                dic[tmp[0]] = tmp[1].replace('\n', '')

        self.token = dic['token']
        self.group_id = dic['group_id']


