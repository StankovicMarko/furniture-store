#racun.py 

import datetime
import pretraga
import unosEntiteta

def prodaja(user):
	
	brojRacuna=utvrdiBrojRacuna()
	korpa=[]#{"naziv":"aa", "cena":1, "kolicina":2},{"naziv":"bb", "cena":2, "kolicina":3}] #lista recnika

	while True:
		ispisProdaja(brojRacuna,user,korpa)
		komanda=opcijeProdaje()
		if komanda==0:
			storniranjeKorpe(korpa)
			return
		elif komanda==1:
			recnik,sifra=prodajaDodajNamestaj()
			while sifra==None:
				recnik,sifra=prodajaDodajNamestaj()

			napraviIzmeneNamestaja(sifra,recnik)
			if proveraNamestajaUKorpi(recnik,korpa):
				continue
			else:
				korpa.append(recnik)


		elif komanda==2:
			recnik=prodajaDodajUslugu()
			if proveraUslugaUKorpi(recnik,korpa):
				continue
			else:
				korpa.append(recnik)


		elif komanda==3:
			if len(korpa)==0:
				print("Ne mozete da izdate racun ako niste nista dodali u korpu")
				return
			izdavanjeRacuna(brojRacuna,user,korpa)
			return



def utvrdiBrojRacuna():
	pretraga.proveriFajl("racuni.txt")
	f=open("racuni.txt","r")
	linije=f.readlines()
	f.close()
	return len(linije)




def ispisProdaja(brojRacuna,user,korpa):
	uCena=ukupnaCena(korpa)

	print("Prodavac:",user[2],user[3],"Username:",user[0])
	print("\n")
	print("Korpa izgleda ovako")
	print("------------------------------------------------------------")
	print("| broj racuna | naziv namestaja/usluge | jed. cena |  kol  |")
	print("------------------------------------------------------------")
	print("|{0:^13}|--------------------------------------------|".format(brojRacuna)) #vidi kako se ovo ponasa
	for recnik in korpa:
		print("|{0:^13}|{1:^24}|{2:^11}|{3:^7}|".format(" ",recnik["naziv"],str(float(recnik["cena"])), str(recnik["kolicina"])))
	print("------------------------------------------------------------")
	print("                                   Ukupan iznos:|{0:^10}|".format(uCena)) #vidi kako se ponasa
	print("------------------------------------------------------------")


def ukupnaCena(korpa):
	uCena=0
	for recnik in korpa:
		uCena=uCena+recnik["cena"]*recnik["kolicina"]
	return uCena


def opcijeProdaje():
	opcijeProdajeMenu()

	komanda="komanda"
 
	while not pretraga.uslovPretragaOpcijeNamestaj(komanda):#koristim funkciju iz drugog modula bitno da je komanda 0,1,2,3
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	return komanda
	

def opcijeProdajeMenu():
	print("da li zelite da ")
	print("0 - vratite se u prethodni meni")
	print("1 - prodate namestaj")
	print("2 - prodate uslugu")
	print("3 - izdaj racun")



def storniranjeKorpe(korpa):
	listaRecnikaNamestaja=pretraga.pretragaUcitajNamestaj()

	for recnikuFajlu in listaRecnikaNamestaja:
		for recnik in korpa:
			try:
				if recnik["sifra"]==recnikuFajlu["sifra"]:
					if recnikuFajlu["kolicina"]==0 and recnikuFajlu["obrisano"]=="true":
						recnikuFajlu["obrisano"]="false"
					recnikuFajlu["kolicina"]=recnikuFajlu["kolicina"]+recnik["kolicina"]
			except KeyError:
				continue

	stringZaUpis=unosEntiteta.recnikToStringNamestaj(listaRecnikaNamestaja)
	unosEntiteta.upisiString(stringZaUpis,"namestaj.txt")


def prodajaDodajNamestaj():
	listaTrazenih=pretraga.p_pretragaNamestaj()

	while len(listaTrazenih)==0:
		listaTrazenih=pretraga.p_pretragaNamestaj()

	recnik,sifra=pretraga.p_pretragaSifra(listaTrazenih)

	while not bool(recnik):
		print("Pogresna sifra proizvoda koji zelite da dodate u korpu")
		recnik,sifra=pretraga.p_pretragaSifra(listaTrazenih)

	kolicina=unosEntiteta.unosKolicina()

	if recnik["kolicina"]<kolicina:
		print("Komada namestaja:",recnik["naziv"],"nema u trazenoj kolicini, mozete prodati najvise",recnik["kolicina"])
		print("Da li zelite tu kolicinu:",recnik["kolicina"],"proizvoda:",recnik["naziv"])
		print("0 - Ne (vratite se nazad)")
		print("1 - Da (nastavite sa prodajom)")
	
		komanda=""
		while not (komanda==0 or komanda==1):
			try:
				komanda=int(input("unesite komandu:"))
			except ValueError:
				print("pogresan format komande probajte opet")

		if komanda==0:
			return None,None
		elif komanda==1:
			return recnik,sifra


	recnik["kolicina"]=kolicina
	return recnik,sifra


def napraviIzmeneNamestaja(sifra,recnik):
	listaRecnikaNamestaja=pretraga.pretragaUcitajNamestaj()
	for recnikuFajlu in listaRecnikaNamestaja:
		if recnikuFajlu["sifra"]==sifra:
			recnikuFajlu["kolicina"]=recnikuFajlu["kolicina"]-recnik["kolicina"]
			if recnikuFajlu["kolicina"]<=0:
				recnikuFajlu["obrisano"]="true"

	stringZaUpis=unosEntiteta.recnikToStringNamestaj(listaRecnikaNamestaja)
	unosEntiteta.upisiString(stringZaUpis,"namestaj.txt")




def prodajaDodajUslugu():
	listaTrazenih=pretraga.p_pretragaUsluga()
	while len(listaTrazenih)==0:
		listaTrazenih=pretraga.p_pretragaUsluga()

	uzmiNaziv=pretraga.uzmiNazivUsluge(listaTrazenih)
	proverenNaziv=unosEntiteta.proveriArgumentNaziv(uzmiNaziv)
	trazeniRecnik,index=unosEntiteta.utvrdiListuTrazenihiIndexUsluga(listaTrazenih,proverenNaziv)

	print("Unesite koliko KM ili Sati se usluga pruza")
	trazeniRecnik["kolicina"]=unosEntiteta.unosKolicina()

	return trazeniRecnik



def izdavanjeRacuna(brojRacuna,user,korpa):
	
	uCena=ukupnaCena(korpa)
	uplata=kupacPlatio(uCena)
	vreme=datetime.datetime.now()
	pdv=porez(korpa)
	print("===================================")
	print("          (Ime preduzeca)          ")
	print("        (adresa preduzeca)         ")
	print("             ( mesto )             ")
	print("PIB: 012345678                     ")
	print("IBFM: 01234567                     ")
	print("-----------------------------------")
	print("{0:^36}               ".format(brojRacuna))
	print("-----------------------------------")
	print("|      ime      |   cena   |  kol |")
	print("-----------------------------------")
	for recnik in korpa:
		print("|{0:^15}|{1:^10}|{2:^6}|".format(recnik["naziv"],str(float(recnik["cena"])), str(recnik["kolicina"])))
	print("-----------------------------------")
	print("PDV 20%: {0:^36}".format(pdv))
	print("-----------------------------------")
	print("Za uplatu: {0:^36}".format(float(uCena)))
	print("Uplaceno: {0:^36}".format(uplata))
	print("Povracaj: {0:^36}".format(float(uplata-uCena)))
	print("{0}.{1}.{2}-{3}:{4}".format(vreme.day,vreme.month,vreme.year,vreme.hour,vreme.minute))
	print("===================================")
	print("{0:<10} - {1:<10} {2:<15}".format(user[0],user[2],user[3]))

	RacunUFajl(brojRacuna,user,korpa,uCena,vreme,pdv)






def porez(korpa):
	return float(ukupnaCena(korpa)*20/100)

def kupacPlatio(uCena):

	uplata=""
	while True:
			try:
				uplata=int(input("Unesite koliko je kupac UPLATIO: "))
				if uplata<=0 or uplata<uCena:
					uplata=kupacPlatio()
				return uplata
			except ValueError:
				print("Pogresan format")



def RacunUFajl(brojRacuna,user,korpa,uCena,vreme,pdv):
#racun je opisan brRacuna|ime N1/n2/n2|kategorija n1/n2/n3/|jedCena n1/n2/n3|kol n1/n2/n3|porez|ukCena|d&t|username|ime|prezime|
	stringZaUpis=str(brojRacuna)

	nazivi=""
	kategorije=""
	jedCena=""
	kol=""
	for recnik in korpa:
		nazivi=nazivi+recnik["naziv"]+"/"
		try:
			kategorije=kategorije+recnik["kategorija"]+"/"
		except KeyError:
			kategorije=kategorije+"/"

		jedCena=jedCena+str(recnik["cena"])+"/"

		kol=kol+str(recnik["kolicina"])+"/"

	porez=str(pdv)

	ukupnaCena=str(uCena)

	strVreme=str(vreme.day)+"/"+str(vreme.month)+"/"+str(vreme.year)+"/"+str(vreme.hour)+"/"+str(vreme.minute)+"/" #promeni mozda nacin cuvanja datum i vreme



	stringZaUpis=stringZaUpis+"|"+nazivi+"|"+kategorije+"|"+jedCena+"|"+kol+"|"+porez+"|"+ukupnaCena+"|"+strVreme+"|"+user[0]+"/"+user[2]+"/"+user[3]+"|"+"false"+"|"+"\n"
	
	f=open("racuni.txt","a")
	f.write(stringZaUpis)
	f.close()



def proveraNamestajaUKorpi(recnik,korpa):
	for prodato in korpa:
		if prodato["sifra"]==recnik["sifra"]:
			prodato["kolicina"]=prodato["kolicina"]+recnik["kolicina"]
			return True #ako vec ima recnik samo promeni kolicinu u korpi 


def proveraUslugaUKorpi(recnik,korpa):
	for prodato in korpa:
		if prodato["naziv"]==recnik["naziv"]:
			prodato["kolicina"]=prodato["kolicina"]+recnik["kolicina"]
			return True #ako vec ima recnik samo promeni kolicinu u korpi 



#	kategorije=""
	# for recnik in korpa:
	# 	try:
	# 		kategorije=kategorije+recnik["kategorija"]+"/"
	# 	except KeyError:
	# 		kategorije=kategorije+"/"

	# jedCena=""
	# for recnik in korpa:
	# 	jedCena=jedCena+recnik["cena"]+"/"


	# kol=""
	# for recnik in korpa:
	# 	kol=kol+recnik["kolicina"]+"/"






	# 1. pitaj za termine pretrage
	# 2. odmah posle kazi unesi sifru onog koji zelis da uzmes
	# 3. uradis pretragu po sifri i ovde vratis taj recnik koji ti treba



#sta odabere dodaje namestaj u racun 


#prodaja namestaja ukucas naziv(termine) i posle dodaj po sifri(kao bar kod) i onda se vraca vamo i doda ga u ovaj prozor i pita opet hoces dodavati nesto



#dodavanje usluga ce isto po imenu biti ali je ono jedinstveno stoga nema probema




#kad stisne 3 onda na konzoli ispise racun koji izgledati jedino da ispise sve sta treba da bude tu, sacuva racun namestaja i da ima racun usluga posebno 
#kod racuna da unese koliko je korisnik dao i koliko kusura treba da se vrati (ako stignem)
#tek nakon izdavanja racuna se sredi njihova kolicina

#verovatno cu uraditi sve posebno ovde, pretraga po sifri, ucitavanje, pisanej i sve sve vezano za racun ce biti ovde necu mesati sa onim kodom

#generisanje racuna na terminal, pisanje u fajl, oduzimanje sa namestaja, provera da li ima dovoljno kolicinski




#svaki put kad se doda nesto doda se na tabelu i iz nje imas potvrdu da je pordaja zavrsena (on uzima pare i pise sve u fajlove)

#razmisljam da imam 2 racuna 1 za namestaj 2 za usluge 



#racun treba da je opisen sve iz specifikacije + username (jer je on jedinstven)


#kad hocu da prodajem 1. pretragu uradim po imenu, pitam za sifru prozivoda, vidim da li ima dovoljna kolicina 

#moram uneti kolicini za usluge u recniku i tu ce mi biti koliko kilometara/sati se radi, ona ne sme biti 0

#kad dodajem vise istih namestaja/usluga pitam jel ima vec sifra/naziv u korpi ako ima samo dodaj novu kolicinu na onu u korpi

#je sada jedinstven i namestaj sa istom sifrom ne mozes da iams vise puta 