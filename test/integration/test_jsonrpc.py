import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from dashd import DashDaemon
from dash_config import DashConfig


def test_dashd():
    config_text = DashConfig.slurp_config_file(config.dash_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00000c63f5826a523923939a5adf28657c2a6b76764f1af99bb39437006489d3'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00000341adf1dd4375bef8ff8059b4268fe0282d8a66f8cf5419bd6b13fbb77b'

    creds = DashConfig.get_rpc_creds(config_text, network)
    dashd = DashDaemon(**creds)
    assert dashd.rpc_command is not None

    assert hasattr(dashd, 'rpc_connection')

    # Dash testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    info = dashd.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert dashd.rpc_command('getblockhash', 0) == genesis_hash
