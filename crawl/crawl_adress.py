from bs4 import BeautifulSoup

class CrawlAdress(object):

	def __init__(self,cep):
		crawl_url = ('http://www.buscacep.correios.com.br/servicos/dnec/consultaLogradouroAction.do?'+
					'relaxation='+cep+'&'+
					'Metodo=listaLogradouro&'+
					'TipoConsulta=relaxation&'+
					'StartRow=1&EndRow=10')

	def getAdress(self):
		soup = BeautifulSoup(self.crawl_url, 'html.parser')

		print(soup.prettify())
