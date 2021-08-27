from flask import Flask, url_for, request, send_from_directory, abort
import json

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
    return json.dumps(packages, indent=4)

@app.route("/api/packages/<author>/<name>")
def get_package_info(author, name):
    try:
        with open(f"packages/{author}/{name}/meta.json") as file:
            return file.read()
    except FileNotFoundError:
        abort(404)

@app.route("/packages/<author>/<name>/releases/<release>/download")
def send_package(author, name, release):
    return send_from_directory(directory=f"packages/{author.lower()}/{name}/releases/{release}/", filename="pack.zip")


'''
with app.test_request_context():
    print(url_for('root'))
    print(url_for('return_path'))
    print(url_for('return_path', next='/'))
    #print(url_for('profile', username='John Doe'))
'''
