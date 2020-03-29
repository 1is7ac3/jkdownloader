#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  downloader.py
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
def Download(capitulo,saveFile):
        #Variable para control ciclo
        i=0
        while  i<len(capitulo):
                n=str(i)
                dl='youtube-dl -o ''"'+saveFile+' '+n+'.mp4''"'+' '+capitulo[i].url
                #Llama el comando desde el terminal
                er=os.system(dl)
                if er!=0 and not os.path.isfile(saveFile+' '+n+'.mp4'):
                        i+=1
                elif er!=0 and os.path.isfile(saveFile+' '+n+'.mp4'):
                  er=os.system(dl)
                else:
                        i=len(capitulo)
                        
