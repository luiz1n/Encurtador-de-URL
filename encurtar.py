import platform, os, json, re, sys

try:
	import requests
except:
	os.system("pip install requests")
	os.system("cls" if platform.system() == "Windows" else "clear")


def get_domain_suffixes():																
    res=requests.get('https://publicsuffix.org/list/public_suffix_list.dat')
    lst=set()
    for line in res.text.split('\n'):
        if not line.startswith('//'):
            domains=line.split('.')
            cand=domains[-1]
            if cand:
                lst.add('.'+cand)
    return tuple(sorted(lst))

domain_suffixes=get_domain_suffixes()

#https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not/65695825#65695825

a = ("http", "https", "www", "ftp")

def validarurl(url = ""):
	return True if url.startswith(a) or url.endswith(domain_suffixes) else False


class Encurtador:

	def __init__(self):
		self.Url = "https://abre.ai/_/generate"
		self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

		self.urlOriginal = ""
		self.urlEncurtada = ""

	def Encurtar(self, url = "", apelido = ""):
		if url != "":

			payloadRequest = {
				"url_translation":
				{	
					"url":url,
					"token": "" if apelido == "" else apelido
				}
			}
			r = requests.post(self.Url, json=payloadRequest, headers={"User-Agent": self.userAgent})
			if r.status_code == 201:
				os.system("cls" if platform.system() == "Windows" else "clear")
				dataJson = json.loads(r.text)['data']
				attributes = dataJson['attributes']
				token = attributes['token']
				self.urlOriginal = url
				self.urlEncurtada = f'https://abre.ai/{apelido}' if apelido != "" else f'https://abre.ai/{token}'
				Id = dataJson['id']
				print(f'-- Sucesso! -- \n\nUrl Original: {self.urlOriginal}\nUrl Encurtada: {self.urlEncurtada}\nID: {Id}')
			else:
				os.system("cls" if platform.system() == "Windows" else "clear")
				erro = json.loads(r.text)['errors']
				erroNome = re.search("{'(.+)': ", str(erro)).group().replace("'", "").replace(":", "").replace("{", "").strip()
				erro = erro[erroNome][0]
				print(f'Erro: {erro}')
		
def main(url, apelido):
	encurtador = Encurtador()
	encurtar = encurtador.Encurtar(url, apelido)

def erro(url):
	print(f'{url} => URL Inválida!')

def uso():
	os.system("cls" if platform.system() == "Windows" else "clear")
	print(f'----- Como usar ------')
	print('\nencurtar.py <*url*> <apelido>')
	print('\nExemplo sem apelido: encurtar.py https://google.com/')
	print('\nExemplo com apelido: encurtar.py https://google.com/ apelidofoda')
	exit()

try:
	URL = str(sys.argv[1])
	Apelido = str(sys.argv[2])
except:
	uso()

validar = validarurl(URL)

main(URL, Apelido) if validar else erro(URL)
