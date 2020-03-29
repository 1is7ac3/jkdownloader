#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  webControl.py
#  
#  Copyright 2020 Unknown <isaac@1is7ac3>
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

def GetUrl(Url):
	try:
		page=requests.get(Url)
	except:
		print ("[!] Error al Conectar!")
		return False
	page=html.fromstring(page.content)
	return page
