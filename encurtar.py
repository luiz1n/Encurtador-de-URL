import json
import platform
import os

def Check():
	try:
		import requests
	except ImportError:
		os.system("python -m pip install requests")
		os.system("cls")

isWindows = platform.system() == "Windows"

Check()
import requests

class EncurtaADor:

	def __init__(self, url):

		self.encurtar1 = url
		self.url = "https://abre.ai/_/generate"
		self.user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"

	def Send(self):
		jsonkk = {"url_translation":{"url":self.encurtar1,"token":""}}
		headers = {'User-Agent': self.user_agent}
		r = requests.post(self.url, headers=headers, json=jsonkk)
		if r.status_code == 201:
			j = json.loads(r.text)
			splitted = str(j).split(':')
			token = splitted[9]
			token = str(token).split(',')
			token = str(token)
			t = token.replace('/', '')
			t = t.replace('[', '')
			t = t.replace('[', '')
			t = t.replace('"', '')
			t = t.replace("'", '')
			t = t.replace('}', '')
			t = t.replace(']', '')

			if isWindows:
				os.system("cls")
			else:
				os.system("clear")

			print(f'''

Informações

Link Original: {self.encurtar1}

[*] Link Encurtado: https://{t}/

				''')
		else:
			print('\nErro ao encurtar a url!')