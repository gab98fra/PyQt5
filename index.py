# ----------------------------------------------------------------------------
# Nombre:       index.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       04 de diciembre 2020
# Modificado:   04 de diciembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Funciones básicas para trabajar con APIS
    Métodos:
        -GET
        -POST
        -HEADERS
        -PUT -  actualizar
        -DELETE
        -Dowload - ejemplo descarga de una imagen de la web

    python 3.8.2
    requests 2.25.0
    https://httpbin.org/#/HTTP_Methods

"""

import requests
import json

"""
def get_html():
#Método: get - args

    url="https://httpbin.org/get"

    #Parámetro a enviar
    args={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }
    
    #obtener respuesta - Enviar parámetro
    response=requests.get(url, params=args)

    if response.status_code==200:
        
        #Obtener Estructura html
        html=response.content        

        print(html)

        #Obtener la url
        print("\n", response.url)
    

def post ():
#Método: post -  data

    url="https://httpbin.org/post"

    #Parámetro a enviar
    payload={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }
    
    #Obtener respueata - Enviar parámetro
    response=requests.post(url, json=payload)#Los datos se incrustan en data

    if response.status_code==200:
        
        #Obtener el contenido
        content=response.content        

        print(content)

        #Obtener la url: se mantien oculto los parámetros enviados
        print("\n", response.url)
    

def header ():
#Encabezaados - headers

    url="https://httpbin.org/post"

    #Parámetro a enviar
    payload={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }
    
    #Indicar el envío en formato json
    headers={
        'Content-Type':"application/json",
        "access-token":"abcd",
    }

    #Obtener respuesta - enviar parámetros
    response=requests.post(url, json=payload, headers=headers)

    if response.status_code==200:
        
        #Leer el contenido del encabezado
        headers_response=response.headers#diccionario
        print(headers_response)

        #obtener el server
        print(headers_response["server"])

def put():
#Método PUT
    
    url="https://httpbin.org/put"

    #Parámetro a enviar
    payload={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }

    #Obtener respuesta- enviar parámetros
    response=requests.put(url, json=payload)

    if response.status_code==200:
        
        #Leer el contenido del
        content=response.content
        
        print(content)

        #obtener la url
        print(response.url)

def delete():
#Método PUT
    
    url="https://httpbin.org/delete"

    #Parámetro a enviar
    payload={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }

    #Obtener respyesta - enviar parámetros
    response=requests.delete(url, json=payload)

    if response.status_code==200:
        
        #Leer el contenido del
        content=response.content
        
        print(content)

        #obtener la url
        print(response.url)


def dowload():
#Descargar imagen de la red
    
    url="https://www.oxfordstudent.com/wp-content/uploads/2019/05/rad-cam.jpg"
    
    #obtener respuesta - Enviar parámetro 
    response=requests.get(url, stream=True) #Sream deja la conexión abierta

    if response.status_code==200:
        
        with open("image_descargada.jpg", "wb") as file:
        #Descarga la imagen
            
            for img in response.iter_content():
            #Descarga el archivo poco a poco
                file.write(img)
            

    #Cerrar conexión
    response.close()

if __name__ == "__main__":
    
    
    get_html()
    post()
    header()
    put()
    delete()
    dowload()

"""

#Link API: https://pokeapi.co/

def get():
#Método: get - args

    url="https://pokeapi.co/api/v2/pokemon-form"

    #obtener respuesta -  enviar url como parámetro
    response=requests.get(url)

    if response.status_code==200:
        
        #Obtener en formato json 
        json_data=response.json()
        
        #print(json_data)

        #Obtenemos los datos json de "results"
        results=json_data.get("results", "")
        
        if results:
        #Obtener los nombres de los pokémones

            for all in results:
                name=all['name']#accedemos al los datos name
                print(name)
        
    
    

if __name__ == "__main__":
    get()