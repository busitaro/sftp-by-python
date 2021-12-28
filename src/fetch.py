from os import remove

from ssh import Ssh
from config import Config


def fetch(ssh: Ssh):
    config = Config()

    # sftpセッション
    try:
        connect = ssh.create_ssh_connect()
        with connect.open_sftp() as connection:
            connection.get(config.target_file, config.to_file)
    except FileNotFoundError:
        print('fetch対象ファイルがありません。 {}'.format(config.target_file))
        remove(config.to_file)


def main():
    ssh = Ssh()
    fetch(ssh)


if __name__ == '__main__':
    main()
