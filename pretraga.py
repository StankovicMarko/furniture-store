#pretraga.py
import unosEntiteta
import datetime


def pretragaKolicine():
	listaRecnikaNamestaja=pretragaUcitajNamestaj()
	donja,gornja=pretragaUcitajKolicine()

	listaTrazenih=[]
	for recnik in listaRecnikaNamestaja:
		if (recnik["kolicina"]>=donja and recnik["kolicina"]<=gornja and recnik["obrisano"]=="false"):
			listaTrazenih.append(recnik)

	sortirajPoKolicini(listaTrazenih)
	pretragaIspisNamestaja(listaTrazenih)


def pretragaUcitajKolicine():
	print("Unesite donju granicu cene")
	donja=unosEntiteta.unosKolicina()
	print("Unesite gornju granicu cene")
	gornja=unosEntiteta.unosKolicina()

	return donja,gornja

def sortirajPoKolicini(listaTrazenih):
	listaTrazenih.sort(key=lambda x: x["kolicina"])


def pretragaOpsegCene(): #promeni ime funkcije u pretragaNamestajOpsegCene
	listaRecnikaNamestaja=pretragaUcitajNamestaj()
	donja,gornja=pretragaUcitajOpsegCene()

	listaTrazenih=[]
	for recnik in listaRecnikaNamestaja:
		if (recnik["cena"]>=donja and recnik["cena"]<=gornja and recnik["obrisano"]=="false"):
			listaTrazenih.append(recnik)

	sortirajPoCeni(listaTrazenih)
	pretragaIspisNamestaja(listaTrazenih)


def pretragaUcitajOpsegCene():
	print("Unesite donju granicu cene")
	donja=unosEntiteta.unosCena()
	print("Unesite gornju granicu cene")
	gornja=unosEntiteta.unosCena()

	return donja,gornja

#sifra ili ima tacno ta ili si pogresno uneo sifru 
def pretragaSifra():
	listaRecnikaNamestaja=pretragaUcitajNamestaj()
	sifra=pretragaUcitajSifru()

	listaTrazenih=[]
	for recnik in listaRecnikaNamestaja:
		if (recnik["sifra"]==sifra and recnik["obrisano"]=="false"):
			listaTrazenih.append(recnik)
			pretragaIspisNamestaja(listaTrazenih) #skratice broj koraka pretrage cim ga nadje (posto su sifre jedinstvene) odmah ce da izadje iz ovoga
			return
	print("Proizvod nepostoji ili je obrisan")
	return


def pretragaUcitajSifru():
	while True:
		try:
			sifra=int(input("unesite sifru proizvoda: "))
			return sifra
		except ValueError:
			print("pogresan format unosa, unesite broj")


def proveriFajl(imeFajla):
	while True:
		try:
			f=open(imeFajla,"r")
			f.close()
			return
		except FileNotFoundError:
			f=open(imeFajla,"w")
			f.close()


def namestajStrToDict(vrednosti):
	recnik={}
	recnik["sifra"]=int(vrednosti[0])
	recnik["naziv"]=vrednosti[1]
	recnik["boja"]=vrednosti[2]
	recnik["kolicina"]=int(vrednosti[3])
	recnik["cena"]=int(vrednosti[4])
	recnik["kategorija"]=vrednosti[5]
	recnik["obrisano"]=vrednosti[6]
	return recnik

def pretragaUcitajNamestaj():
	proveriFajl("namestaj.txt")

	f=open("namestaj.txt","r")
	linije=f.readlines()
	f.close()

	return napraviListuRecNamestaja(linije)

def napraviListuRecNamestaja(linije):
	listaRecnika=[]
	for linija in linije:
		vrednosti=linija.strip().split("|")
		recnik=namestajStrToDict(vrednosti)
		listaRecnika.append(recnik)
	
	return listaRecnika



def pretragaUcitajTermine():
	termini=""
	while termini=="":
		termini=input("unesite termine pretrage: ")

	listaTermina=termini.lower().split(" ")

	return list(set(listaTermina))

def pretragaNaziv():
	listaRecnikaNamestaja=pretragaUcitajNamestaj()
	listaTermina=pretragaUcitajTermine() #implemtancija kao na google bla bla blu, split, for i in a, if a in s, ceo red pravi recni i stavljaj u listu inace nastavi
	listaTrazenih=pretragaSelekcija(listaRecnikaNamestaja,listaTermina)

	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisNamestaja(listaTrazenih)

	sifraNamestaja=uzmiSifruNamestaja(listaTrazenih)
	pretragaOpcijeNamestaj(sifraNamestaja)

#mogu da saljem i kljuc i u zavisnosti od njega mogu da iskoristim funkcije 
def pretragaSelekcija(listaRecnikaNamestaja,listaTermina):
	listaTrazenih=[]
	for recnik in listaRecnikaNamestaja:
		for termin in listaTermina:
			if (termin in recnik["naziv"] and recnik["obrisano"]=="false"):
				if not (recnik in listaTrazenih):
					listaTrazenih.append(recnik)
	return listaTrazenih

	# pretragaSortirajPoNazivu(listaTrazenih)
	# pretragaIspisNamestaja(listaTrazenih)
	# sifraNamestaja=uzmiSifruNamestaja(listaTrazenih)
	# pretragaOpcijeNamestaj(sifraNamestaja)

def pretragaSortirajPoNazivu(listaTrazenih):
	listaTrazenih.sort(key=lambda x: x["naziv"])
	

def pretragaIspisNamestaja(listaTrazenih): 
#posle 1 000 000 000 artikala sifra vise nije tacna tada cemo uraditi update software-a ili jednostavno dodati UI i u njemu implementirati ovo
#cene preko 9 999 999 999
	print("------------------------------------------------------------------------")
	print("|  sifra   |     naziv     |     boja      | kol |   cena   |  kateg   |")
	print("------------------------------------------------------------------------")
	for recnik in listaTrazenih:
		print("|{0:^10}|{1:^15}|{2:^15}|{3:^5}|{4:^10}|{5:^10}|".format(str(recnik["sifra"])[:10],recnik["naziv"][:15],recnik["boja"][:15],str(recnik["kolicina"])[:5],str(recnik["cena"])[:10],recnik["kategorija"][:10]))


	#ima opcija da saljem da je iz pretrage sifara i tu sifru da iskoristi za izmenu/brisanje
	#i druga opcija je ako je len(listaTrazenih) == 1 onda u pretraguOpcije posalji sifru i nju iskoristi za dalje 
	

	
	#ovo saljes kao arugment u izmeni/brisanju ce pitati ako je taj parametar none = zovi pretargu po sifri inace iskoristi tu sifru sto si dobio
#ovde stajem sutra NASTAVLJAM 

	# sifraNamestaja=uzmiSifruNamestaja(listaTrazenih) #prakticno gle da li je pretraga dosla iz pretrage sifara ili ne, odnosno da li pretraga bila jedinstvena ili ne
	# pretragaOpcijeNamestaj(sifraNamestaja)

def uzmiSifruNamestaja(listaTrazenih):
	if len(listaTrazenih) == 1:
		return listaTrazenih[0]["sifra"]
	else:
		return None

def pretragaOpcijeMenuNamestaj():
	print("da li zelite da: ")
	print("0 - Idite nazad")
	print("1 - izmenite proizvod")
	print("2 - obrisete proizvod")
	print("3 - (niste nasli proizvod?) Pretrazi Obrisane")

def pretragaOpcijeNamestaj(sifraNamestaja):
	pretragaOpcijeMenuNamestaj()

	komanda="komanda"

	while not uslovPretragaOpcijeNamestaj(komanda):
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	
	if komanda==0:
		return
	elif komanda==1:
		unosEntiteta.izmenaNamestaja(sifraNamestaja) #ovde cu slati sifru tog proizvoda koji sam pretrazio
	elif komanda==2:
		unosEntiteta.brisanjeNamestaja(sifraNamestaja)#takodje i ovde saljes sifru
	elif komanda==3:
		pretragaObrisanihNamestaja()

def uslovPretragaOpcijeNamestaj(komanda):
    return komanda==0 or komanda==1 or komanda==2 or komanda==3


def pretragaNamestajMenu():
	print("\nNalazite se na mainMenu/pretragaGrananje/pretragaNamestajaGrananje")
	print("Dobro dosli u pretragu podataka, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Pretraga po nazivu namestaja")
	print("2 - Pretraga po opsegu cene")
	print("3 - Pretraga po raspolozivoj kolicini")
	print("4 - Pretraga po sifri namestaja")

def pretragaKomandaUslov(komanda):
	return komanda==0 or komanda==1 or komanda==2 or komanda==3 or komanda==4

def pretragaNamestajaKomanda():
	komanda="komanda"

	while not pretragaKomandaUslov(komanda):
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	return komanda

def pretragaNamestajGrananje():
	while True:
		pretragaNamestajMenu()
		komanda=pretragaNamestajaKomanda() 
		if komanda==0:
			print("Povratak u prethodni menu")
			break
		elif komanda==1:
			print('Izabrali ste "Pretraga po nazivu namestaja"')
			pretragaNaziv()
		elif komanda==2:
			print('Izabrali ste "Pretraga po opsegu cene"')
			pretragaOpsegCene()
		elif komanda==3:
			print('Izabrali ste "Pretraga po raspolozivoj kolicini"')
			pretragaKolicine()
		elif komanda==4:
			print('Izabrali ste "Pretraga po sifri namestaja"')
			pretragaSifra()
			


def pretragaMenu():
	print("\nNalazite se na mainMenu/pretragaGrananje")
	print("Dobro dosli u pretragu podataka, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Pretraga namestaja")
	print("2 - Pretraga usluga salona")
	print("3 - Pretraga racuna")
	print("4 - Pretraga kategorija(po naziv)")
	print("5 - Pretraga korisnika")
	print("6 - Pretraga obrisanih entiteta")
	

def pretragaUslov(komanda):
	return komanda==0 or komanda==1 or komanda==2 or komanda==3 or komanda==4 or komanda==5 or komanda==6

def pretragaKomanda():
	komanda="komanda"

	while not pretragaUslov(komanda):
			try:
				komanda=int(input("Unesite komandu: "))
			except ValueError:
				print("Pogresan format komande, unesite broj sa menija")
	return komanda

def pretragaGrananje():
	while True:
		pretragaMenu()
		komanda=pretragaKomanda()
		if komanda==0:
			print("Povratak u prethodni menu")
			return
		elif komanda==1:
			print('Izabrali ste "Pretraga namestaja"')
			pretragaNamestajGrananje()
		elif komanda==2:
			print('Izabrali ste "Pretraga usluga salona"')
			pretragaUslugaGrananje()
		elif komanda==3:
			print('Izabrali ste "Pretraga racuna"')
			pretragaRacunaGrananje()
		elif komanda==4:
			print('Izabrali ste "Pretraga kategorija"')
			pretragaKategorija()
		elif komanda==5:
			print('Izabrali ste "Pretraga korisnika"')
			pretragaKorisnikaGrananje()
		elif komanda==6:
			print('Izabrali ste "Pretraga obrisanih entiteta"')
			pretragaObrisanihGrananje()

	############ gore je pretraga namestaja


	################   dole ce biti pretraga usluga salona



def pretragaUslugaGrananje():
	pretragaUslugaGrananjeMenu()
	komanda=pretragaUslugaKomanda()
	if komanda==0:
		print("Povratak u prethodni menu")
		return
	elif komanda==1:
		print('Izabrali ste "Pretraga usluga po nazivu"')
		pretragaUslugaNaziv()
	elif komanda==2:
		print('Izabrali ste "Pretraga usluga po opsegu cene"')
		pretragaUslugaOpsegCene()



def pretragaUslugaGrananjeMenu():
	print("\nNalazite se na mainMenu/pretragaGrananje/pretragaUslugaGrananje")
	print("Dobro dosli u pretragu usluga, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Pretraga usluga po nazivu")
	print("2 - Pretraga usluga opsegu cene")

def pretragaUslugaKomanda():
	komanda="komanda"

	while not pretragaUslugaUslov(komanda):
			try:
				komanda=int(input("Unesite komandu: "))
			except ValueError:
				print("Pogresan format komande, unesite broj sa menija")
	return komanda

def pretragaUslugaUslov(komanda):
	return komanda==0 or komanda==1 or komanda==2


def pretragaUslugaNaziv():
	proveriFajl("usluge.txt")

	listaTermina=pretragaUcitajTermine()
	listaRecnika=napraviListuRecUsluga()

	listaTrazenih=[]
	for recnik in listaRecnika:
		for termin in listaTermina:
			if (termin in recnik["naziv"] and recnik["obrisano"]=="false"):
				if not(recnik in listaTrazenih):
					listaTrazenih.append(recnik)

	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisUsluga(listaTrazenih)
	nazivUsluge=uzmiNazivUsluge(listaTrazenih) #prakticno gle da li je pretraga dosla iz pretrage sifara ili ne 
	pretragaOpcijeUsluge(nazivUsluge)


def napraviListuRecUsluga():
	f=open("usluge.txt")
	linije=f.readlines()
	f.close()

	listaRecnika=[]
	for linija in linije:
		vrednosti=linija.strip("\n").split("|")
		recnik=napraviRecUsluga(vrednosti)
		listaRecnika.append(recnik)

	return listaRecnika

def napraviRecUsluga(vrednosti):
	recnik={}
	recnik["naziv"]=vrednosti[0]
	recnik["opis"]=vrednosti[1]
	recnik["cena"]=int(vrednosti[2])
	recnik["obrisano"]=vrednosti[3]

	return recnik


def pretragaIspisUsluga(listaTrazenih):
	print("--------------------------------------------")
	print("|     naziv     |     opis      |   cena   |")
	print("--------------------------------------------")
	for recnik in listaTrazenih:
		print("|{0:^15}|{1:^15}|{2:^10}|".format(recnik["naziv"][:15],recnik["opis"][:15],str(recnik["cena"])[:10]))

	# nazivUsluge=uzmiNazivUsluge(listaTrazenih) #prakticno gle da li je pretraga dosla iz pretrage sifara ili ne 
	# pretragaOpcijeUsluge(nazivUsluge)

def uzmiNazivUsluge(listaTrazenih):
	if len(listaTrazenih) == 1:
		return listaTrazenih[0]["naziv"]
	else:
		return None

def pretragaOpcijeUsluge(nazivUsluge):
	pretragaOpcijeMenuNamestaj()

	komanda="komanda"
 
	while not uslovPretragaOpcijeNamestaj(komanda):#koristim funkciju ovde od gore
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	
	if komanda==0:
		return
	elif komanda==1:
		unosEntiteta.izmenaUsluga(nazivUsluge) #ovde cu slati naziv usluge
	elif komanda==2:
		unosEntiteta.brisanjeUsluga(nazivUsluge)#takodje i ovde saljes naziv, kada kliknem izmenu/brisanje proizvoda na UBIentitete ce traziti naziv usluge 
		#kao parametar, ako je slucajno dobio parametar vec radi posao
	elif komanda==3:
		pretragaObrisanihUsluga()


def pretragaUslugaOpsegCene():
	listaRecnikaUsluga=napraviListuRecUsluga()
	donja,gornja=pretragaUcitajOpsegCene()

	listaTrazenih=[]
	for recnik in listaRecnikaUsluga:
		if (recnik["cena"]>=donja and recnik["cena"]<=gornja and recnik["obrisano"]=="false"):
			listaTrazenih.append(recnik)


	sortirajPoCeni(listaTrazenih)
	pretragaIspisUsluga(listaTrazenih)

def sortirajPoCeni(listaTrazenih):
	listaTrazenih.sort(key=lambda x: x["cena"])



##### gore je pretraga usluga po nazivu i ceni

#pretraga kategorija po nazivu samo implemetujem i to je to, uradio bih kao naziv za namestaj
def pretragaKategorija():
	proveriFajl("kategorije.txt")

	listaTermina=pretragaUcitajTermine()
	listaRecnika=napraviListuRecKategorija()

	listaTrazenih=[]
	for recnik in listaRecnika:
		for termin in listaTermina:
			if (termin in recnik["naziv"] and recnik["obrisano"]=="false"):
				if not(recnik in listaTrazenih):
					listaTrazenih.append(recnik)

	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisKategorija(listaTrazenih)


def napraviListuRecKategorija():
	f=open("kategorije.txt")
	linije=f.readlines()
	f.close()

	listaRecnika=[]
	for linija in linije:
		vrednosti=linija.strip("\n").split("|")
		recnik=napraviRecKategorija(vrednosti)
		listaRecnika.append(recnik)

	return listaRecnika

def napraviRecKategorija(vrednosti):
	recnik={}
	recnik["naziv"]=vrednosti[0]
	recnik["opis"]=vrednosti[1]
	recnik["obrisano"]=vrednosti[2]

	return recnik


def pretragaIspisKategorija(listaTrazenih):
	print("---------------------------------")
	print("|     naziv     |     opis      |")
	print("---------------------------------")
	for recnik in listaTrazenih:
		print("|{0:^15}|{1:^15}|".format(recnik["naziv"][:15],recnik["opis"][:15]))

	nazivKategorije=uzmiNazivUsluge(listaTrazenih) #koristim funkciju da uzme naziv i prosledi ga izmeni 
	pretragaOpcijeKategorije(nazivKategorije)


def pretragaOpcijeKategorije(nazivKategorije):
	pretragaOpcijeMenuNamestaj() #koristim funkciju koja je vec napisana

	komanda="komanda"
 
	while not uslovPretragaOpcijeNamestaj(komanda):#koristim funkciju ovde od gore
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	
	if komanda==0:
		return
	elif komanda==1:
		unosEntiteta.izmenaKategorija(nazivKategorije) #ovde cu slati naziv usluge
	elif komanda==2:
		unosEntiteta.brisanjeKategorija(nazivKategorije)#takodje i ovde saljes naziv, kada kliknem izmenu/brisanje proizvoda na UBIentitete ce traziti naziv usluge 
		#kao parametar, ako je slucajno dobio parametar vec radi posao
	elif komanda==3:
		pretragaObrisanihKategorija()



# pretraga korisnka
def pretragaKorisnikaGrananje():
	while True:
		pretragaKorisnikaMenu()
		komanda=pretragaKomanda() #ovde budi paznjiv jer koristis funkciju koja za uslov ima 5 a tebi treba 4 pa gledaj da tu ne bude problem
		if komanda==0:
			print("Povratak u prethodni menu")
			break
		elif komanda==1:
			print('Izabrali ste "Pretraga po Username-u korisnika"')
			pretragaUsername()
		elif komanda==2:
			print('Izabrali ste "Pretraga Imenu korisnika"')
			pretragaIme()
		elif komanda==3:
			print('Izabrali ste "Pretraga Prezimenu korisnika"')
			pretragaPrezime()
		elif komanda==4:
			print('Izabrali ste "Pretraga po ulozi korisnika"')
			pretragaUloga()


def pretragaKorisnikaMenu():
	print("\nNalazite se na mainMenu/pretragaGrananje/pretragaKorisnikaGrananje")
	print("Dobro dosli u pretragu korisnika, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Pretraga po Username-u korisnika")
	print("2 - Pretraga Imenu korisnika")
	print("3 - Pretraga Prezimenu korisnika")
	print("4 - Pretraga po ulozi korisnika")

def pretragaUsername():
	listaRecnikaKorisnika=pretragaUcitajKorisnike()
	username=unosEntiteta.installUsername()

	listaTrazenih=[]
	for recnik in listaRecnikaKorisnika:
		if (recnik["username"]==username and recnik["obrisano"]=="false"):
			listaTrazenih.append(recnik)

	pretragaIspisKorisnika(listaTrazenih)

def pretragaUcitajKorisnike():
	proveriFajl("korisnici.txt")
	f=open("korisnici.txt","r")
	linije=f.readlines()
	f.close()
	listaRecnika=[]
	for linija in linije:
		vrednosti=linija.strip("\n").split("|")
		recnik=napraviRecKorisnika(vrednosti)
		listaRecnika.append(recnik)

	return listaRecnika

def napraviRecKorisnika(vrednosti):
	recnik={}
	recnik["username"]=vrednosti[0]
	recnik["password"]=vrednosti[1]
	recnik["ime"]=vrednosti[2]
	recnik["prezime"]=vrednosti[3]
	recnik["uloga"]=vrednosti[4]
	recnik["obrisano"]=vrednosti[5]

	return recnik

def pretragaIspisKorisnika(listaTrazenih):
	print("--------------------------------------------------------------------------")
	print("|   username    |    password   |     ime      |    prezime    |  uloga  |")
	print("--------------------------------------------------------------------------")
	for recnik in listaTrazenih:
		print("|{0:^15}|{1:^15}|{2:^14}|{3:^15}|{4:^9}|".format(recnik["username"][:15],recnik["password"][:15],recnik["ime"][:14],recnik["prezime"][:15],recnik["uloga"][:9]))


	username=uzmiUsername(listaTrazenih) 
	pretragaOpcijeKorisnika(username)

def uzmiUsername(listaTrazenih):
	if len(listaTrazenih) == 1:
		return listaTrazenih[0]["username"]
	else:
		return None

def pretragaOpcijeKorisnika(username):
	pretragaOpcijeMenuKorisnika()  #promeni ovo napravi novi meni za korisnike i gore za usluge, od sada svaka stvar ima svoj meni

	komanda="komanda"

	while not uslovPretragaOpcijeNamestaj(komanda):
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	
	if komanda==0:
		return
	elif komanda==1:
		unosEntiteta.izmenaKorisnika(username)
	elif komanda==2:
		unosEntiteta.brisanjeKorisnika(username)
	elif komanda==3:
		pretragaObrisanihKorisnika()

def pretragaOpcijeMenuKorisnika():
	print("Da li zelite da: ")
	print("0 - Idite nazad")
	print("1 - Izmenite korisnika")
	print("2 - Obrisete korisnika")
	print("3 - (niste nasli korisnika?) Pretrazi brisane korisnike")


def pretragaIme():
	proveriFajl("korisnici.txt")

	listaTermina=pretragaUcitajTermine()
	listaRecnika=pretragaUcitajKorisnike()

	listaTrazenih=[]
	for recnik in listaRecnika:
		for termin in listaTermina:
			if (termin in recnik["ime"] and recnik["obrisano"]=="false"):
				if not(recnik in listaTrazenih):
					listaTrazenih.append(recnik)

	pretragaSortirajPoImenu(listaTrazenih)
	pretragaIspisKorisnika(listaTrazenih)

def pretragaSortirajPoImenu(listaTrazenih):
	listaTrazenih.sort(key=lambda x: x["ime"])


def pretragaPrezime():
	proveriFajl("korisnici.txt")

	listaTermina=pretragaUcitajTermine()
	listaRecnika=pretragaUcitajKorisnike()

	listaTrazenih=[]
	for recnik in listaRecnika:
		for termin in listaTermina:
			if (termin in recnik["prezime"] and recnik["obrisano"]=="false"):
				if not(recnik in listaTrazenih):
					listaTrazenih.append(recnik)

	pretragaSortirajPoPrezimenu(listaTrazenih)
	pretragaIspisKorisnika(listaTrazenih)

def pretragaSortirajPoPrezimenu(listaTrazenih):
	listaTrazenih.sort(key=lambda x: x["prezime"])


def pretragaUloga():
	listaRecnikaKorisnika=pretragaUcitajKorisnike()
	uloga=unosEntiteta.unosUloga()

	listaTrazenih=[]
	for recnik in listaRecnikaKorisnika:
		if recnik["uloga"]==uloga and recnik["obrisano"]=="false":
			listaTrazenih.append(recnik)


	pretragaIspisKorisnika(listaTrazenih)



#pretrage racuna
#pretraga obrisanih racuna ako budem imao vremena







def pretragaObrisanihGrananje():
	while True:
		pretragaObrisanihGrananjeMenu()
		komanda=pretragaObrisanihNamestajaKomanda() 
		if komanda==0:
			print("Povratak u prethodni menu")
			break
		elif komanda==1:
			print('Izabrali ste "Pretraga obrisanih namestaja"')
			pretragaObrisanihNamestaja()
		elif komanda==2:
			print('Izabrali ste "Pretraga obrisanih usluga"')
			pretragaObrisanihUsluga()
		elif komanda==3:
			print('Izabrali ste "Pretraga obrisanih korisnika"')
			pretragaObrisanihKorisnika()
		elif komanda==4:
			print('Izabrali ste "Pretraga obrisanih kategorija"')
			pretragaObrisanihKategorija()

def pretragaObrisanihGrananjeMenu():
	print("\nNalazite se na mainMenu/pretragaGrananje/pretragaObrisanihGrananje")
	print("Dobro dosli u pretragu obrisanih podataka, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Pretraga obrisanih namestaja(po nazivu)")
	print("2 - Pretraga obrisanih usluga(po nazivu)")
	print("3 - Pretraga obrisanih korisnika(prezimenu i ulozi)")
	print("4 - Pretraga obrisanih kategorija(po nazivu)")


def pretragaObrisanihNamestajaKomanda():
	komanda="komanda"

	while not pretragaKomandaUslov(komanda): #gore imas funkckiju gleda da li je tacno 0,1,2,3,4
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	return komanda


#pretraga obrisanih samo obrisane da mi nadje i sifru da bih vratio u zivot
#namestaj po nazivu i kategoriji



def pretragaObrisanihNamestaja():
	listaRecnikaNamestaja=pretragaUcitajNamestaj()
	listaTermina=pretragaUcitajTermine()
	listaTrazenih=[]
	for recnik in listaRecnikaNamestaja:
		for termin in listaTermina:
			if (termin in recnik["naziv"] and recnik["obrisano"]=="true"):
				if not(recnik in listaTrazenih):
					listaTrazenih.append(recnik)

	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisObrisanihNamestaja(listaTrazenih)


def pretragaIspisObrisanihNamestaja(listaTrazenih):
	print("------------------------------------------------------------------------")
	print("|  sifra   |     naziv     |     boja      | kol |   cena   |  kateg   |")
	print("------------------------------------------------------------------------")
	for recnik in listaTrazenih:
		print("|{0:^10}|{1:^15}|{2:^15}|{3:^5}|{4:^10}|{5:^10}|".format(str(recnik["sifra"])[:10],recnik["naziv"][:15],recnik["boja"][:15],str(recnik["kolicina"])[:5],str(recnik["cena"])[:10],recnik["kategorija"][:10]))

	
	sifraNamestaja=uzmiSifruNamestaja(listaTrazenih) #prakticno gle da li je pretraga dosla iz pretrage sifara ili ne 
	pretragaOpcijeObrisanihNamestaja(sifraNamestaja)


def pretragaOpcijeObrisanihNamestaja(sifraNamestaja):
	pretragaOpcijeMenuObrisanihNamestaja()

	komanda="komanda"

	while not uslovPretragaOpcijeObrisanihNamestaja(komanda):
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	
	if komanda==0:
		return
	elif komanda==1:
		unosEntiteta.restoreNamestaja(sifraNamestaja) #ovde cu slati sifru tog proizvoda koji sam pretrazio


def pretragaOpcijeMenuObrisanihNamestaja():
	print("da li zelite da: ")
	print("0 - Idite nazad")
	print("1 - Vratite proizvod (uradite restore)")

def uslovPretragaOpcijeObrisanihNamestaja(komanda):
    return komanda==0 or komanda==1


#usluge po nazivu

def pretragaObrisanihUsluga():
	proveriFajl("usluge.txt")

	listaTermina=pretragaUcitajTermine()
	listaRecnika=napraviListuRecUsluga()

	listaTrazenih=[]
	for recnik in listaRecnika:
		for termin in listaTermina:
			if (termin in recnik["naziv"] and recnik["obrisano"]=="true"):
				if not(recnik in listaTrazenih):
					listaTrazenih.append(recnik)

	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisObrisanihUsluga(listaTrazenih)

def pretragaIspisObrisanihUsluga(listaTrazenih):
	print("--------------------------------------------")
	print("|     naziv     |     opis      |   cena   |")
	print("--------------------------------------------")
	for recnik in listaTrazenih:
		print("|{0:^15}|{1:^15}|{2:^10}|".format(recnik["naziv"][:15],recnik["opis"][:15],str(recnik["cena"])[:10]))

	nazivUsluge=uzmiNazivUsluge(listaTrazenih) #prakticno gle da li je pretraga dosla iz pretrage sifara ili ne 
	pretragaOpcijeObrisanihUsluga(nazivUsluge)

def uzmiNazivUsluge(listaTrazenih):
	if len(listaTrazenih) == 1:
		return listaTrazenih[0]["naziv"]
	else:
		return None

def pretragaOpcijeObrisanihUsluga(nazivUsluge):
	pretragaOpcijeMenuObrisanihUsluga()

	komanda="komanda"
 
	while not uslovPretragaOpcijeObrisanihNamestaja(komanda):#koristim funkciju ovde od gore mora biti 0,1
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	
	if komanda==0:
		return
	elif komanda==1:
		unosEntiteta.restoreUsluga(nazivUsluge) #ovde cu slati naziv usluge

def pretragaOpcijeMenuObrisanihUsluga():
	print("da li zelite da: ")
	print("0 - Idite nazad")
	print("1 - Vratite uslugu (uradite restore)")

#korisnici po Prezimenu i ulozi zajedno kao uslov i da mi izbaci 

#kada u pretrazi zoves (nije prikazan, pretrazi obrisane) tu sredi pozive funkcija

def pretragaObrisanihKorisnika():
	proveriFajl("korisnici.txt")

	listaTermina=pretragaUcitajTermine() #prezime
	uloga=unosEntiteta.unosUloga()
	listaRecnika=pretragaUcitajKorisnike()

	listaTrazenih=[]
	for recnik in listaRecnika:
		for termin in listaTermina:
			if (termin in recnik["prezime"] and recnik["uloga"]==uloga and recnik["obrisano"]=="true"):
				if not(recnik in listaTrazenih):
					listaTrazenih.append(recnik)

	pretragaSortirajPoPrezimenu(listaTrazenih)
	pretragaIspisObrisanihKorisnika(listaTrazenih)

def pretragaIspisObrisanihKorisnika(listaTrazenih):
	print("--------------------------------------------------------------------------")
	print("|   username    |    password   |     ime      |    prezime    |  uloga  |")
	print("--------------------------------------------------------------------------")
	for recnik in listaTrazenih:
		print("|{0:^15}|{1:^15}|{2:^14}|{3:^15}|{4:^9}|".format(recnik["username"][:15],recnik["password"][:15],recnik["ime"][:14],recnik["prezime"][:15],recnik["uloga"][:9]))

	username=uzmiUsername(listaTrazenih) 
	pretragaOpcijeObrisanihKorisnika(username)


def pretragaOpcijeObrisanihKorisnika(username):
	pretragaOpcijeMenuObrisanihKorisnika()  #promeni ovo napravi novi meni za korisnike i gore za usluge, od sada svaka stvar ima svoj meni

	komanda="komanda"

	while not uslovPretragaOpcijeObrisanihNamestaja(komanda):
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	
	if komanda==0:
		return
	elif komanda==1:
		unosEntiteta.restoreKorisnika(username)

def pretragaOpcijeMenuObrisanihKorisnika():
	print("Da li zelite da: ")
	print("0 - Idite nazad")
	print("1 - Vratite korisnika (uradite restore)")


#kategorije po nazivu

def pretragaObrisanihKategorija():
	proveriFajl("kategorije.txt")

	listaTermina=pretragaUcitajTermine()
	listaRecnika=napraviListuRecKategorija()

	listaTrazenih=[]
	for recnik in listaRecnika:
		for termin in listaTermina:
			if (termin in recnik["naziv"] and recnik["obrisano"]=="true"):
				if not(recnik in listaTrazenih):
					listaTrazenih.append(recnik)

	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisObrisanihKategorija(listaTrazenih)

def pretragaIspisObrisanihKategorija(listaTrazenih):
	print("---------------------------------")
	print("|     naziv     |     opis      |")
	print("---------------------------------")
	for recnik in listaTrazenih:
		print("|{0:^15}|{1:^15}|".format(recnik["naziv"][:15],recnik["opis"][:15]))

	nazivKategorije=uzmiNazivUsluge(listaTrazenih) #koristim funkciju da uzme naziv i prosledi ga izmeni 
	pretragaOpcijeObrisanihKategorija(nazivKategorije)


def pretragaOpcijeObrisanihKategorija(nazivKategorije):
	pretragaOpcijeMenuObrisanihKategorija() #koristim funkciju koja je vec napisana

	komanda="komanda"

	while not uslovPretragaOpcijeObrisanihNamestaja(komanda):#koristim funkciju ovde od gore
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	
	if komanda==0:
		return
	elif komanda==1:
		unosEntiteta.restoreKategorija(nazivKategorije) 


def pretragaOpcijeMenuObrisanihKategorija():
	print("Da li zelite da: ")
	print("0 - Idite nazad")
	print("1 - Vratite kategoriju (uradite restore)")



#mozda da impelemtujes da kad obrises kategoriju obrise sve namestaje sa tom kategorijom al to je samo ideja





##############pretraga prodavac

def p_pretragaGrananje():
	while True:
		p_pretragaGrananjeMenu()
		komanda=p_pretragaKomanda()
		if komanda==0:
			print("Povratak u prethodni menu")
			return
		elif komanda==1:
			print('Izabrali ste "Pretraga namestaja po nazivu"')
			p_pretragaNamestaj()
		elif komanda==2:
			print('Izabrali ste "Pretraga namestaja po kategorijama"')
			p_pretragaNamestajKategorija()
		elif komanda==3:
			print('Izabrali ste "Pretraga usluga salona"')
			p_pretragaUsluga()

def p_pretragaGrananjeMenu():
	print("\nNalazite se na mainMenu/p_pretragaGrananje")
	print("Dobro dosli u pretragu podataka, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Pretraga namestaja po nazivu")
	print("2 - Pretraga namestaja po kategorijama")
	print("3 - Pretraga usluga salona")

def p_pretragaKomanda():
	komanda="komanda"

	while not p_pretragaKomandaUslov(komanda):
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	return komanda

def p_pretragaKomandaUslov(komanda):
	return komanda==0 or komanda==1 or komanda==2 or komanda==3

def p_pretragaNamestaj(): #po nazivu
	listaRecnikaNamestaja=pretragaUcitajNamestaj()
	listaTermina=pretragaUcitajTermine()
	listaTrazenih=pretragaSelekcija(listaRecnikaNamestaja,listaTermina)
	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisNamestaja(listaTrazenih)
	return listaTrazenih


def p_pretragaSifra(listaTrazenih):
	print("zavrsena je pretraga po nazivu, molimo unesite sifru proizvoda koji zelite da dodate u korpu")
	sifra=pretragaUcitajSifru()

	for recnik in listaTrazenih:
		if recnik["sifra"]==sifra:
			return recnik,sifra
	print("Pogresna sifra proizvoda")
	return None, None

def p_pretragaNamestajKategorija():
	listaRecnikaNamestaja=pretragaUcitajNamestaj()
	print("Unesite ime kategorije")
	listaTermina=pretragaUcitajTermine()

	listaTrazenih=pretragaSelekcijaKatName(listaRecnikaNamestaja,listaTermina)

	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisNamestaja(listaTrazenih)

def pretragaSelekcijaKatName(listaRecnikaNamestaja,listaTermina):
	listaTrazenih=[]
	for recnik in listaRecnikaNamestaja:
		for termin in listaTermina:
			if (termin in recnik["kategorija"] and recnik["obrisano"]=="false"):
				if not (recnik in listaTrazenih):
					listaTrazenih.append(recnik)
	return listaTrazenih


#pretraga usluga
def p_pretragaUsluga():
	proveriFajl("usluge.txt")
	listaTermina=pretragaUcitajTermine()
	listaRecnika=napraviListuRecUsluga()
	listaTrazenih=pretragaSelekcija(listaRecnika,listaTermina)
	
	pretragaSortirajPoNazivu(listaTrazenih)
	pretragaIspisUsluga(listaTrazenih)

	return listaTrazenih

# def p_pretragaNamestajUProdaji(listaRecnikaNamestajaProdaja):
# 	listaTermina=pretragaUcitajTermine() 
# 	listaTrazenih=pretragaSelekcija(listaRecnikaNamestajaProdaja,listaTermina)
# 	pretragaSortirajPoNazivu(listaTrazenih)
# 	pretragaIspisNamestaja(listaTrazenih)
# 	return listaTrazenih



####pretraga racuna 
#imacu pretragu racuna namestaja.########################################

def pretragaRacunaGrananje():
	while True:
		pretragaRacunaMenu()
		komanda=pretragaRacunaKomanda() 
		if komanda==0:
			print("Povratak u prethodni menu")
			return
		elif komanda==1:
			print('Izabrali ste "Pretraga racuna po broju racuna"')
			pretragaBrojRacuna()
		elif komanda==2:
			print('Izabrali ste "Pretraga racuna po nazivu namestaja"')
			pretragaNazivRacunaNamestaj()
		#elif komanda==3:
		#	print('Izabrali ste "Pretraga po nazivu usluga"')
			
		elif komanda==3:
			print('Izabrali ste "Pretraga racuna po datumu izdavanja"')
			pretragaDatumRacuna()
		elif komanda==4:
			print('Izabrali ste "Pretraga racuna po prodavcu koji ga je izdao"')
			pretragaProdavacRacun()


def pretragaRacunaMenu():
	print("\nNalazite se na mainMenu/pretragaGrananje/pretragaRacunaGrananje")
	print("Dobro dosli u pretragu racuna, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Pretraga racuna po broju racuna")
	print("2 - Pretraga racuna po nazivu namestaja/usluga")
#	print("3 - Pretraga racuna po nazivu usluga")
	print("3 - Pretraga racuna po datumu izdavanja")
	print("4 - Pretraga racuna po prodavcu koji ga je izdao")

def pretragaRacunaKomanda():
	komanda="komanda"

	while not pretragaRacunaKomandaUslov(komanda):
		try:
			komanda=int(input("Unesite komandu: "))
		except ValueError:
			print("Pogresan format komande, unesite broj sa menija")
	return komanda

def pretragaRacunaKomandaUslov(komanda):
	return komanda==0 or komanda==1 or komanda==2 or komanda==3 or komanda==4


def pretragaBrojRacuna():
	brRacuna=pretragaUcitajBrRac()
	listaRecnikaRacuna=ucitajRecnikeRacuna()
	listaTrazenih=pretragaSelekcijaRacunaBrRac(listaRecnikaRacuna,brRacuna)
	ispisiRacun(listaTrazenih)


def pretragaUcitajBrRac():
	while True:
		try:
			brRacuna=int(input("unesite broj racuna: "))
			return brRacuna
		except ValueError:
			print("pogresan format unosa, unesite broj")


def ucitajRecnikeRacuna():
	proveriFajl("racuni.txt")

	f=open("racuni.txt","r")
	linije=f.readlines()
	f.close()

	listaRecnika=[]
	for linija in linije:
		vrednosti=linija.strip().split("|")
		recnik=racunStrToDict(vrednosti)
		listaRecnika.append(recnik)
	
	return listaRecnika

def racunStrToDict(vrednosti): #lista recnika koji sadrze recnike i kljucevi ce biti 0,1,2,3.. koji ce odgovarati cenama i kolicinama
	recnik={}

	recnik["brojRacuna"]=int(vrednosti[0])


	recnik["nazivi"]={}
	l_naziv=vrednosti[1].split("/")
	l_naziv=list(filter(None,l_naziv))
	i=0
	for naziv in l_naziv:
		recnik["nazivi"][i]=naziv
		i=i+1

	recnik["kategorije"]={}
	l_kategorija=vrednosti[2].split("/")
	i=0
	for kategorija in l_kategorija:
		recnik["kategorije"][i]=kategorija
		i=i+1


	recnik["cene"]={}
	cene=vrednosti[3].split("/")
	cene=list(filter(None,cene))
	cene=[int(i) for i in cene]
	i=0
	for cena in cene:
		recnik["cene"][i]=cena
		i=i+1

	
	recnik["kolicine"]={}
	kolicine=vrednosti[4].split("/")
	kolicine=list(filter(None,kolicine))
	i=0
	for kolicina in kolicine:
		recnik["kolicine"][i]=kolicina
		i=i+1
	

	recnik["pdv"]=float(vrednosti[5])

	recnik["ukupnaCena"]=int(vrednosti[6])

	recnik["vreme"]={}
	vreme=vrednosti[7].split("/")
	vreme=list(filter(None,vreme))
	vreme=[int(i) for i in vreme]
	recnik["vreme"]["dan"]=vreme[0]
	recnik["vreme"]["mesec"]=vreme[1]
	recnik["vreme"]["godina"]=vreme[2]
	recnik["vreme"]["sat"]=vreme[3]
	recnik["vreme"]["minut"]=vreme[4]

	recnik["prodavac"]={}
	prodavac=vrednosti[8].split("/")
	#prodavac=list(filter(None,prodavac))
	recnik["prodavac"]["username"]=prodavac[0]
	recnik["prodavac"]["ime"]=prodavac[1]
	recnik["prodavac"]["prezime"]=prodavac[2]

	recnik["obrisano"]=vrednosti[9]

	return recnik


def pretragaSelekcijaRacunaBrRac(listaRecnikaRacuna,brRacuna):
	listaTrazenih=[]
	for recnik in listaRecnikaRacuna:
		if (brRacuna==recnik["brojRacuna"] and recnik["obrisano"]=="false"):
			listaTrazenih.append(recnik)
			return listaTrazenih

def ispisiRacun(listaRecnikaRacuna):
	for recnik in listaRecnikaRacuna:
		print("===================================")
		print("          (Ime preduzeca)          ")
		print("        (adresa preduzeca)         ")
		print("             ( mesto )             ")
		print("PIB: 012345678                     ")
		print("IBFM: 01234567                     ")
		print("-----------------------------------")
		print("{0:^36}               ".format(recnik["brojRacuna"]))
		print("-----------------------------------")
		print("|      ime      |   cena   |  kol |")
		print("-----------------------------------")
		#for recnik in listaRecnikaRacuna:
		for pozicija in recnik["nazivi"]:
			print("|{0:^15}|{1:^10}|{2:^6}|".format(recnik["nazivi"][pozicija],str(float(recnik["cene"][pozicija])), str(recnik["kolicine"][pozicija])))
		print("-----------------------------------")
		print("PDV 20%: {0:^36}".format(recnik["pdv"]))
		print("-----------------------------------")
		print("Za uplatu: {0:^36}".format(float(recnik["ukupnaCena"])))
		#print("Uplaceno: {0:^36}".format(uplata))
		#print("Povracaj: {0:^36}".format(float(uplata-uCena)))
		print("{0}.{1}.{2}-{3}:{4}".format(recnik["vreme"]["dan"],recnik["vreme"]["mesec"],recnik["vreme"]["godina"],recnik["vreme"]["sat"],recnik["vreme"]["minut"]))
		print("===================================")
		print("{0:<10} - {1:<10} {2:<15}".format(recnik["prodavac"]["username"],recnik["prodavac"]["ime"],recnik["prodavac"]["prezime"]))




def pretragaNazivRacunaNamestaj():
	listaTermina=pretragaUcitajTermine()
	listaRecnikaRacuna=ucitajRecnikeRacuna()
	listaTrazenih=pretragaSelekcijaRacunaNaziv(listaRecnikaRacuna,listaTermina)

	ispisiRacun(listaTrazenih)	



def pretragaSelekcijaRacunaNaziv(listaRecnikaRacuna,listaTermina):
	listaTrazenih=[]
	for recnik in listaRecnikaRacuna:
		for termin in listaTermina:
			for index in recnik["nazivi"]:
				if (termin in recnik["nazivi"][index] and recnik["obrisano"]=="false"):
					listaTrazenih.append(recnik)
				if recnik in listaTrazenih:
					break
			if recnik in listaTrazenih:
					break
	return listaTrazenih


def pretragaDatumRacuna():
	print("Unesite pocetno vreme")
	datum1=unesiDatum()
	print("Unesite krajnje vreme")
	datum2=unesiDatum()
	listaRecnikaRacuna=ucitajRecnikeRacuna()
	listaTrazenih=pretragaSelekcijaRacunaDatum(listaRecnikaRacuna,datum1,datum2)

	ispisiRacun(listaTrazenih)	#vidi recimo da ovde radis ret listaTrazenih, pa da mozes da iskoristis


def unesiDatum():
	while True:
		try:
			day=int(input("unesite dan: "))
			month=int(input("unesite mesec: "))
			year=int(input("unesite godinu: "))
		except ValueError:
			continue

		try:
			datum=datetime.date(year,month,day)
			return datum
		except ValueError:
			print("Pogresan format datuma, molimo unesite dobar format")

def pretragaSelekcijaRacunaDatum(listaRecnikaRacuna,datum1,datum2):

	listaTrazenih=[]
	for recnik in listaRecnikaRacuna:
		datumRecnika=datetime.date(recnik["vreme"]["godina"],recnik["vreme"]["mesec"],recnik["vreme"]["dan"])
		if (datumRecnika>=datum1 and datumRecnika<=datum2 and recnik["obrisano"]=="false"):
			listaTrazenih.append(recnik)

	return listaTrazenih


def pretragaProdavacRacun():
	listaRecnikaRacuna=ucitajRecnikeRacuna()
	ime=unosEntiteta.installIme()
	prezime=unosEntiteta.installPrezime()
	listaTrazenih=pretragaSelekcijaRacunaProdavac(listaRecnikaRacuna,ime,prezime)

	ispisiRacun(listaTrazenih)


def pretragaSelekcijaRacunaProdavac(listaRecnikaRacuna,ime,prezime):

	listaTrazenih=[]
	for recnik in listaRecnikaRacuna:
		if (recnik["prodavac"]["ime"]==ime and recnik["prodavac"]["prezime"]==prezime and recnik["obrisano"]=="false"):
			listaTrazenih.append(recnik)

	return listaTrazenih


	# 1. uzecu sifru
	# 2. ucitacu racune, napraviti listu recnika 
	# 3. uporediti 
	# 4. ispisati

	#prezentacije 1 za programere 2 za preduzetnike. programerima pricam kako sam napravio, uml diagrami, logika itd..
#preduztnicima pricam performase programa, lakoca koriscenja sto je dobro jer ce obuka manje trajati, mogucnosti stvaranja izvestaja sto rasteecuje 
#racunovodstvo, kompletno pracenje i cuvanje podataka koji su potrebni za vodjenje posla, lak za odrzavanje i sa mogucnoscu dodavanja stvari koje obavlja
#koko bi mu prosirila primena i olaksalo, ubrzalo poslovanje. naravno ovo bi se moglo doterati malo kada bi se graficki interfejs dodao i on ce izgledati 
#otprilike ovako (pa pokazem neki nadrkan interfejs)
#storniranje racuna
#dodatak za informacioni sistem koji pokriva magacin(ulaz,izlaz,popis) koji u slucaju da je proizvod trazen cim padne kolicina ispod odredjene odmah salje izvesta
#da je potrebno naruciti, storno racuna koji vraca sve podatke sa tog racuna gde bi trbali, popis...
#u prezentaciji napomenem da nam je sifra bar kod i da bi smo mogli napraviti implementaciju skenirana bar koda



#napravim slajd kako je program testiran na obicnim ljudima koji nemaju veze sa namestajem i podelim njihove utiske dzonijeva, mladenova, vukasova, raticeva slika
#aleksandrina napisem u oblacicu njihove utiske o programu, njihovu sturcnu spremu (kod djomle napisem klosar), kazem da ce imati besplatno odrzavanje prvih 
#mesec dana i besplatna 2 casa oko uvoda o koriscenju aplikacije


#moram da skontam izmenu i brisanje. 
#jedan od nacina je ako hocu da izmenim prvo ukucam pretragu po cemu hocu da trazim termine kada nadje svi oni koji imaju te termine(u opseg cene..)
#bivaju izmenjeni tako sto cu uneti kako zelim da mi izgleda to ucitati ceo fajl ici kroz njega dok ne nadjem podudaranje i onda izmeniti i to vratiti u fajl

#jako mi je haoticno hocu i da kad menadzer uradi pretragu da ima opciju da izmeni fail ili obrise, tako da kad klikne tamo na izmenu odluka je vec donesena
#i odradim pretragu samo navodi sta hoce da izmeni. 

#i to je problem jer ako imam 10 ikea i kliknem izmenu sta tacno ce on menjati? svaki od njih redom? 
#ili da implementiram pretraga otprilike i imas opciju za brisanje izmenu samo kada je jedan fajl napisan? 
#ako i masovne izmene ucitam fajl uporedim sa rezultatima pretrage kad nadje poklapanje kazem napravite izmene za taj i taj sacuvaj,izmeni nazad(preskocice taj)
#ili mogu da kad kazem izmenu a vise razultata u pretrazi on da napravi novu listu sa novim recnicima u kojima se nalaze izmene i za svaki pitam sacuvaj,
#izmena ili nazad(taj ostaje isti) i onda ceo fajl ucitam, poredim sa pretragom nadjem isto, zameni sa adekvatnom izmenom 1-1,2-2... i to je to

#pretraga je oke ali ako je prazna pitaj hoces da pretrazis obrisane i onda cu ista pretraga samo bez uslova za true i jedna opcija ce biti izmeni (koja ce)
#automatski da uradi restore stavice true na false ili samo restore (inverz brisana)



#recnik ce iz fajla da pretvori u int,float sta ima a kad pisem to pretvoricu ga nazad u string jer mogu da ga isecem

#hocu da kad trazis proizvode da ti ponudi da izmenis ili obrises proizvod ako ga trazis po sifri i sad kontam da imam promenjivu koja kaze dolazim iz pretragaSifre
#i u ispisu pitam jel to True ako jeste ponudi 0 nazad, 1 izmeni, 2 izbrisi

#kad budem radio izmenu/brisanje pitacu za sifru ili uradi pretragu pa trazi po imenu, trazi sifru dobije opciju izmene i brisanja i onda odradi posao

#sad se lomimi dobar nacin je i da napravis pretragu imas ponudjenu opciju i kad uzmes pita te da unses sifru proizvoda koji hoces da izmenis/obrises
#ovo je mozda cak i bolje. jer mozes da izmenis, obrises samo 1 a opet deluje fino i zaobilazi celu pricu oko moras pretragu po necemu pa moras po sifri pa
#tek onda imas opciju da menjas

#u pretrazi ces da imas i opciju da potrazis obrisane ali to samo menadzer
#znaci meni ce biti
# 0 - nazad
# 1- izmeni
# 2 - obrisi
#3 4 - (niste nasli proizvod?) pretrazite obrisane 

#sad je zanimljivo kad kazes izmeni i on trazi sifru (radice pretragu po sifri) imam utisak da ce se zapetljati ako iz pretrage po sifri budem trazio izmenu
#tu bi trebao da stavim da ako je pretraga po sifri da tu sifru salje u izmenu tako da ce tamo moci da se ucita ceo fajl nadje ta sifra i startuje izmena iz
#modula UBI u kojoj ces moci da sacuvas izmenu, izmenis izmenu, vratis se nazad

########### ima dosta funkcija koje kad bi se malo uredile mogle bi se koristi ponovo kao npr pretraga kolicine, cene rastavim to i koristim vise puta
###########istu stvar