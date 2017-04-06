#! /usr/bin/env python
# -*- encoding: utf8 -*-
#This makes possible to run this program as a script invoking the interpreter

#########################
##     HEADER INFO     ##
#########################

__author__ = "Kike Puma"
__copyright__ = "Copyright 2007, CosasDePuma"
__credits__ = ["KikePuma", "CosasDePuma"]
__license__ = "GNU-3.0"
__version__ = "1.1 BoboCrawler"
__maintainer__ = "KikePuma"
__email__ = "kikefontanlorenzo@gmail.com"
__status__ = "In development"

########################
##       COLORS       ##
########################

#Color change: "\033[cod_formato;cod_texto;cod_fondom"
CERROR = "\n\033[1;31m" #BOLD RED
CGREEN = "\033[1;32m" #GREEN
CWHITE = "\033[1;37m" #WHITE
CRED = "\033[0;31m" #RED
CBLUE = "\033[1;34m" #BLUE
CDEFAULT = "\033[0m" #DEFAULT COLOR
CREDITS = "\033[2;37m" #LIGHT WHITE

#########################
##     REQUIREMENTS    ##
#########################

try:
    import requests
except ImportError:
    print(CERROR + "[ERROR] Please, install REQUESTS module\n[ERROR] Try to use 'pip install requests' or 'pip install --upgrade requests'" + CDEFAULT)
    exit(0)

#########################
##      FUNCTIONS      ##
#########################

def Crawl(url):

    #Init variable
    crawler = requests.models.Response()
    #Crawling
    while True:
        try:
            crawler = requests.post(url) #Make the connection
            break
        except requests.exceptions.ConnectionError:
            crawler.status_code = 900 #Connection failed
            break
        except requests.exceptions.MissingSchema:
            url = 'http://' + url #Fix the URL
    return crawler.status_code

def BoboResponse(code):
    response = {
            200: 'La solicitud es correcta y la pagina web existe',
            301: 'La solicitud es correcta pero redirige a otra pagina',
            400: 'La solicitud contiene sintaxis erronea y no deberia repetirse',
            401: 'La solicitud fue legal, pero el servidor rehusa responderla dado que el cliente no tiene los privilegios para hacerla, pero tampoco cambiaria nada de tenerlos',
            403: 'La solicitud fue legal, pero el servidor rehúsa responderla dado que no tienes los privilegios para hacerla',
            405: 'La solicitud fue legal pero requiere algun tipo de parametro. De todas formas, la pagina existe',
            404: 'Recurso no encontrado. La pagina web es posible que no exista',
            410: 'El contenido solicitado ya no esta disponible y no lo estara de nuevo',
            451: 'El contenido ha sido eliminado como consecuencia de una orden judicial o sentencia emitida por un tribunal',

            900: 'La URL no existe o has insertado una URL invalida',
            901: 'BoboCrawler todavia no soporta peticiones a IPs'
            }
    return response.get(code, "El codigo recibido es " + str(code) + " pero Bobo no sabe que significa")

#########################
##       DEBUGGER      ##
#########################

if __name__ == '__main__':
    import sys
    try:
        url = sys.argv[1]
    except IndexError:
        print("[ERROR] Usage: python Bobo-Crawl.py [url]")
        exit(0)
    response = Crawl(url)
    print (url, response, BoboResponse(response))
