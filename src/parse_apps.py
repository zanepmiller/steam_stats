import json
import os
import datetime

import numpy as np
import pandas as pd

import requests as req
from bs4 import BeautifulSoup
import lxml #   bs4 documentation says this is faster than the standard Python html parser

def read_applist(target : str) -> pd.DataFrame:
    if not os.path.isfile(target) : return None
    with open(target, encoding='utf-8') as j_file:
        try:
            app_j = json.load(j_file)
            return pd.read_json(app_j)
        except json.JSONDecodeError:
            return None

if __name__ == '__main__':
#region Argument Parsing
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', required=True)

    args = parser.parse_args()
#endregion

#region App Request
    applist_path = os.path.abspath(args.target)
    if not os.path.isfile(applist_path):
        print(f"Provided target {args.target} resolved to {applist_path}, which is not a valid file.")
        exit(0)

    app_df = read_applist(os.path(applist_path))

#endregion