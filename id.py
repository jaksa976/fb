from requests import get,post
from json import loads
from sys import stdout,exit
from time import sleep
from os import remove as apus
print(' [ fb auto get id grup ]')
print(' [   coded by deray    ]')
print
try:
	token=open(raw_input('- list token lu : ')).read().split('\n')[0]
	limit=raw_input('- berapa banyak mau ngambil id member : ')
	id=raw_input('- id grup nya : ')
	output=open('id.txt','w')
	print("- starting ...")
	ambil=get('https://graph.facebook.com/'+id+'?access_token='+token).json()
	print "+ mengambil "+str(limit)+" id dari grup:",ambil['name']
	for x in get('https://graph.facebook.com/'+id+'/members?fields=id&limit='+str(limit)+'&access_token='+token).json()['data']:
		print("\r+ "+x['id']+" ..."),;stdout.flush();output.write(x['id']+"\n")
		sleep(000.001)
	print("\n+ done. "+str(limit)+" id terambil ")
	print("+ output: id.txt")
except:
	print('- gagal ambil token')
	apus('id.txt')
	exit()