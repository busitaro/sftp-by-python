from os import remove

from ssh import Ssh
from config import Config


def fetch(ssh: Ssh, delete: bool = False):
    """
    指定のファイルをSSHサーバから取得する

    Params
    ---------
    ssh: Ssh
        ssh生成オブジェクト
    delete: bool
        取得ファイルをサーバから取得するかのフラグ

    """
    config = Config()

    # sftpセッション
    try:
        connect = ssh.create_ssh_connect()
        with connect.open_sftp() as connection:
            connection.get(config.target_file, config.to_file)
            if delete:
                # ファイルの削除
                connection.remove(config.target_file)
    except FileNotFoundError:
        print('fetch対象ファイルがありません。 {}'.format(config.target_file))
        remove(config.to_file)


def main():
    ssh = Ssh()
    fetch(ssh)


if __name__ == '__main__':
    main()
