import configparser
import os
import errno


class Config():
    """
    セッティング保持クラス
    """
    def __init__(self):
        self.config_file = 'setting.ini'
        path_to_config_file = './conf/{}'.format(self.config_file)
        if not os.path.exists(path_to_config_file):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                path_to_config_file
            )
        self._parser = configparser.ConfigParser()
        self._parser.read(path_to_config_file, encoding='utf_8')

    @property
    def host(self):
        section = 'DEFAULT'
        key = 'Host'
        return self._parser.get(section, key)

    @property
    def port(self):
        section = 'DEFAULT'
        key = 'Port'
        return self._parser.get(section, key)

    @property
    def user(self):
        section = 'DEFAULT'
        key = 'User'
        return self._parser.get(section, key)

    @property
    def key_file(self):
        section = 'DEFAULT'
        key = 'KeyFile'
        return self._parser.get(section, key)

    @property
    def pass_phrase(self):
        section = 'DEFAULT'
        key = 'PassPhrase'
        return self._parser.get(section, key)

    @property
    def target_file(self):
        section = 'DEFAULT'
        key = 'TargetFile'
        return self._parser.get(section, key)

    @property
    def to_file(self):
        section = 'DEFAULT'
        key = 'ToFile'
        return self._parser.get(section, key)
