#izvestaj.py
import pretraga
import datetime

#moze se desiti greska da ako imas namestaj sa istim nazivom i kategorijom da napravi problem u izvestaju ali to resi nekako


def izvestajGrananje():
	while True:
		izvestajGrananjeMenu()
		komanda=izvestajGrananjeKomanda()
		if komanda==0:
			print("Povratak u prethodni menu")
			return
		elif komanda==1:
			print("Izabrali ste 'Izvestaj o ukupnoj prodaji po danima'")
			izvestajPoDanima()
		elif komanda==2:
			print("Izabrali ste 'Izvestaj o ukupnoj prodaji po kategorijama'")
			izvestajPoKategorijama()


def izvestajGrananjeMenu():
	print("\nNalazite se na mainMenu/izvestajGrananje")
	print("Dobro dosli u izvestaj, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Izvestaj o ukupnoj prodaji po danima")
	print("2 - Izvestaj o ukupnoj prodaji po kategorijama")

def izvestajGrananjeKomanda():
	komanda="komanda"

	while not izvestajGrananjeKomandaUslov(komanda):
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	return komanda

def izvestajGrananjeKomandaUslov(komanda):
	return komanda==0 or komanda==1 or komanda==2


def izvestajPoDanima():
	print("Unesite pocetno vreme")
	datum1=pretraga.unesiDatum()
	print("Unesite krajnje vreme")
	datum2=pretraga.unesiDatum()
	listaRecnikaRacuna=pretraga.ucitajRecnikeRacuna()
	listaTrazenih=pretraga.pretragaSelekcijaRacunaDatum(listaRecnikaRacuna,datum1,datum2)

	srediIzvestajDani(listaTrazenih,datum1,datum2)


def srediIzvestajDani(listaTrazenih,datum1,datum2):
	print("-------------------+--------------------")
	print("Izvestaj po danima {0}.{1}.{2}-{3}.{4}.{5}".format(datum1.day,datum1.month,datum1.year,datum2.day,datum2.month,datum2.year))
	print("-------------------+--------------------")
	print("       DATUM       |       PROMET       ")
	print("-------------------+--------------------")
	ukupanPrometPeriod=0
	ukupanPrometZaDatum=0
	i=0
	if len(listaTrazenih)==0:
		print("Pogresan interval datuma za izvestaj")
		return
	datumTemp=datetime.date(listaTrazenih[0]["vreme"]["godina"],listaTrazenih[0]["vreme"]["mesec"],listaTrazenih[0]["vreme"]["dan"])

	for recnik in listaTrazenih:
		datumRecnika=datetime.date(recnik["vreme"]["godina"],recnik["vreme"]["mesec"],recnik["vreme"]["dan"])

		if datumTemp==datumRecnika:
			ukupanPrometZaDatum=ukupanPrometZaDatum+recnik["ukupnaCena"]
			i=i+1

		else:
			ispisIzvestajDani(datumTemp,ukupanPrometZaDatum)
			datumTemp=datumRecnika
			ukupanPrometPeriod=ukupanPrometPeriod+ukupanPrometZaDatum
			ukupanPrometZaDatum=recnik["ukupnaCena"]
			i=i+1

	ukupanPrometPeriod=ukupanPrometPeriod+ukupanPrometZaDatum
	ispisIzvestajDani(datumTemp,ukupanPrometZaDatum)
	ispisUkupne(ukupanPrometPeriod)


def ispisIzvestajDani(datumRecnika,ukupanPrometZaDatum):
	print("{0}.{1}.{2}          |{3:^20}".format(datumRecnika.day,datumRecnika.month,datumRecnika.year, ukupanPrometZaDatum))

def ispisUkupne(ukupanPrometPeriod):
	print("-------------------+--------------------")
	print("Ukupan promet      |{0:^20}".format(ukupanPrometPeriod))
	print("-------------------+--------------------")


def izvestajPoKategorijama():
	print("Unesite pocetno vreme")
	datum1=pretraga.unesiDatum()
	print("Unesite krajnje vreme")
	datum2=pretraga.unesiDatum()
	listaRecnikaRacuna=pretraga.ucitajRecnikeRacuna()
	listaTrazenih=pretraga.pretragaSelekcijaRacunaDatum(listaRecnikaRacuna,datum1,datum2)


	listaTraznihRecnikaKategorija=srediIzvestajKategorije(listaTrazenih)
	
	izbrisiDuplikate(listaTraznihRecnikaKategorija)
	ispisIzvestajKategorije(listaTraznihRecnikaKategorija,datum1,datum2)


def srediIzvestajKategorije(listaTrazenih):
	izvestajRecnici=[]

	for recnik in listaTrazenih:
		for index in range(len(recnik["kategorije"])-1):
			if len(izvestajRecnici)==0:
				noviRecnik=napraviRecnikIzvestajKategorija(recnik,index)
				izvestajRecnici.append(noviRecnik)
			elif recnik["kategorije"][index]=="":
				continue
			else:
				noviRecnik=napraviRecnikIzvestajKategorija(recnik,index)
				izvestajRecnici.append(noviRecnik)

	return izvestajRecnici




def izbrisiDuplikate(listaTraznihRecnikaKategorija):
	duzinaListe=len(listaTraznihRecnikaKategorija)


	i=0
	while i<=duzinaListe-1:
		j=i+1
			
		while j<=duzinaListe-1:
			if listaTraznihRecnikaKategorija[i]["naziv"]==listaTraznihRecnikaKategorija[j]["naziv"]:
				listaTraznihRecnikaKategorija[i]["kolicina"]=listaTraznihRecnikaKategorija[i]["kolicina"]+listaTraznihRecnikaKategorija[j]["kolicina"]
				listaTraznihRecnikaKategorija[i]["cena"]=listaTraznihRecnikaKategorija[i]["cena"]+listaTraznihRecnikaKategorija[j]["cena"]
				listaTraznihRecnikaKategorija[i]["promet"]=listaTraznihRecnikaKategorija[i]["promet"]+listaTraznihRecnikaKategorija[j]["promet"]
				if listaTraznihRecnikaKategorija[i]["profitNamestaja"]<listaTraznihRecnikaKategorija[j]["profitNamestaja"]:
					listaTraznihRecnikaKategorija[i]["najprofNamestaj"]=listaTraznihRecnikaKategorija[j]["najprofNamestaj"]
					listaTraznihRecnikaKategorija[i]["profitNamestaja"]=listaTraznihRecnikaKategorija[j]["profitNamestaja"]
				del listaTraznihRecnikaKategorija[j]
				j=j-1
				duzinaListe=duzinaListe-1
				

			j=j+1

		i=i+1



def napraviRecnikIzvestajKategorija(recnik,index):
	noviRecnik={}
	noviRecnik["naziv"]=recnik["kategorije"][index]
	noviRecnik["cena"]=float(recnik["cene"][index])
	noviRecnik["kolicina"]=int(recnik["kolicine"][index])
	noviRecnik["promet"]=float(recnik["cene"][index])*int(recnik["kolicine"][index])
	noviRecnik["najprofNamestaj"]=recnik["nazivi"][index]
	noviRecnik["profitNamestaja"]=int(recnik["cene"][index])*int(recnik["kolicine"][index])

	return noviRecnik




def ispisIzvestajKategorije(listaTraznihRecnikaKategorija,datum1,datum2):
	sortirajIzvestajPromet(listaTraznihRecnikaKategorija)
	print("--------------------------------------------------------------------------------")
	print("Izvestaj po kategorijama {0}.{1}.{2}  -  {3}.{4}.{5}".format(datum1.day,datum1.month,datum1.year,datum2.day,datum2.month,datum2.year))
	print("--------------------+--------------+------------------+------------------------+")
	print("     Kategorija     |   Kolicina   |      Promet      | Najprof. kom. namestaja|")
	print("--------------------+--------------+------------------+------------------------+")
	for recnik in listaTraznihRecnikaKategorija:
		print("{0:^20}|{1:^14}|{2:^18}|{3:^24}".format(recnik["naziv"],str(recnik["kolicina"]),str(recnik["promet"]),recnik["najprofNamestaj"]))
	print("--------------------+--------------+------------------+------------------------+")


def sortirajIzvestajPromet(listaTraznihRecnikaKategorija):
	listaTraznihRecnikaKategorija.sort(key=lambda x: x["promet"], reverse=True)
	


	# period na koji se odnosi 
	# kategorija    |    kol    | promet (cena ukupna za taj period) | naziv namestaja koji je najprofitabilniji (kol * cena) u okviru te kategorije | profit od njega

	# 1. ucitam racune
	# 2. uzmem 1. kategoriju, pitam da li je u listi naziva kategorija, ako nije dodam i idem redom kroz recnike i sabiram kolicinu, cena*kolicina,
	# a ako jeste idem na 2. kategoriju u prvom recniku. 




	# listaRecnikaNamKolProm=[] imace recnike {naziv, kategorija, promet od tog namestaja}	

	# napravices listu malih recnik u koju ces staviti naziv namestaja kol, i profit ukupan i kategorija
	# ako nije u toj listi recnika (naziv nije u vrednostima liste recnika) onda dodaj
	# svaki put kad naidjes udji lociraj dotaj kol, profit
	# ocisti listu del c[:]

	# kad izvrti sve ovo pitaj da li je 
	# to ta kategorija 
	# 	jeste pitaj uzmi protit prvog kao max
	# 			idi redom pitaj da li je neki profit veci
	# 				ako je veci u recniku stavi da je naziv=naziv
					
	# del listaTraznihRecnikaKategorija[len(listaTraznihRecnikaKategorija)-1]
	# del listaTraznihRecnikaKategorija[len(listaTraznihRecnikaKategorija)-1]
	# del listaTraznihRecnikaKategorija[len(listaTraznihRecnikaKategorija)-1]
	# del listaTraznihRecnikaKategorija[len(listaTraznihRecnikaKategorija)-1]

	# for i in range(duzinaListe-1):
	# 	for j in range(duzinaListe-1):
	# 		if listaTraznihRecnikaKategorija[i]["naziv"]==listaTraznihRecnikaKategorija[j]["naziv"]:
	# 			listaTraznihRecnikaKategorija[i]["kolicina"]=listaTraznihRecnikaKategorija[i]["kolicina"]+listaTraznihRecnikaKategorija[j]["kolicina"]
	# 			listaTraznihRecnikaKategorija[i]["cena"]=listaTraznihRecnikaKategorija[i]["cena"]+listaTraznihRecnikaKategorija[j]["cena"]
	# 			listaTraznihRecnikaKategorija[i]["promet"]=listaTraznihRecnikaKategorija[i]["promet"]+listaTraznihRecnikaKategorija[j]["promet"]
	# 			if listaTraznihRecnikaKategorija[i]["profitNamestaja"]<listaTraznihRecnikaKategorija[j]["profitNamestaja"]:
	# 				listaTraznihRecnikaKategorija[i]["najprofNamestaj"]==listaTraznihRecnikaKategorija[j]["najprofNamestaj"]
	# 				listaTraznihRecnikaKategorija[i]["profitNamestaja"]==listaTraznihRecnikaKategorija[j]["profitNamestaja"]
	# 				j=j-1
	# 				duzinaListe=duzinaListe-1
					


	# listaTraznihRecnika=[]
	# noviRecnik={}
	# for recnik in listaTrazenih:
	# 	for index in range(len(recnik["kategorije"])-2):
	# 		if proveriRecnikIzvestajKateogorija(recnik,index,listaTraznihRecnika):
	# 			continue
	# 		else:
	# 			if recnik["kategorije"][index]=="":
	# 				continue
	# 			else:
	# 				noviRecnik=napraviRecnikIzvestajKategorija(recnik,index)
	# 				listaTraznihRecnika.append(noviRecnik)


	# return listaTraznihRecnika
	#listaTraznihRecnika=[{naziv:sto, cena:19, kolicina:10, nazivNamestaja:ikea-23, profit(cena*kol:202)},]


	# izvestajRecnici=[]

	# for recnik in listaTrazenih:
	# 	for index in range(len(recnik["kategorije"])-2):
	# 		if len(izvestajRecnici)==0:
	# 			noviRecnik=napraviRecnikIzvestajKategorija(recnik,index)
	# 			izvestajRecnici.append(noviRecnik)
	# 		else:
	# 			for kategorija in izvestajRecnici:
	# 				if recnik["kategorije"][index]=="":
	# 					continue
	# 				elif recnik["kategorije"][index] in list(kategorija.values()):
	# 					print(list(kategorija.values()))
						
	# 					if kategorija["naziv"]==recnik["kategorije"][index]:
	# 						kategorija["kolicina"]=kategorija["kolicina"]+int(recnik["kolicine"][index])
	# 						kategorija["cena"]=kategorija["cena"]+int(recnik["cene"][index])
	# 						kategorija["promet"]=kategorija["promet"]+float(recnik["cene"][index])*int(recnik["kolicine"][index])
	# 						profitNamURecniku=int(recnik["cene"][index])*int(recnik["kolicine"][index])
	# 						if profitNamURecniku>kategorija["profitNamestaja"]:
	# 							kategorija["profitNamestaja"]=profitNamURecniku
	# 							kategorija["najprofNamestaj"]=recnik["nazivi"][index]
	# 							print("AAAAAAAAAAAAAAAAAAAAAAA")


	# 				else:
	# 					noviRecnik=napraviRecnikIzvestajKategorija(recnik,index)
	# 					izvestajRecnici.append(noviRecnik)

	# return izvestajRecnici
	# def proveriRecnikIzvestajKateogorija(recnik,index,listaTraznihRecnika):
# 	for kategorija in listaTraznihRecnika:
# 		if kategorija["naziv"]==recnik["kategorije"][index]:
# 			kategorija["kolicina"]=kategorija["kolicina"]+int(recnik["kolicine"][index])
# 			kategorija["promet"]=kategorija["promet"]+float(recnik["cene"][index])*int(recnik["kolicine"][index])
# 			profitNamURecniku=int(recnik["cene"][index])*int(recnik["kolicine"][index])
# 			if profitNamURecniku>kategorija["profitNamestaja"]:
# 				kategorija["profitNamestaja"]=profitNamURecniku
# 				kategorija["najprofNamestaj"]=recnik["nazivi"][index]
# 			return True
# 	return False

