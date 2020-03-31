#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  Module control.py
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
#  
#
import requests
from lxml import html
import os
import re
pgweb='https://jkanime.net/'
class Serie:
	def __init__(self, name, num, url):
		self.name=name
		self.num=num
		self.url=url
#Clase capitulo 		
class Capitulo:
	def __init__(self, url, name):
		self.url=url
		self.name=name
def sleep(n):
	
	os.system('sleep '+str(n))
	
def version():
	print('JkDownloader v:1.0\n')
	print('from Isaac Quiroz')

def GetUrl(Url):
	try:
		page=requests.get(Url)
	except:
		print ("[!] Error al Conectar!")
		return False
	page=html.fromstring(page.content)
	return page
	
def Clear():
	if os.name=="posix":
		os.system('clear')
	else:
		os.system('cls')
	return
	
def Download(capitulo,savePath):
	#Variable para control ciclo
	i=0
	saveFile=savePath+'/'+capitulo[i].name
	while  i<len(capitulo):
		n=str(i)
		dl='youtube-dl -o ''"'+saveFile+'.mp4''"'+' '+capitulo[i].url
		#Llama el comando desde el terminal
		er=os.system(dl)
		if er!=0 and not os.path.isfile(saveFile+'.mp4'):
			i+=1
		elif er!=0 and os.path.isfile(saveFile+'.mp4'):
			er=os.system(dl)
		else:
			i=len(capitulo)

def showResult(results):
	#Ciclo por si se introduce un dato erróneo 
	while True:
		#Imprime Instrucciones
		print('Seleccione el numero que desea descargar:\n')
		#Ciclo para imprimir todos los resultados
		for bus in results:
			n=str(bus.num)
			print ('[',n,']',bus.name)
		#Imprime información y captura el numero a usar
		choice=input('\n Introduzca el numero a Descargar: ')
		#Comprueba si el dato entrante es un numero
		if choice.isdigit():
			#si es un numero convierte la variable en un entero 
			choice=int(choice)
			#Compara que el entero introducido este en la lista impresa
			if choice>=len(results):
				print ('\n[!] Error!. El numero no esta en la lista. Presione ENTER para re-intentar.')
				#input()
			else:
				return choice
		else:
			print ('\n[!]Error! Introduzca un Numero. Presione ENTER para re-intentar.')
			
def getVideo(url):
	
	page=GetUrl(url)
	#Extrae el enlace de descarga
	fulljs=page.xpath('//script/text()')
	buscript=re.findall('jk.php\?u=(.*)/"',str(fulljs))
	videoUrl=pgweb+buscript[0]
	#Extrae el nombre del capitulo
	epNames = page.xpath('//div[@class="video-header"]/h1/text()')
	#Extrae el nombre del servidor de descarga
	seNames=page.xpath('//ul[@class="server-tab"]//a/text()')
	#Crea lista vaciá
	capitulo=[]
	capitulo.append(Capitulo(videoUrl, epNames[0]))
	#Retorna lista
	return capitulo 
