"""vk-api-schema to sanbox app."""
import os
import shutil

import requests

import insomnia
import postman
import vscode_restclient

BUILD_FOLDER = "build"
JSON_SCHEMA_URL = "https://raw.githubusercontent.com/VKCOM/vk-api-schema/master/methods.json"
TAGS_SCHEMA_URL = "https://api.github.com/repos/VKCOM/vk-api-schema/tags"


def getVersion():
    """Return last version."""
    tags = requests.get(TAGS_SCHEMA_URL).json()
    last_tag_name = tags[0]["name"].split(".")
    major = ''.join(filter(lambda x: x.isdigit(), last_tag_name[0]))
    minor = ''.join(filter(lambda x: x.isdigit(), last_tag_name[1]))
    return major + "." + minor


def downloadSchema():
    """Return object schema."""
    return requests.get(JSON_SCHEMA_URL).json()


if __name__ == "__main__":
    if os.path.exists(BUILD_FOLDER):
        shutil.rmtree(BUILD_FOLDER, ignore_errors=True)
    os.makedirs(BUILD_FOLDER)

    schema = downloadSchema()
    version = getVersion()

    vscode_restclient.handler(schema, BUILD_FOLDER, version)
    insomnia.handler(schema, BUILD_FOLDER, version)
    postman.handler(schema, BUILD_FOLDER, version)
