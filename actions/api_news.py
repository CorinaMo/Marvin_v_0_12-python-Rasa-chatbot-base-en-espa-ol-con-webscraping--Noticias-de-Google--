import requests
from bs4 import BeautifulSoup
import re

# Función de webscraping con el buscador de noticias de Google.
# Coge la ruta del buscador de noticias y le pasa el parámetro (la categoría de noticias del slot querynews)
# Las etiquetas de clase sacadas con webscraping

def apiBuscaGoogleNews(param):

    resp = requests.get('https://www.google.es/search?tbm=nws&q=noticias+{}'.format(str(param)))
    soup = BeautifulSoup(resp.content, 'html.parser')
    lista = soup.find_all(class_="ZINbbc xpd O9g5cc uUPGi")
    noticias = " \n Noticias de {} según Google: \n \n  ".format(str(param)) 
    noticia = []

    i=0
    for l in lista:
        if ( i < 6):
            qtitulo = l.find(class_="BNeawe vvjwJb AP7Wnd") 
            fuente = l.find(class_="BNeawe UPmit AP7Wnd")
            pattern = re.compile('http.*\.html')
            qfragmento = l.find(class_="BNeawe s3v9rd AP7Wnd")
            qlink = l.find(class_="kCrYT")
            link = re.search(pattern, str(qlink.a))
            
           # Ordenando los datos extraidos de las noticias
            newsbloque= str('( ' + fuente.text + ' ) ' )
            
            if qtitulo:
                newsbloque += qtitulo.text + ' \n '

            if qfragmento:
                newsbloque = newsbloque + 'Fragmento: << ' + qfragmento.text + '>>.' +' \n '
        
            if link:
                newsbloque = newsbloque + 'Link: ' + link.group(0) + ' \n \n '
            else:
                pattern2 = re.compile('http.*\/&amp')              
                link_alt = re.search(pattern2, str(qlink.a))

                if link_alt :
                    int_1 = link_alt.span(0)[0]
                    int_2 = link_alt.span(0)[1] -4
                    p = str(qlink.a)[int_1:int_2]
                
                    newsbloque = newsbloque + 'Link: ' + p + ' \n \n '
                       
            noticia.append(newsbloque)             
            i=i+1

    resultado = [str(noticias),noticia[0],noticia[1],noticia[2],noticia[3],noticia[4],noticia[5]]
    return resultado
  