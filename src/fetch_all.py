import stat

from ssh import Ssh
from config import Config


def fetch_all(ssh: Ssh, delete: bool = False):
    """
    SSHサーバ上の指定ディレクトリから
    すべてのファイルを取得する

    Params
    ---------
    ssh: Ssh
        ssh生成オブジェクト
    delete: bool
        取得ファイルをサーバから取得するかのフラグ

    """
    config = Config()
    dir_path = config.target_dir

    # sftpセッション
    connect = ssh.create_ssh_connect()
    with connect.open_sftp() as connection:
        try:
            attrs = connection.listdir_attr(dir_path)
        except FileNotFoundError:
            print('fetch対象ディレクトリがありません。 {}'.format(dir_path))

        for attr in attrs:
            if attr.st_mode & stat.S_IFREG:
                # ファイルの場合
                connection.get(
                    '{}/{}'.format(dir_path, attr.filename),
                    '{}/{}'.format(config.to_dir, attr.filename)
                )
                if delete:
                    # ファイルの削除
                    connection.remove('{}/{}'.format(dir_path, attr.filename))


def main():
    ssh = Ssh()
    fetch_all(ssh)


if __name__ == '__main__':
    main()
