import requests
import json


proxies = {
  'http': 'http://172.67.182.159:80',
  'https': 'http://46.4.242.214:1337',
}
cookies = {
    #КУКИ СЮДАААА
}

headers = {
    #HEADERS СЮДА
}

params = {
    "username": "hereare0318", # СЮДА ЮСЕРНЕЙМ
}

response = requests.get(
    "https://www.instagram.com/api/v1/users/web_profile_info/",
    params=params,
    headers=headers,
    cookies=cookies,
    proxies=proxies
)
print(response.json()["data"]["user"]["profile_pic_url_hd"])