import json 


f_n = "song.txt"

s_txt = {'Sade':"Ziya-po ya-ya, pa-pa-ya-pa!Ti-da-lee,\
				na po-po pu-du-loo!\
				Ste--peh na-na po po-ro po!"} 


with open(f_n, 'w') as js:
	json.dump(s_txt, js)

with open(f_n) as js:
	res = json.load(js)
	print(res['Sade'])
