import requests
from bs4 import BeautifulSoup


def get_all_best_sellers_100():
    #Se recorren las paginas de los libros mas vendidos de la 1 a la 10
        for page_number in range(0,11):
            print('A continuación se muestran los libros de la página '+ str(page_number) + '\n')
            datos = get_main_news(page_number)
            
            for libros_mas_vendidos in datos:
                print('=================================')
                print(libros_mas_vendidos)
                print('=================================')
                print('\n')
            
            
        
# La función get_main_news retornará un diccionario con todas las urls, títulos y autor de libros encontrados en la sección principal.
def get_main_news(page_number):
    url = 'https://www.todostuslibros.com/mas_vendidos?page='+str(page_number)

    respuesta = launch_request(url)

    contenido_web = BeautifulSoup(respuesta.text, 'html.parser')

# Buscar la etiqueta ul, que tenga la clase books, que es la lista que contiene todas las urls. 
    libreria = contenido_web.find('ul', attrs={'class':'books'})
# Con el resultado de esa búsqueda, utilizaremos findChildren para encontrar todos los divs que usen la clase que book-details que es la que contiene la url, el título y el autor,
# esto nos devolverá una lista con todos los resultados encontrados.
    libros = libreria.findChildren('div', attrs={'class':'book-details'})

# Después recorreremos la lista para obtener la url, el título, para ello usaremos el siguiente código:
    datos = [];
    for libro in libros:
        datos.append({
            'url': libro.find('h2').a.get('href'),
			'titulo': libro.find('h2').get_text(),
			'autor' : libro.find('h3').get_text()
        })

    return datos


def launch_request(url):
    try:
        respuesta = requests.get(
            url,
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
        )
        respuesta.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return respuesta


if __name__ == '__main__':
    get_all_best_sellers_100()

		
