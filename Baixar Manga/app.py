from playwright.sync_api import sync_playwright
import os,requests

def app():
    manga = input("nome do manga: ")  
    with sync_playwright() as play:
        nav = play.chromium.launch(channel='chrome',headless=True)

        page = nav.new_page(base_url='https://muitomanga.com/')
        
        page.goto('manga/'+manga.replace(' ','-'))
        for capitulo in (page.locator('div.single-chapter>a').all_text_contents()):
            print(capitulo)
        cap_selecionado = input('Qual Capitulo Baixar: ')
        
        
        page.goto('ler/'+manga.replace(' ','-')+'/capitulo-'+cap_selecionado)
        
        paginas = (page.locator('select.select_paged>option').count())
        try:
            os.makedirs(f'Manga/{manga}/{cap_selecionado}')
        except:
            pass
        for c in range(paginas+1):
            page.locator('a#chimagenext').click()
            
            link = (page.locator('img#imagech').get_attribute('src'))

            
            with open(f'Manga/{manga}/{cap_selecionado}/imagem{c}.jpg','wb') as file:
                file.write(requests.get(link).content)          
               
        nav.close() 

app()