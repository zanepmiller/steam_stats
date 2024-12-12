import pytest

import os

from src import parse_apps as pa

#region Test Values
INV_PATH = f"Z:/invalid/path"
J_TXT = '''
{
 "applist": {
  "apps": [
   {
    "appid": 1941401,
    "name": "Test App 0"
   },
   {
    "appid": 2170321,
    "name": "Test App 1: 骸骷王"
   },
   ]
}
'''

@pytest.fixture(scope='session')
def text_file(tmp_path_factory):
    txt = f"Invalid text"
    fn = tmp_path_factory.mktemp('test') / 'test.txt' 
    with open(fn, 'w') as o_file:
        print(txt, file=o_file)
    return fn

@pytest.fixture(scope='session')
def poison_json_file(tmp_path_factory):
    txt = f"Invalid text"
    fn = tmp_path_factory.mktemp('test') / 'test.json'
    with open(fn, 'w') as o_file:
        print(txt, file=o_file)
    return fn

@pytest.fixture(scope='session')
def json_file(tmp_path_factory):
    txt = J_TXT
    fn = tmp_path_factory.mktemp('test') / 'test.json'
    with open(fn, 'w') as o_file:
        print(txt, file=o_file)
    return fn

#endregion

#region read_applist
def test_read_applist_no_file():
    ### Tests an invalid filename returns None
    assert pa.read_applist(INV_PATH) == None

def test_read_applist_not_json(text_file):
    ### Tests a non-json file returns None
    assert pa.read_applist(text_file) == None

def test_read_applist_bad_json(poison_json_file):
    ### Tests an invalid json file returns None
    assert pa.read_applist(poison_json_file) == None

def test_read_applist_test_json(json_file):
    ### Tests an invalid json file returns None
    assert pa.read_applist(json_file) == None

#endregion