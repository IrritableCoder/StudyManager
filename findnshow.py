import os
from pathlib import Path


def fns():
    dir_path = "MYSQL DATABASE DIRECTORY"

    dir_list = []

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            dir_list.append(Path(path).stem)

    print("Avalable Tables:")
    for f in dir_list:
        print("> "+f)

    return dir_list
