#!/usr/bin/python3
# -*- coding: utf-8 -*-
#	
#	Module newEpisode.py
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
import os
import control
		
	# Realiza la busqueda de enlaces
def SearchEngine():
	searchUrl='http://jkanime.net'
	page=control.GetUrl(searchUrl)
	serieLinks=page.xpath('//div[@class="overview"]//a[@class="odd"]/@href')
	serieNames=page.xpath('//div[@class="overview"]//a[@class="odd"]//h2/text()')
	linkNum=len(serieLinks)
	if linkNum!=len(serieNames):
		print ('[!] Error Faltan Enlaces!')
		return False
	# Crear lista Serie
	serieList=[]
	for n in range(0, linkNum):
		serie=control.Serie(serieNames[n],n,serieLinks[n])
		serieList.append(serie)
	return serieList
		
def main():
	#Mostrar Series Encontradas
	busque=SearchEngine()
	choice=control.showResult(busque)
	#Mostrar Servidores de Descarga
	servi=control.getVideo(busque[choice].url)
	#Ubicacion de Descarga 	
	path=os.environ['HOME']+'/.Anime'
	#Nombre Carpeta
	if not os.path.exists(path):
		os.mkdir(path)
	savePath = os.path.join(path, busque[choice].name)
	if not os.path.exists(savePath):
		os.mkdir(savePath)
	descarga=control.Download(servi, savePath)
	
if __name__=="__main__":
		while True:
				main()
