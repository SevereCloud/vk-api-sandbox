# VK API Sandbox

[![Build Status](https://travis-ci.com/SevereCloud/vk-api-sandbox.svg?branch=master)](https://travis-ci.com/SevereCloud/vk-api-sandbox)
[![GitHub release](https://img.shields.io/github/release/SevereCloud/vk-api-sandbox.svg)](https://github.com/SevereCloud/vk-api-sandbox/releases)
[![GitHub issues](https://img.shields.io/github/issues/SevereCloud/vk-api-sandbox.svg)](https://github.com/SevereCloud/vk-api-sandbox/issues)
[![license](https://img.shields.io/github/license/SevereCloud/vk-api-sandbox.svg?maxAge=2592000)](https://github.com/SevereCloud/vk-api-sandbox/blob/master/LICENSE)

Этот репозиторий [содержит файлы](https://github.com/SevereCloud/vk-api-sandbox/releases) различных REST клиентов для работы с VK API. Автоматически собирается из 
[VK API JSON Schema](https://github.com/VKCOM/vk-api-schema/).

### Insomnia

После импорта json файла, в настройках Environment задайте `access_token`

```json
{
    "access_token": "TOKEN HERE"
}
```

![](https://pp.userapi.com/c851028/v851028188/11fa4e/XrhnPN1ybRQ.jpg)

### Postman

После импорта json файла, в Variables задайте `access_token` в поле **current value**

![](https://pp.userapi.com/c847019/v847019561/205eda/YzCD3jBjw2U.jpg)

### REST Client for VSCode

Представляет набор `.http` файлов для каждого раздела методов. Токен задается в начале файла

```
@access_token=TOKEN_HERE
```

![](https://pp.userapi.com/c851028/v851028188/11fa81/ug1jLmDUbbs.jpg)

### Хочу для %clientname%

Вы можете создать [Issue](https://github.com/SevereCloud/vk-api-sandbox/issues) или прислать [Pull request](https://github.com/SevereCloud/vk-api-sandbox/pulls)
