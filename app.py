"""
    Ejemplo del manejo de hilos - silvia ramirez
"""

import os
import requests
import time
import csv
import threading
#import subprocess

#Listado de sitios de educación en línea a nivel general

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        
        for row in lineas:
            numero = row[0].strip()
            url = row[1].strip()
            lista.append((numero,url))
    return lista

def worker(numero, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    pagina = requests.get(url)
    nombre_archivo = f"{numero}.txt"
    ruta_archivo = os.path.join("output",nombre_archivo)
    with open(ruta_archivo,'w') as archivo:
        archivo.writelines(pagina.txt)
    print (f"Archivo guardado: {nombre_archivo}")
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # en la función
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...',
                            target=worker,
                            args=(numero, url))
    hilo1.start()