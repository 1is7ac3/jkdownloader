#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  JK
#  
#  Copyright 2020 Isaac Quiroz <isaac.qa13@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
'''
Autor: Isaac Quiroz
Objetivo: Descarga de todos los capítulos de una serie
'''  
import control
import os

#Función Para la captura de los datos de la serie a descargar
def SearchInput():
	#Ciclo para la captura  
	while True:
		#Imprime versión de la app
		control.version()
		#Imprime sugerencia
		print('Debido al diseño de la pagina solo se mostraran diez coincidencias.\n')
		#Captura el nombre de la serie a buscar
		search=input('Introduzca el nombre de la serie que desea descargar: \n')
		#Lanza la función de búsqueda
		bus=SearchEngine(search)
		#Revisa que la búsqueda halla obtenido resultados
		if bus != []:
			return bus
		#Si no encuentra resultados repite el ciclo
		else:
			print ('[!]No se encontró, intente nuevamente \n')	
#función de búsqueda
def SearchEngine(search):
	#Une el nombre de la búsqueda con la pagina
	searchUrl='http://jkanime.net/buscar/'+search+'/1/'
	#Se revisa el estado de la pagina
	page=control.GetUrl(searchUrl)
	#Captura los enlaces de las diez primeras series
	Links=page.xpath('//h2[@class="portada-title"]/a/@href')
	#Captura el nombre de las series desde la pagina web
	Names=page.xpath('//h2[@class="portada-title"]/a/text()')
	# Revisa que los nombres coincidan en numero con los enlaces
	linkNum=len(Links)
	if linkNum!=len(Names):
		print ('[!] Error Faltan Enlaces!')
		return False
	# Crear lista
	serieList=[]
	#Guarda los datos obtenidos usando la clase Anime
	for n in range(0, linkNum):
		serie=control.Serie(Names[n],n,Links[n])
		serieList.append(serie)
	return serieList

#Función para descargar todos los capítulos  		
def GetAllCap(url,title):
	#Imprime versión
	control.version()
	#Se obtiene nombre de usuario
	#Se crea variable con la dirección donde se va a guardar 
	path=os.environ['HOME']+'/.Anime'
	if not os.path.exists(path):
		os.mkdir(path)
	#se unen la ruta de descarga con la carpeta donde se van a guardar los capítulos
	savePath=os.path.join(path, title)
	#Se crea la capeta si no se existe
	if not os.path.exists(savePath):
		os.mkdir(savePath)
	#Se verifica la url de los capítulos
	page=control.GetUrl(url)
	#se extrae los datos del numero de paginas 
	pageLink=page.xpath('//div[@class="navigation"]/a/text()')
	#Se obtiene el numero de paginas 
	linkpa=len(pageLink)
	#Obtener el numero del primer capitulo de la ultima pagina 
	ini=str(((linkpa-1)*10)+1)
	#Variable que almacena el texto de la ultima pagina ej:21 - 24 
	exac=pageLink[linkpa-1]
	#Obtener cuantos capítulos tiene la serie.   
	ran=int(exac.replace(ini+' - ',''))
	#Ciclo para descarga delos capítulos
	inide=1
	print('desea descargar por rango.\n[0] Sí.\n[*] No.\n')
	opts=input('Introduzca su opción:\n')
	if opts==0:
		inide=int(input('Introduzca primer capitulo para iniciar:\n'))
		finde=-1
		while finde==-1:
			print('si desea descargar hasta el ultimo capitulo disponible introduzca: 0\n')
			finde=int(input('Introduzca Ultimo capitulo para descargar:\n'))
			if finde>ran or finde<-1:
				print('No esta entre rango de capítulos disponible intente nuevamente.\n')
				finde=-1
			elif finde<ran and finde!=0:
				ran=finde
				finde=0
	else:
		print('se descargara desde el capitulo',inide,'hasta',ran,':')
	for n in range(inide,(ran+1)):
		#Variable donde se convierte en texto para ser usado en la url del capitulo 
		capi=str(n)
		#Se une la url con el numero del capitulo a descargar
		url2=url+capi+'/'
		servi=control.getVideo(url2)
		control.Download(servi,savePath) 
		                        
#Función principal
def main():
	#Llama la función para la entrada de la búsqueda
	buscar=SearchInput()
	#Llama la función para mostrar resultado de la búsqueda
	choice=control.showResult(buscar)
	#Obtiene nombre de la serie para la carpeta
	title = buscar[choice].name
	#Llama la función para descargar todo los capítulos 
	capall=GetAllCap(buscar[choice].url, title)
#Ciclo para repetir todo 
if __name__ == "__main__":
		while True:
				main()
