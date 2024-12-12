import os
import datetime
import json

import requests as req

def req_app_list(target : str):
    app_list_path = f"{target}/applist_{datetime.datetime.today().hour}.{datetime.datetime.today().minute}.json"

    if os.path.isfile(target):
        if __name__ == '__main__': print(f"{target} already exists.")
        return
    elif not target.endswith('.json'):
        if not os.path.isdir(target):
            os.mkdir(target)
    elif target.endswith('.json'):
        app_list_path = target
    else:
        raise ImportError(f"{target} was not a valid directory or .json name!")

    r = req.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
    with open(app_list_path, mode='w', encoding='UTF8') as file:
        j = json.loads(r.text)
        json.dump(j, file, indent=1)
        if __name__ == '__main__': print(f"Wrote applist to {file.name}.")

if __name__ == '__main__':
#region Argument Parsing
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', default=os.getcwd(),
        help='Target location for applist.json to be placed. Defaults to '+\
              'current working directory. A file name will overwrite the '+\
              'default filename of applist_<hour>_<minute>.json.')

    args = parser.parse_args()
#endregion

#region App List Collection
    j_applist = req_app_list(args.input)
#endregion