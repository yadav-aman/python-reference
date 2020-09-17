#! /usr/bin/env python3
import os
import requests

os.chdir('/data')

dictionary = {"title": "", "name": "", "date": "", "feedback": ""}

for files in os.listdir():
    with open(files,'r') as file:
        data = file.read().split('\n')
        dictionary["title"] = data[0];
        dictionary["name"] = data[1];
        dictionary["date"] = data[2];
        dictionary["feedback"] = data[3];
        response = requests.post("http://<IP of server>/feedback/",json=dictionary)
        print(response.status_code)
        if (response.status_code == 201):
          print("Feedback Added")
        else :
          response.raise_for_status()