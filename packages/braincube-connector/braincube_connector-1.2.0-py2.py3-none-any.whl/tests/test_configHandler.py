
# class TestConfigHandler(TestCase):
from braincube.bc_connector.config_handler import is_config_filled, get_verify, _read_config_from_dict



def test_is_config_filled_ko_01():
    assert is_config_filled({"client_secret": "", "client_id": ""}) is False


def test_is_config_filled_ko_02():
    assert is_config_filled({"client_secret": "", "client_id": "test"}) is False


def test_is_config_filled_ko_03():
    assert is_config_filled({"client_secret": "test", "client_id": ""}) is False


def test_is_config_filled_ok():
    assert is_config_filled({"client_secret": "test", "client_id": "test"}) is True


def test_no_verify():
    global config

    config_verify = {"client_secret": "test", "client_id": "test", 'verify':True}
    config_no_verify = {"client_secret": "test", "client_id": "test", 'verify':False}
    config_certchain = {"client_secret": "test", "client_id": "test", 'verify':'hi mom'}
    config_none_certchain = {"client_secret": "test", "client_id": "test", 'verify':None}
    config_emptycertchain = {"client_secret": "test", "client_id": "test", 'verify':''}

    _read_config_from_dict(config_verify)
    assert get_verify() is True
    
    _read_config_from_dict(config_no_verify)
    assert get_verify() is False

    _read_config_from_dict(config_certchain)
    assert get_verify() == 'hi mom'

    # cases where the config is bad
    _read_config_from_dict(config_none_certchain)
    assert get_verify() is True

    _read_config_from_dict(config_emptycertchain)
    assert get_verify() is True

