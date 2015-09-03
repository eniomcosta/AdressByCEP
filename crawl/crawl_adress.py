# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

class CrawlAdress:

	def __init__(self,cep):
		self.crawl_url = ('http://www.buscacep.correios.com.br/servicos/dnec/consultaLogradouroAction.do?'+
					'relaxation='+cep+'&'+
					'Metodo=listaLogradouro&'+
					'TipoConsulta=relaxation&'+
					'StartRow=1&EndRow=10')

		self.html = self.getHTML()

	def getAdress(self):
		soup = BeautifulSoup(self.html, 'html.parser')

		if soup.find_all("title")[1].get_text() == "Erro":
			print "Não foi encontrado nenhum endereço com o CEP informado"
			return
		else:
			trs = soup.find("table",{"bgcolor" : "gray"}).tr

			properties = ['Logradouro','Bairro','Localidade','UF','CEP']
			cont = 0

			for td in trs.find_all("td"):
				print properties[cont]+": "+td.get_text()
				cont+=1

	def getHTML(self):
		return urllib2.urlopen(self.crawl_url).read()

	def showURL(self):
		print self.crawl_url
