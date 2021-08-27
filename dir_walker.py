import os
import json

def get_all_meta(path="packages"):
    """ 'Walks' through all directories, looking for meta.json """
    conbined_dict = []
    for a in os.listdir(path):  # Names
        print(a)
        try:
            with open(os.path.join(path, a, "meta.json")) as file:
                conbined_dict.append(
                    json.loads(file.read())
                )
        except FileNotFoundError:
            pass
    return conbined_dict
