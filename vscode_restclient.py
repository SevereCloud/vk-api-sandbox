import shutil
import os


def handler(schema, build_folder, version):
    folder_path = build_folder + '/vscode-restclient'

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path, ignore_errors=True)
    os.makedirs(folder_path)

    not_empty = []

    for method in schema["methods"]:
        file_name = method["name"].split('.')[0]
        file_path = f'{folder_path}/{file_name}.http'

        with open(file_path, 'a') as f:

            if file_name not in not_empty:
                # first line
                f.write('@baseUrl = https://api.vk.com/method\n')
                f.write(f'@v={version}\n\n')
                f.write('@access_token=TOKEN_HERE\n\n')
                not_empty.append(file_name)

            f.write(f'###\n\n')

            if method.get('description'):
                f.write(f'// {method["description"]}\n')
            f.write(f'// https://api.vk.com/method/{method["name"]}\n')

            f.write('POST {{baseUrl}}/' + f'{method["name"]}\n')
            f.write('Content-Type: application/x-www-form-urlencoded\n\n')

            if method.get('parameters'):
                if len(method["parameters"]) > 0:
                    f.write(f'{method["parameters"][0]["name"]}=\n')

                    for parameter in method["parameters"][1:]:
                        f.write(f'&{parameter["name"]}=\n')

                    f.write('&v={{v}}\n')
                else:
                    f.write('v={{v}}\n')
            else:
                f.write('v={{v}}\n')
            f.write('&access_token={{access_token}}\n\n')
    shutil.make_archive(
        f"{build_folder}/restclient-vk-api-sandbox",
        "zip",
        folder_path)
    shutil.rmtree(folder_path, ignore_errors=True)
