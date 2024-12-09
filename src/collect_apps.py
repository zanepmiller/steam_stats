import os
import sys
import time

import requests as req
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import lxml #   bs4 documentation says this is faster than the standard Python html parser

if __name__ == '__main__':
#region Argument Parsing
    import argparse
    parser = argparse.ArgumentParser()

    args = parser.parse_args()
#endregion