from flask import Flask, url_for, request, send_from_directory, abort
import json
import os
from dir_walker import get_all_meta

app = Flask(__name__)

print("Getting package list (might take a lot of ram with many packages)")
packages = get_all_meta()

@app.route("/")
def root():
    return "I am root /<br><a href='/api/packages'>Get list of packages (/api/packages)</a>"

@app.route("/api/packages")
def get_packages_all():
    global packages
    """dictionary = [
        {
            "author": "Marcin",
            "name": "tuxemon-main",
            "title": "Tuxemon",
            "short_description": "The base game",
            "release": 0
        },
        {
            "author": "Marcin",
            "name": "tuxemon-main",
            "title": "Tuxemon",
            "short_description": "The base game",
            "release": 0
        }
    ]"""
    returned = []
    for i in packages: 
        i["repo"] = request.host_url
        returned.append(i)
    return json.dumps(returned, indent=4)

@app.route("/api/packages/<name>")
def get_package_info(name):
    try:
        with open(f"packages/{name}/meta.json") as file:
            send = json.loads(file.read())
            return {**send, **{"repo": request.host_url}}
    except FileNotFoundError:
        abort(404)

@app.route("/api/packages/<name>/releases/")
def get_package_releases(name):
    return json.dumps(os.listdir(f"packages/{author.lower()}/{name}/releases"))

@app.route("/packages/<name>/releases/<release>/download")
def send_package(name, release):
    return send_from_directory(directory=f"packages/{name}/releases/{release}/", filename="pack.zip")


'''
with app.test_request_context():
    print(url_for('root'))
    print(url_for('return_path'))
    print(url_for('return_path', next='/'))
    #print(url_for('profile', username='John Doe'))
'''
