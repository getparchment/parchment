import yaml


class ReadConfig:
    '''read config from .yaml config file
    '''
    def __init__(self, config_file_src, config=None):
        self.config_file = open(config_file_src, 'r')
        self._config = self._read_config()

    def __del__(self):
        if not self.config_file.closed:
            self.config_file.close()

    def _read_config(self):
        return yaml.load(self.config_file)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def get_config_keys(self):
        return list(self._config.keys())

    '''
    @property
    def title(self):
        return self.config['title']

    @property
    def author(self):
        return self.config['author']

    @property
    def bio(self):
        return self.config['bio']

    @property
    def social(self):
        return self.config['social']

    @property
    def contact(self):
        return self.config['contact']

    @property
    def theme(self):
        return self.config['theme']
    '''

'''
a = ReadConfig('/home/gao/project/parchment/config.yaml')
config_keys_list = a.get_config_keys()
for key in config_keys_list:
    value = a._config[key]
    print(value)
'''
