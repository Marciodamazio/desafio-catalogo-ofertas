from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def obter_dados_produto():
    
    chrome_driver_path = r"C:\Users\MARCIO DAMAZIO\Desktop\chromedriver\chromedriver-win64\chromedriver.exe"

   
    chrome_binary_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_binary_path 

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    
    url = 'https://lista.mercadolivre.com.br/computador-gamer-i7-16gb-ssd-1tb'

    
    driver.get(url)

    
    time.sleep(5)

    
    page_source = driver.page_source

    
    soup = BeautifulSoup(page_source, 'html.parser')

    
    produtos = soup.find_all('li', {'class': 'ui-search-layout__item'})

    lista_produtos = []
    precos_produtos = []  

    for produto in produtos:
        nome_produto = produto.find('h2', {'class': 'ui-search-item__title'}).text.strip()
        preco_produto = produto.find('span', {'class': 'price-tag-fraction'}).text.strip()
        imagem_produto = produto.find('img', {'class': 'ui-search-result-image__img'})['src']
        link_produto = produto.find('a', {'class': 'ui-search-link'})['href']
        
        try:
            preco_antigo = produto.find('span', {'class': 'price-tag__discount'}).text.strip()
        except AttributeError:
            preco_antigo = None

        try:
            frete_gratis = 'Frete grátis' in produto.text
        except AttributeError:
            frete_gratis = False

        
        preco_produto_num = float(preco_produto.replace('R$', '').replace('.', '').replace(',', '.'))

        
        produto_info = {
            'nome': nome_produto,
            'preco': preco_produto,
            'imagem': imagem_produto,
            'link': link_produto,
            'preco_antigo': preco_antigo,
            'frete_gratis': frete_gratis
        }

        lista_produtos.append(produto_info)
        precos_produtos.append(preco_produto_num)

    # Fecha o navegador
    driver.quit()

    
    if precos_produtos:
        maior_preco = max(precos_produtos)
        menor_preco = min(precos_produtos)

       
        print(f"Maior Preço: R$ {maior_preco:,.2f}")
        print(f"Menor Preço: R$ {menor_preco:,.2f}")
    else:
        print("Não foi possível encontrar preços.")


    for produto in lista_produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']}")
        print(f"Imagem: {produto['imagem']}")
        print(f"Link: {produto['link']}")
        print(f"Preço sem Desconto: {produto['preco_antigo']}")
        print(f"Frete Grátis: {produto['frete_gratis']}")
        print("-" * 40)

    return lista_produtos


produtos = obter_dados_produto()
print("Raspagem concluída!")
