"""vk-api-schema to sanbox app."""
import json
import os
import shutil

import urllib3

import insomnia
import postman
import vscode_restclient

BUILD_FOLDER = "build"
JSON_SCHEMA_URL = "https://raw.githubusercontent.com/VKCOM/vk-api-schema/master/methods.json"
TAGS_SCHEMA_URL = "https://api.github.com/repos/VKCOM/vk-api-schema/tags"


def getVersion():
    """Return last version."""
    user_agent = {'user-agent': 'urllib3'}
    http = urllib3.PoolManager(headers=user_agent)
    r = http.request('GET', TAGS_SCHEMA_URL, preload_content=False)

    tags = json.loads(r.data.decode('utf-8'))
    last_tag_name = tags[0]["name"].split(".")
    return last_tag_name[0] + "." + last_tag_name[1]


def downloadSchema():
    """Return object schema."""
    http = urllib3.PoolManager()
    r = http.request('GET', JSON_SCHEMA_URL, preload_content=False)

    return json.loads(r.data.decode('utf-8'))


if __name__ == "__main__":
    if os.path.exists(BUILD_FOLDER):
        shutil.rmtree(BUILD_FOLDER, ignore_errors=True)
    os.makedirs(BUILD_FOLDER)

    schema = downloadSchema()
    version = getVersion()

    vscode_restclient.handler(schema, BUILD_FOLDER, version)
    insomnia.handler(schema, BUILD_FOLDER, version)
    postman.handler(schema, BUILD_FOLDER, version)
