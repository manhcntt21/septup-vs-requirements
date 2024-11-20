from distutils.core import setup
from distutils.command.install import install
import os

HOME = os.path.expanduser('~')


def post_install():
    user_home = os.path.expanduser('~')

    # Định nghĩa các thư mục và files
    config_dir = os.path.join(user_home, '.config', 'mypkg')
    default_dir = os.path.join(user_home, '.local', 'share', 'mypkg')
    share_dir = os.path.join(user_home, '.local', 'share', 'docs', 'mypkg')

    # Tạo thư mục
    os.makedirs(config_dir, exist_ok=True)
    os.makedirs(share_dir, exist_ok=True)


class CustomInstall(install):
    def run(self):
        install.run(self)
        self.execute(post_install, [], msg="Running post install task")


setup(
    name='mypackage',
    version='1.0',
    packages=['mypkg'],
    data_files=[
        (os.path.join(HOME, '.config', 'mypkg'), ['data/config.init']),
        (os.path.join(HOME, '.local', 'share', 'mypkg'), ['data/default.json']),
        (os.path.join(HOME, '.local', 'share', 'docs', 'mypkg'), ['docs/examples.txt']),
    ],
    cmdclass={'install': CustomInstall}
)

