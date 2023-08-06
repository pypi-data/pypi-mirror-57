import os
import time
import json
import requests
from hashlib import sha1


class Client:
    def __init__(self, app_key, app_id):
        """
        :param app_key: your app key
        :param app_id: your app id
        """
        self.app_key = app_key
        self.app_id = app_id
        self.base_url = "http://127.0.0.1:5000"

    def send(self, request):
        url = self.base_url + request.path
        if request.method == 'POST':
            return self.__post(request, url)
        if request.method == "GET":
            return self.__get(request, url)

    def __get(self, request, url):
        response = requests.get(url,
                                headers=self.__get_headers(),
                                data=json.dumps(request.get_body_parameters()))
        return response.json()

    def __post(self, request, url):
        response = requests.post(url,
                                headers= self.__get_headers(),
                                data=request.get_body_parameters())
        return response.json()

    def __delete(self, request, url):
        response = requests.delete(url,
                                headers= self.__get_headers(),
                                data=request.get_body_parameters())
        return response.json()


    def __get_headers(self):
        headers = {}
        headers['appKey'] = self.app_key
        headers['appId'] = self.app_id
        return headers
