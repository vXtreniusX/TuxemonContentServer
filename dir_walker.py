import os
import json

def get_all_meta(path="packages"):
    """ 'Walks' through all directories, looking for meta.json """
    conbined_dict = []
    for a in os.listdir(path):  # Authors...
        for b in os.listdir(os.path.join(path, a)):  # Names
            print(a, b)
            with open(os.path.join(path, a, b, "meta.json")) as file:
                conbined_dict.append(
                    json.loads(file.read())
                )
    return conbined_dict
