import os

from seeq import spy
from seeq.spy import _login
from seeq.base import gconfig


def login(url=None):
    key_path = os.path.join(gconfig.get_data_folder(), 'keys', 'agent.key')
    credentials = open(key_path, "r").read().splitlines()

    spy.login(credentials[0], credentials[1], url=url)


def get_client():
    return _login.client
