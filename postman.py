import json


def handler(schema, build_folder, version):
    file_path = build_folder + '/postman-vk-api-sandbox.json'

    obj = {
        "info": {
            "_postman_id": "95eacf86-9495-45aa-92c5-0ab478f1491f",
            "name": "VK API Sandbox",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": [],
        "variable": [
            {
                "id": "b4497c31-9cdf-4577-ac17-aad895f2e9dd",
                "key": "basic_url",
                "value": "https://api.vk.com/method",
                "type": "string"
            },
            {
                "id": "75f0bb78-d994-405f-a2a1-2cc699c932ff",
                "key": "v",
                "value": version,
                "type": "string"
            },
            {
                "id": "a308f436-2952-4eaa-89cf-26afc07368cf",
                "key": "access_token",
                "value": "",
                "type": "string"
            }
        ]
    }

    not_empty = {}

    for method in schema["methods"]:
        folder_name = method["name"].split('.')[0]

        if not not_empty.get(folder_name):
            folder = {
                "name": folder_name,
                "item": []
            }
            obj["item"].append(folder)

            not_empty[folder_name] = len(obj["item"]) - 1

        desc = ""
        if method.get("description"):
            desc = method.get("description")

        method_obj = {
            "name": method["name"],
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "name": "Content-Type",
                        "value": "application/x-www-form-urlencoded",
                        "type": "text"
                    }
                ],
                "body": {
                    "mode": "urlencoded",
                    "urlencoded": [
                        {
                            "key": "access_token",
                            "value": "{{access_token}}",
                            "description": "access token",
                            "type": "text"
                        },
                        {
                            "key": "v",
                            "value": "{{v}}",
                            "description": "version",
                            "type": "text"
                        }
                    ]
                },
                "url": {
                    "raw": "{{basic_url}}/" + method["name"],
                    "host": [
                        "{{basic_url}}"
                    ],
                    "path": [method["name"]]
                },
                "description": f'[vk.com/dev/{method["name"]}](https://vk.com/dev/{method["name"]})\n\n' + desc
            },
            "response": []
        }
        if method.get("parameters"):
            for parameter in method["parameters"]:
                disabled = True
                if parameter.get("required"):
                    disabled = False

                default = ""
                if parameter.get("default"):
                    default = parameter.get("default")

                description = ""
                if parameter.get("description"):
                    description = parameter.get("description")

                param = {
                    "key": parameter["name"],
                    "value": default,
                    "description": description,
                    "type": "text",
                    "disabled": disabled,
                }
                method_obj["request"]["body"]["urlencoded"].append(param)

        obj["item"][not_empty.get(folder_name)]["item"].append(method_obj)

    with open(file_path, 'a') as f:
        json.dump(obj, f)
