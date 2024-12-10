#   This test suite ended up being pointless, as all collect_apps.py does is 
#   request the list of steam apps from the web api and save it in a readable
#   format. Maintaining the file for future extension.

import pytest

def test_pytest():
    ### Ensure pytest is installed and working.
    assert True