import paramiko

from config import Config


class Ssh:
    def create_ssh_connect(self) -> paramiko.client.SSHClient:
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
        return ssh
