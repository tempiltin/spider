#!/usr/bin/env python

import requests

def request(url):
    try:
        return  requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "samtuit.uz"
with open("/root/PycharmProjects/pythonProject/crawler/subdomain.list", "r") as wordlist_file:
     for line in wordlist_file:
         word = line.strip()
         test_url = word +"."+ target_url # subdomain uchun
         # test_url = target_url + "/" + word
         respone = request(test_url)

         if respone:
             print("[+] Aniqlangan subdomain ----------> " + test_url)
