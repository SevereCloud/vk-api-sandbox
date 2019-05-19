import json
import random
import string
import time
from datetime import datetime


def timeNow():
    return int(time.time() + 0.5 * 1000)


def randomString(stringLength=32):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


def handler(schema, build_folder, version):
    file_path = build_folder + '/insomnia-vk-api-sandbox.json'

    wrk_id = "wrk_vk-api-sandbox"
    obj = {
        "_type": "export",
        "__export_format": 4,
        "__export_date": datetime.today().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "__export_source": "vk-api-sandbox",
        "resources": [
            {
                "_id": wrk_id,
                "created": 1558286019961,
                "description": "",
                "modified": timeNow(),
                "name": "VK API Sandbox",
                "parentId": None,
                "_type": "workspace"
            },
            {
                "_id": "env_vk-api-sandbox-basic",
                "color": None,
                "created": 1558286019961,
                "data": {
                    "basic_url": "https://api.vk.com/method",
                    "v": version
                },
                "isPrivate": False,
                "metaSortKey": timeNow(),
                "modified": timeNow(),
                "name": "Base Environment",
                "parentId": wrk_id,
                "_type": "environment"
            },
            {
                "_id": "env_vk-api-sandbox-secret",
                "color": None,
                "created": 1558286019961,
                "data": {
                    "access_token": "TOKEN HERE"
                },
                "isPrivate": True,
                "metaSortKey": timeNow(),
                "modified": timeNow(),
                "name": "Secret Environment",
                "parentId": "env_vk-api-sandbox-basic",
                "_type": "environment"
            }
        ]
    }
    not_empty = {}

    for method in schema["methods"]:
        folder_name = method["name"].split('.')[0]

        if not not_empty.get(folder_name):
            folder = {
                "_id": "fld_vk-api-sandbox-f-" + folder_name,
                "created": 1558286019961,
                "description": "",
                "environment": {},
                "metaSortKey": -timeNow(),
                "modified": timeNow(),
                "name": folder_name,
                "parentId": wrk_id,
                "_type": "request_group"
            }
            obj["resources"].append(folder)

            not_empty[folder_name] = folder["_id"]

        fld_id = not_empty.get(folder_name)

        desc = ""
        if method.get("description"):
            desc = method.get("description")

        method_obj = {
            "_id": "req_vk-api-sandbox-m-" + method["name"],
            "authentication": {},
            "body": {
                "mimeType": "application/x-www-form-urlencoded",
                "params": [
                    {
                        "id": "pair_" + randomString(),
                        "name": "access_token",
                        "value": "{{ access_token }}"
                    },
                    {
                        "id": "pair_" + randomString(),
                        "name": "v",
                        "value": "{{ v }}"
                    }
                ]
            },
            "created": 1558286019961,
            "description": f'[vk.com/dev/{method["name"]}](https://vk.com/dev/{method["name"]})\n\n' + desc,
            "headers": [
                {
                    "id": "pair_" + randomString(),
                    "name": "Content-Type",
                    "value": "application/x-www-form-urlencoded"
                }
            ],
            "isPrivate": False,
            "metaSortKey": -timeNow(),
            "method": "POST",
            "modified": timeNow(),
            "name": method["name"],
            "parameters": [],
            "parentId": fld_id,
            "settingDisableRenderRequestBody": False,
            "settingEncodeUrl": True,
            "settingRebuildPath": True,
            "settingSendCookies": False,
            "settingStoreCookies": False,
            "url": "{{ basic_url }}/" + method["name"],
            "_type": "request"
        }
        if method.get("parameters"):
            for parameter in method["parameters"]:
                disabled = True
                if parameter.get("required"):
                    disabled = False

                param = {
                    "disabled": disabled,
                    "id": "pair_",
                    "name": parameter["name"],
                    "value": parameter.get("default")
                }
                method_obj["body"]["params"].append(param)

        obj["resources"].append(method_obj)

    with open(file_path, 'a') as f:
        json.dump(obj, f)
