from requests.exceptions import HTTPError,ConnectionError,InvalidURL
import requests,os
from bs4 import BeautifulSoup

class Scraping:
    def __init__(self,url):
        self.url = url

    def requisição(self):
        user = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        try:
            self.html = requests.get(self.url,headers=user)
        except HTTPError:
            return None
        except ConnectionError:
            return None
        except InvalidURL:
            return None
        if not self.html.status_code == 200:
            return None
        return self.html

    def parser(self):
        try:
            self.soup = BeautifulSoup(self.html.text,'html.parser')
        except:
            return None
        return self.soup

    def listacapitulos(self):
        self.requisição()
        self.parser()
        try:
            capitulos = self.soup.select('.single-chapter a')
        except:
            return None
        cont = 0
        for capitulo in capitulos:
            if str(capitulo).startswith('<a href'):
                cont += 1
        return cont-1

    def criar_pasta(self,manga,capitulo):
        try:
            os.makedirs(f'Manga/{manga}/cap {capitulo}')
        except FileExistsError:
            pass

    def listapaginas(self):
        self.requisição()
        self.parser()
        try:
            paginas = self.soup.select('.select_paged option')
        except:
            return None
        cont = 0
        for pag in paginas:
            cont += 1
        return cont

    def baixar_paginas(self,manga,capitulo):
        self.criar_pasta(manga,capitulo)
        self.requisição()
        paginas = self.listapaginas()

        for c in range(1,paginas):
            res = requests.get(f'https://imgs.muitomanga.com/imgs/{manga}/{capitulo}/{c}.jpg').content
            with open(f'Manga/{manga}/cap {capitulo}/pagina{c}.jpg','wb') as file:
                file.write(res)


