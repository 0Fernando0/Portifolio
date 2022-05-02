from BackEnd import Scraping

manga = input('manga: '.title()).strip().replace(' ','-')

html = Scraping(f'https://muitomanga.com/manga/{manga}')
print(f'{html.listacapitulos()} capitulos disponiveis'.title())

capitulo = input('capitulo: '.title()).strip()
print('baixando...'.title())
paginas = Scraping(f'https://muitomanga.com/ler/{manga}/capitulo-{capitulo}')
paginas.baixar_paginas(manga,capitulo)

print('download concluido\nboa leitura!'.title())