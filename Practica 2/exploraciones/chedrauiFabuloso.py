from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time
import datetime
import json


def exploracion():
    #importar el driver de edge
    PATH = "msedgedriver.exe"
   

    options = EdgeOptions()
    options.use_chromium = True
    options.headless = True
    options.add_experimental_option(
        "excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--lang=en_US.utf-8')
    
    driver = Edge(options=options)
    driver = webdriver.Edge(PATH)    
    driver.maximize_window()

    pSoriana = []

    driver.get(
        "https://www.soriana.com/buscar?q=fabuloso&cid=&search-button=&page=2&cref=0&view=grid")
    html = ""
    # esperar 5 segundos
    time.sleep(6)
    # obtener el html de la pagina web link
    html = driver.page_source
    # iterar 20 veces para obtener los 20 productos de la pagina web
    for x in range(20):
        datos ='/html/body/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div['+str(x)+']/div[1]/div/div[1]/a/img'
        url = "/html/body/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div['+str(x)+']/div[1]/div/div[1]/a"

        try:

            objeto = driver.find_element(By.XPATH, datos)
            print(objeto)
            url = driver.find_element(By.XPATH, url)

            texto_json = (objeto.get_attribute("data-cbt"))
            ulr = url.get_attribute("href")

            objeto_json = json.loads(texto_json)

            # Acceder a la lista de productos
            productos = objeto_json['ecommerce']['click']['products']



            a = productos[0]
            nombre_producto = productos[0]['name']
            precio_producto = productos[0]['price']
            url_producto = ulr

            producto = {
                "precio": a['price'],
                "busqueda": "Fabuloso",
                "nombre": a['name'],
                "url": ulr,
                "tienda": "Soriana",
                "fecha": datetime.datetime.now().strftime("%Y-%m-%d")
            }

            pSoriana.append(producto)

        except Exception as e:
            objeto = ""
            print(e)
    time.sleep(2)
    driver.quit()

    return pSoriana
