# -*- coding: utf-8 -*-
from crawl.crawl_adress import CrawlAdress

cep = raw_input("Informe o CEP: ").replace("-","")

crawl = CrawlAdress(cep)

crawl.getAdress()


