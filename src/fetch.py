from os import remove

import paramiko

from config import Config


def main():
    config = Config()

    rsa_key = paramiko.RSAKey.from_private_key_file(
        config.key_file, config.pass_phrase
    )

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        config.host,
        config.port,
        config.user,
        pkey=rsa_key
    )

    # sftpセッション
    try:
        with ssh.open_sftp() as connection:
            connection.get(config.target_file, config.to_file)
    except FileNotFoundError as ex:
        print('fetch対象ファイルがありません。 {}'.format(config.target_file))
        remove(config.to_file)


if __name__ == '__main__':
    main()
