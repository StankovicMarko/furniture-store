import pretraga

def upisKorisnika(username,password,ime,prezime,uloga):
    string=(username+"|"+password+"|"+ime+"|"+prezime+"|"+uloga+"|"+"false"+"|"+"\n").lower()
    f = open("korisnici.txt", "a")
    f.write(string)
    f.close()

def installUsername():
    username="naziv"
    while True:
        try:
            username=input("Unesite username korisnika: ")
            if username=="":
                username=installUsername()
            username=int(username)
            print("pogresan format username-a")
        except ValueError:
            return username



def installPassword():
    while True:
            password=input("Unesite password korisnika: ")
            if password=="":
                password=installPassword()
            return password


def uslovInstallIme(ime):
    return any(ch.isdigit() for ch in ime) 

def installIme():
    ime="1"

    while uslovInstallIme(ime):
        ime=input("unesite ime korisnika: ")

    if ime=="":
        ime=installIme()

    return ime

def uslovInstallPrezime(prezime):
    return any(ch.isdigit() for ch in prezime) 

def installPrezime():
    prezime="1"

    while uslovInstallPrezime(prezime):
        prezime=input("unesite unesite prezime korisnika: ")

    if prezime=="":
        prezime=installPrezime()

    return prezime

def proveraUsername(username):
    pretraga.proveriFajl("korisnici.txt")

    f=open("korisnici.txt","r")
    linije=f.readlines()
    f.close()

    for linija in linije:
        l_linija=linija.split("|")
        if l_linija[0]==username:
            print("ovaj username vec postoji, morate uneti novi")
            return True
    return False

def installKorisnik():
    username=installUsername()
    if proveraUsername(username):
        return
    password=installPassword()
    ime=installIme()
    prezime=installPrezime()
    uloga=unosUloga()

    installKorisnikProveraPodataka(username,password,ime,prezime,uloga)

def unosUloga():
    uloga=input("unesite ulogu korisnika(prodavac,menadzer)")
    while not (uloga=="prodavac" or uloga=="menadzer"):
        print("niste uneli ulogu korisnika u dobrom formatu, unesite ponovo")
        uloga=input("unesite ulogu korisnika(prodavac,menadzer)")
    return uloga


def uslovInstallKorisnikProveraPodataka(komanda):
    return komanda==0 or komanda==1 or komanda==2

def installKorisnikProveraPodataka(username,password,ime,prezime,uloga):
    print("podaci su: \nusername: {0},\npassword: {1},\nime: {2},\nprezime: {3},\nuloga: {4}.\n".format(username,password,ime,prezime,uloga))
    komanda=""
    while not uslovUnosNamestajaProveraPodataka(komanda):
        try:
            komanda=int(input("\n0 - vratite se nazad,\n1 - zelim da sacuvam podatke,\n2 - zelim da napravim izmene(pogresio sam pri unosu):\n"))
        except ValueError:
            print("pogresan format komande probajte opet")
        
    if komanda==1:
        upisKorisnika(username,password,ime,prezime,uloga)
    elif komanda==2:
        installKorisnik()
    else:
        return

def uslovInstall(komanda):
    return komanda==0 or komanda==1

def unesiInstallKomandu():
    komanda="komanda"

    while not uslovInstall(komanda):
        try:
            komanda=int(input("Unesite komandu: "))
        except ValueError:
            print("Pogresan format komande, unesite broj sa menija")
    return komanda

def installMenu():
    print("Dobro dosli u instalaciju aplikacije")
    print("Unesite komande sta zelite da uradite")
    print("1 - Unos korisnika aplikacije")
    print("0 - Izlaz")

def installGrananje():
    korisnikUnet=False

    while True:
        installMenu()
        komanda = unesiInstallKomandu()
        if komanda==1:
            print("Izabrali ste unos korisnika")
            installKorisnik()
            korisnikUnet=True
        elif komanda==0:
            if korisnikUnet==False:
                print("Niste dobro instalirali aplikaciju, molimo vas pokusajte ponovo")
                exit()
            else:
                print("zavrsen je unos Korisnika u sistem, zelimo vam prijatan dan.")
                break

def install():
    try:
        f=open("korisnici.txt","r")
        f.close()
        return
    except FileNotFoundError:
        print("Molimo vas instalirajte aplikaciju")
        installGrananje()

def unosUpisNamestaja(sifra,naziv,boja,kolicina,cena,kategorija):
    linija=str(sifra)+"|"+naziv+"|"+boja+"|"+str(kolicina)+"|"+str(cena)+"|"+kategorija+"|"+"False"+"|"+"\n"
    linija=linija.lower()
    f=open("namestaj.txt", "a")
    f.write(linija)
    f.close()
   

def uslovUnosNamestajaProveraPodataka(komanda):
    return komanda==0 or komanda==1 or komanda == 2


def unosNamestajaProveraPodataka(sifra,naziv,boja,kolicina,cena,kategorija):
    print("podaci su: \nsifra: {0},\nnaziv: {1},\nboja: {2},\nkolicina: {3},\ncena: {4},\nkategorija: {5}.".format(sifra,naziv,boja,kolicina,cena,kategorija))
    komanda=""
    while not uslovUnosNamestajaProveraPodataka(komanda):
        try:
            komanda=int(input("\n0 - vratite se nazad,\n1 - zelim da sacuvam podatke,\n2 - zelim da napravim izmene(pogresio sam pri unosu):\n"))
        except ValueError:
            print("pogresan format komande probajte opet")
        
    if komanda==1:
        if proveraKategorija(kategorija)==False:
            print("Ova kategorija namestaja ne postoji")
            unosNoveKategorije(kategorija)
        unosUpisNamestaja(sifra,naziv,boja,kolicina,cena,kategorija)
    elif komanda==2:
        unosNamestaja()
    elif komanda==0:
        return
    

    
def utvrdiSifruNamestaja():
    while True:
        try: 
            f=open("namestaj.txt","r")
            linije=f.readlines()
            f.close()
            return len(linije)
        except FileNotFoundError:
              f=open("namestaj.txt","w")
              f.close()  
        

#uzme imput, pokusa da konvetuje u int ako ne moze vrati taj naziv. ovo je dobro jer u imenu mozemo imati i brojeve ali ne mozemo imati same brojeve
def unosNaziv():
    naziv="naziv"
    while True:
        try:
            naziv=input("Unesite naziv: ")
            if naziv=="":
                naziv=unosNaziv()
            naziv=int(naziv)
            print("pogresan format naziva")
        except ValueError:
            return naziv

def unosBoja():
    boja=""
    while True:
        try:
            boja=input("Unesite boju: ")
            if boja=="":
                boja=unosBoja()
            boja=int(boja)
            print("pogresan format boje")
        except ValueError:
            return boja

def unosKolicina():
    kol=""
    while True:
        try:
            kol=int(input("Unesite kolicina: "))
            if kol<=0:
                kol=unosKolicina()
            return kol
        except ValueError:
            print("pogresan format kolicine")


def unosCena():
    cena=""
    while True:
        try:
            cena=int(input("Unesite cena: "))
            if cena<=0:
                cena=unosCena()
            return cena
        except ValueError:
            print("pogresan format cena")

def proveraKategorija(kategorija):
    pretraga.proveriFajl("kategorije.txt")
    # while True:
    #     try:
    f=open("kategorije.txt","r")
    linije=f.readlines()
    f.close()
    for linija in linije:
        l_linija=linija.split("|")
        if l_linija[0]==kategorija:
           
            return True
    return False

 
def uslovUnosOpisKategorije(opis):
    return any(ch.isdigit() for ch in opis) 

def unosOpisKategorije():
    opis="1"   

    while uslovUnosOpisKategorije(opis): #iskoristio sam funkciju za istu stvar pita da li je string
        opis=input("Unesite opis nove kategorije: ")

    if opis=="":
        opis=unosOpisKategorije()

    return opis

def unosNoveKategorije(kategorija):
    opis=unosOpisKategorije()
    f=open("kategorije.txt","a")
    f.write((kategorija+"|"+opis+"|"+"False"+"|"+"\n").lower())
    f.close()

def uslovUnosKategorija(kategorija):
    return any(ch.isdigit() for ch in kategorija) 

def unosKategorija():
    kategorija="1"   


    while uslovUnosKategorija(kategorija):
        kategorija=input("unesite naziv kategorije: ")

    if kategorija=="":
        kategorija=unosKategorija()

    return kategorija

    

def unosNamestaja():
    print("mainMenu/unosGrananje/unosNamestaja")
    sifra=utvrdiSifruNamestaja()
    naziv=unosNaziv()

    boja=unosBoja()
    kolicina=unosKolicina()
    cena=unosCena()	
    kategorija=unosKategorija()

    unosNamestajaProveraPodataka(sifra,naziv,boja,kolicina,cena,kategorija)
    
   

#meni i grananje 
def unosMenu():
	print("\nNalazite se na mainMenu/unosGrananje")
	print("Dobro dosli u unos podataka, molimo Vas izaberite sta zelite")
	print("0 - Idite nazad")
	print("1 - Unos komada namestaja")
	print("2 - Unos korisnika")
	print("3 - Unos usluga salona")


#################################################### gore je unos namestaja
###################################sad ide unos usluga##########

def proveraNaziv(naziv):
    pretraga.proveriFajl("usluge.txt")

    f=open("usluge.txt", "r")
    linije=f.readlines()
    f.close()
    for linija in linije:
        l_linija=linija.split("|")
        if l_linija[0]==naziv:
            print("naziv ove usluge vec postoji(nazivi usluga su jedinstveni)")
            return True
    return False


def uslovNazivUsluge(naziv):
    return any(ch.isdigit() for ch in naziv)
    #for ch in naziv
    #   if ch.isdigit()
    #       return True
    #return False

def nazivUsluge():
    naziv="1"
    while uslovNazivUsluge(naziv):
        naziv=input("unesite ime usluge: ")

    if naziv=="":
        naziv=nazivUsluge()

    return naziv


#ova funkcija moze da zanemari i da se iskoristi unos cene gore
def cenaUsluge():
    cena=""
    while True:
        try:
            cena=int(input("Unesite cenu usluge: "))
            if cena<=0:
                cena=cenaUsluge()
            return cena
        except ValueError:
            print("pogresan format cene")

def uslovUnosProveraPodatakaUsluge(komanda):
    return komanda==0 or komanda==1 or komanda == 2

def unosProveraPodatakaUsluge(naziv,opis,cena):
    print("podaci su: \nnaziv: {0},\nopis: {1},\ncena: {2}\n".format(naziv,opis,cena,))
    komanda=""
    while not uslovUnosProveraPodatakaUsluge(komanda):
        try:
            komanda=int(input("\n0 - vratite se nazad,\n1 - zelim da sacuvam podatke,\n2 - zelim da napravim izmene(pogresio sam pri unosu):\n"))
        except ValueError:
            print("pogresan format komande probajte opet")
        
    if komanda==1:
        unosUpisUsluga(naziv,opis,cena)
    elif komanda==2:
        unosUsluga()
    else:
        return

def unosUpisUsluga(naziv,opis,cena):
    string=(naziv+"|"+opis+"|"+str(cena)+"|"+"False"+"|"+"\n").lower()
    f=open("usluge.txt","a")
    f.write(string)
    f.close()


def uslovUnosOpisUsluge(opis):
    return any(ch.isdigit() for ch in opis) 

def unosOpisUsluge():
    opis="1"   

    while uslovUnosOpisUsluge(opis): 
        opis=input("unesite opis usluge: ")

    if opis=="":
        opis=unosOpisUsluge()

    return opis

def unosUsluga():
    print("mainMenu/unosGrananje/unosUsluga")
    naziv=nazivUsluge()
    if proveraNaziv(naziv):
        return

    opis=unosOpisUsluge()
    cena=cenaUsluge()

    unosProveraPodatakaUsluge(naziv,opis,cena)


def unosUslov(komanda):
    return komanda==0 or komanda==1 or komanda==2 or komanda==3

def unosKomanda():
    komanda="komanda"

    while not unosUslov(komanda):
        try:
            komanda=int(input("Unesite komandu: "))
        except ValueError:
            print("Pogresan format komande, unesite broj sa menija")
    return komanda



def unosGrananje():

    while True:
        unosMenu()
        komanda=unosKomanda()
        if komanda==0:
            print("Povratak u prethodni menu")
            break
        elif komanda==1:
            print('Izabrali ste "Unos komada namestaja"')
            unosNamestaja()
        elif komanda==2:
            print('Izabrali ste "Unos korisnika"')
            installKorisnik() 
        elif komanda==3:
            print('Izabrali ste "Unos usluga salona"')
            unosUsluga()



##########  Izmene




def izmenaGrananje():
    while True:
        izmenaMenu()
        komanda=pretraga.pretragaNamestajaKomanda()
        if komanda==0:
            print("Povratak u prethodni menu")
            return
        elif komanda==1:
            print('Izabrali ste "Izmena namestaja"')
            izmenaNamestaja(None)
            #proba(None)
        elif komanda==2:
            print('Izabrali ste "Izmena usluga"')
            izmenaUsluga(None)
        elif komanda==3:
            print('Izabrali ste "Izmena korisnika"')
            izmenaKorisnika(None)
        elif komanda==4:
            print('Izabrali ste "Izmena kategorija"')
            izmenaKategorija(None)            

def izmenaMenu():
    print("\nNalazite se na mainMenu/izmenaGrananje")
    print("Dobro dosli u izmenu podataka, molimo Vas izaberite sta zelite")
    print("0 - Idite nazad")
    print("1 - Izmena namestaja")
    print("2 - Izmena usluga")
    print("3 - Izmena korisnika")
    print("4 - Izmena kategorija")





#izmena namestaja (probacu binarnu pretragu)

def izmenaNamestaja(sifraNamestaja):
    sifra=proveriArgumentSifra(sifraNamestaja)
    listaRecnikaNamestaja=pretraga.pretragaUcitajNamestaj()
    trazeniRecnik,index=utvrdiListuTrazenihiIndexNamestaj(listaRecnikaNamestaja,sifra)
    if index==None:
        print("Proizvod nepostoji ili je obrisan")
        return
    prikaziNamestaj(trazeniRecnik)

    noviRecnik=izmenjenRecnikNamestaj(sifra)
    print("izmenjen proizvod izgleda ovako")
    prikaziNamestaj(noviRecnik)

    izmenaNamestajaProveraPodataka(noviRecnik,index,listaRecnikaNamestaja)


#pita da je None(odnosno radili smo pretragu i imali smo vise rezultata i zelimo neki da izmenimo stoga pitamo za sifru jer je ona jedinstvena)
#ako nije none koristicemo sifruNamestaja sasvim normalno u pronalazenju naseg namestaja i menjaju istog
def proveriArgumentSifra(sifraNamestaja):
    if sifraNamestaja==None:
        return pretraga.pretragaUcitajSifru()
    else:
        return sifraNamestaja


def utvrdiListuTrazenihiIndexNamestaj(listaRecnikaNamestaja,sifra):
    index=0
    trazeniRecnik={}
    for recnik in listaRecnikaNamestaja:
        if (recnik["sifra"]==sifra and recnik["obrisano"]=="false"):
            trazeniRecnik=recnik
            return trazeniRecnik, index 
        index=index+1
    return trazeniRecnik, None #proizvod je obrisan ili nepostoji
    



def prikaziNamestaj(recnik):
    print("------------------------------------------------------------------------")
    print("|  sifra   |     naziv     |     boja      | kol |   cena   |  kateg   |")
    print("------------------------------------------------------------------------")
    print("|{0:^10}|{1:^15}|{2:^15}|{3:^5}|{4:^10}|{5:^10}|".format(str(recnik["sifra"])[:10],recnik["naziv"][:15],recnik["boja"][:15],str(recnik["kolicina"])[:5],str(recnik["cena"])[:10],recnik["kategorija"][:10]))



def izmenjenRecnikNamestaj(sifra):
    print("Unesite podatke koje zelite da promenite")
    recnik={}
    recnik["sifra"]=sifra
    recnik["naziv"]=unosNaziv()
    recnik["boja"]=unosBoja()
    recnik["kolicina"]=unosKolicina()
    recnik["cena"]=unosCena()
    recnik["kategorija"]=unosKategorija()
    recnik["obrisano"]="false"
    return recnik


def izmenaNamestajaProveraPodataka(noviRecnik,index,listaRecnikaNamestaja):
    komanda=""
    while not uslovUnosNamestajaProveraPodataka(komanda):
        try:
            komanda=int(input("\n0 - vratite se nazad,\n1 - zelim da sacuvam podatke,\n2 - zelim da napravim izmene(pogresio sam pri unosu):\n"))
        except ValueError:
            print("pogresan format komande probajte opet")
        
    if komanda==1:
        if proveraKategorija(noviRecnik["kategorija"])==False:
            print("Ova kategorija namestaja ne postoji")
            unosNoveKategorije(noviRecnik["kategorija"])
        izmenaUnosNamestaja(noviRecnik,index,listaRecnikaNamestaja)
    elif komanda==2:
        izmenaNamestaja(None)
    elif komanda==0:
        return

def izmenaUnosNamestaja(recnik,index,listaRecnikaNamestaja):
    sacuvajIzmeneNamestaja(recnik,index,listaRecnikaNamestaja)

    stringZaUpis=recnikToStringNamestaj(listaRecnikaNamestaja)

    upisiString(stringZaUpis,"namestaj.txt")

    # 1. recnik stavim u listu recnika
    # 2. idem redom i svaki recnik pretvorim u string koji je u novoj listi
    # 3. upisem 

def sacuvajIzmeneNamestaja(recnik,index,listaRecnikaNamestaja):
    listaRecnikaNamestaja[index]["sifra"]=recnik["sifra"]
    listaRecnikaNamestaja[index]["naziv"]=recnik["naziv"]
    listaRecnikaNamestaja[index]["boja"]=recnik["boja"]
    listaRecnikaNamestaja[index]["kolicina"]=recnik["kolicina"]
    listaRecnikaNamestaja[index]["cena"]=recnik["cena"]
    listaRecnikaNamestaja[index]["kategorija"]=recnik["kategorija"]
    listaRecnikaNamestaja[index]["obrisano"]="false"


def recnikToStringNamestaj(listaRecnikaNamestaja):
    stringZaUpis=""
    for recnik in listaRecnikaNamestaja:
        stringZaUpis=stringZaUpis+"|".join([str(recnik["sifra"]),recnik["naziv"],recnik["boja"],str(recnik["kolicina"]),str(recnik["cena"]),recnik["kategorija"],recnik["obrisano"],"\n"])
    return stringZaUpis

def upisiString(stringZaUpis,imeFajla):
    f=open(imeFajla,"w")
    f.write(stringZaUpis)
    f.close()




#izmena usluga

def izmenaUsluga(naziv):

    naziv=proveriArgumentNaziv(naziv)
    listaRecnikaUsluga=pretraga.napraviListuRecUsluga()

    trazeniRecnik,index=utvrdiListuTrazenihiIndexUsluga(listaRecnikaUsluga,naziv)
    if index==None:
        print("Usluga ne postoji ili je obrisana")
        return
    prikaziUslugu(trazeniRecnik)

    noviRecnik=izmenjenRecnikUsluga(naziv)
    print("izmenjen proizvod izgleda ovako")
    prikaziUslugu(noviRecnik)

    izmenaUslugaProveraPodataka(noviRecnik,index,listaRecnikaUsluga)

def proveriArgumentNaziv(naziv):
    if naziv==None:
        return nazivUsluge()
    else:
        return naziv

def utvrdiListuTrazenihiIndexUsluga(listaRecnikaUsluga,naziv):
    index=0
    trazeniRecnik={}
    for recnik in listaRecnikaUsluga:
        if (recnik["naziv"]==naziv and recnik["obrisano"]=="false"):
            trazeniRecnik=recnik
            return trazeniRecnik, index 
        index=index+1
    return trazeniRecnik, None    


def prikaziUslugu(trazeniRecnik):
    print("--------------------------------------------")
    print("|     naziv     |     opis      |   cena   |")
    print("--------------------------------------------")
    print("|{0:^15}|{1:^15}|{2:^10}|".format(trazeniRecnik["naziv"][:15],trazeniRecnik["opis"][:15],str(trazeniRecnik["cena"])[:10]))


def izmenjenRecnikUsluga(naziv):
    print("Unesite podatke koje zelite da promenite")
    recnik={}
    recnik["naziv"]=naziv
    recnik["opis"]=unosOpisUsluge()
    recnik["cena"]=unosCena()
    recnik["obrisano"]="false"
    return recnik

def izmenaUslugaProveraPodataka(noviRecnik,index,listaRecnikaUsluga):
    komanda=""
    while not uslovUnosNamestajaProveraPodataka(komanda):
        try:
            komanda=int(input("\n0 - vratite se nazad,\n1 - zelim da sacuvam podatke,\n2 - zelim da napravim izmene(pogresio sam pri unosu):\n"))
        except ValueError:
            print("pogresan format komande probajte opet")
        
    if komanda==1:
        izmenaUnosUsluga(noviRecnik,index,listaRecnikaUsluga)
    elif komanda==2:
        izmenaUsluga(None)
    elif komanda==0:
        return    

def izmenaUnosUsluga(noviRecnik,index,listaRecnikaUsluga):
    sacuvajIzmeneUsluga(noviRecnik,index,listaRecnikaUsluga)

    stringZaUpis=recnikToStringUsluga(listaRecnikaUsluga)

    upisiString(stringZaUpis,"usluge.txt")    


def sacuvajIzmeneUsluga(recnik,index,listaRecnikaUsluga):
    listaRecnikaUsluga[index]["naziv"]=recnik["naziv"]
    listaRecnikaUsluga[index]["opis"]=recnik["opis"]
    listaRecnikaUsluga[index]["cena"]=recnik["cena"]
    listaRecnikaUsluga[index]["obrisano"]="false"    


def recnikToStringUsluga(listaRecnikaUsluga):
    stringZaUpis=""
    for recnik in listaRecnikaUsluga:
        stringZaUpis=stringZaUpis+"|".join([recnik["naziv"],recnik["opis"],str(recnik["cena"]),recnik["obrisano"],"\n"])
    return stringZaUpis





# izmena korisnika 

def izmenaKorisnika(username):
    username=proveriArgumentUsername(username)
    listaRecnikaKorisnika=pretraga.pretragaUcitajKorisnike()

    trazeniRecnik,index=utvrdiListuTrazenihiIndexKorisnika(listaRecnikaKorisnika,username)
    if index==None:
        print("Korisnik ne postoji ili je obrisana")
        return
    prikaziKorisnika(trazeniRecnik)

    noviRecnik=izmenjenRecnikKorisnika(username)
    print("izmenjen proizvod izgleda ovako")
    prikaziKorisnika(noviRecnik)

    izmenaKorisnikaProveraPodataka(noviRecnik,index,listaRecnikaKorisnika)

def proveriArgumentUsername(username):
    if username==None:
        return installUsername()
    else:
        return username

def utvrdiListuTrazenihiIndexKorisnika(listaRecnikaKorisnika,username):
    index=0
    trazeniRecnik={}
    for recnik in listaRecnikaKorisnika:
        if (recnik["username"]==username and recnik["obrisano"]=="false"):
            trazeniRecnik=recnik
            return trazeniRecnik, index 
        index=index+1
    return trazeniRecnik, None    


def prikaziKorisnika(trazeniRecnik):
    print("--------------------------------------------------------------------------")
    print("|   username    |    password   |     ime      |    prezime    |  uloga  |")
    print("--------------------------------------------------------------------------")
    print("|{0:^15}|{1:^15}|{2:^14}|{3:^15}|{4:^9}|".format(trazeniRecnik["username"][:15],trazeniRecnik["password"][:15],trazeniRecnik["ime"][:14],trazeniRecnik["prezime"][:15],trazeniRecnik["uloga"][:9]))


def izmenjenRecnikKorisnika(username):
    print("Unesite podatke koje zelite da promenite")
    recnik={}
    recnik["username"]=username
    recnik["password"]=installPassword()
    recnik["ime"]=installIme()
    recnik["prezime"]=installPrezime()
    recnik["uloga"]=unosUloga()
    recnik["obrisano"]="false"
    return recnik

def izmenaKorisnikaProveraPodataka(noviRecnik,index,listaRecnikaKorisnika):
    komanda=""
    while not uslovUnosNamestajaProveraPodataka(komanda):
        try:
            komanda=int(input("\n0 - vratite se nazad,\n1 - zelim da sacuvam podatke,\n2 - zelim da napravim izmene(pogresio sam pri unosu):\n"))
        except ValueError:
            print("pogresan format komande probajte opet")
        
    if komanda==1:
        izmenaUnosKorisnika(noviRecnik,index,listaRecnikaKorisnika)
    elif komanda==2:
        izmenaKorisnika(None)
    elif komanda==0:
        return    

def izmenaUnosKorisnika(noviRecnik,index,listaRecnikaKorisnika):
    sacuvajIzmeneKorisnika(noviRecnik,index,listaRecnikaKorisnika)

    stringZaUpis=recnikToStringKorisnika(listaRecnikaKorisnika)

    upisiString(stringZaUpis,"korisnici.txt")    


def sacuvajIzmeneKorisnika(noviRecnik,index,listaRecnikaKorisnika):
    listaRecnikaKorisnika[index]["username"]=noviRecnik["username"]
    listaRecnikaKorisnika[index]["password"]=noviRecnik["password"]
    listaRecnikaKorisnika[index]["ime"]=noviRecnik["ime"]
    listaRecnikaKorisnika[index]["prezime"]=noviRecnik["prezime"]
    listaRecnikaKorisnika[index]["uloga"]=noviRecnik["uloga"]
    listaRecnikaKorisnika[index]["obrisano"]=noviRecnik["obrisano"]


def recnikToStringKorisnika(listaRecnikaKorisnika):
    stringZaUpis=""
    for recnik in listaRecnikaKorisnika:
        stringZaUpis=stringZaUpis+"|".join([recnik["username"],recnik["password"],recnik["ime"],recnik["prezime"],recnik["uloga"],recnik["obrisano"],"\n"])
    return stringZaUpis




#izmene kategorije


def izmenaKategorija(naziv):
    naziv=proveriArgumentNazivKategorija(naziv)
    listaRecnikaKategorija=pretraga.napraviListuRecKategorija()

    trazeniRecnik,index=utvrdiListuTrazenihiIndexKategorija(listaRecnikaKategorija,naziv)
    if index==None:
        print("Kategorija ne postoji ili je obrisana")
        return
    prikaziKategoriju(trazeniRecnik)

    noviRecnik=izmenjenRecnikKategorija(naziv)
    print("izmenjen proizvod izgleda ovako")
    prikaziKategoriju(noviRecnik)

    izmenaKategorijaProveraPodataka(noviRecnik,index,listaRecnikaKategorija)

def proveriArgumentNazivKategorija(naziv):
    if naziv==None:
        return unosKategorija()
    else:
        return naziv

def utvrdiListuTrazenihiIndexKategorija(listaRecnikaKategorija,naziv):
    index=0
    trazeniRecnik={}
    for recnik in listaRecnikaKategorija:
        if (recnik["naziv"]==naziv and recnik["obrisano"]=="false"):
            trazeniRecnik=recnik
            return trazeniRecnik, index 
        index=index+1
    return trazeniRecnik, None    


def prikaziKategoriju(trazeniRecnik):
    print("---------------------------------")
    print("|     naziv     |     opis      |")
    print("---------------------------------")
    print("|{0:^15}|{1:^15}|".format(trazeniRecnik["naziv"][:15],trazeniRecnik["opis"][:15]))


def izmenjenRecnikKategorija(naziv):
    print("Unesite podatke koje zelite da promenite")
    recnik={}
    recnik["naziv"]=naziv
    recnik["opis"]=unosOpisKategorije()
    recnik["obrisano"]="false"
    return recnik

def izmenaKategorijaProveraPodataka(noviRecnik,index,listaRecnikaKategorija):
    komanda=""
    while not uslovUnosNamestajaProveraPodataka(komanda):
        try:
            komanda=int(input("\n0 - vratite se nazad,\n1 - zelim da sacuvam podatke,\n2 - zelim da napravim izmene(pogresio sam pri unosu):\n"))
        except ValueError:
            print("pogresan format komande probajte opet")
        
    if komanda==1:
        izmenaUnosKategorija(noviRecnik,index,listaRecnikaKategorija)
    elif komanda==2:
        izmenaKategorija(None)
    elif komanda==0:
        return    

def izmenaUnosKategorija(noviRecnik,index,listaRecnikaKategorija):
    sacuvajIzmeneKategorija(noviRecnik,index,listaRecnikaKategorija)

    stringZaUpis=recnikToStringKategorija(listaRecnikaKategorija)

    upisiString(stringZaUpis,"kategorije.txt")    


def sacuvajIzmeneKategorija(noviRecnik,index,listaRecnikaKategorija):
    listaRecnikaKategorija[index]["naziv"]=noviRecnik["naziv"]
    listaRecnikaKategorija[index]["opis"]=noviRecnik["opis"]
    listaRecnikaKategorija[index]["obrisano"]="false"    


def recnikToStringKategorija(listaRecnikaKategorija):
    stringZaUpis=""
    for recnik in listaRecnikaKategorija:
        stringZaUpis=stringZaUpis+"|".join([recnik["naziv"],recnik["opis"],recnik["obrisano"],"\n"])
    return stringZaUpis



######### Brisanje


def brisanjeGrananje():
    while True:
        brisanjeMenu()
        komanda=pretraga.pretragaKomanda()
        if komanda==0:
            print("Povratak u prethodni menu")
            return
        elif komanda==1:
            print('Izabrali ste "Brisanje namestaja"')
            brisanjeNamestaja(None)
            #proba(None)
        elif komanda==2:
            print('Izabrali ste "Brisanje usluga"')
            brisanjeUsluga(None)
        elif komanda==3:
            print('Izabrali ste "Brisanje korisnika"')
            brisanjeKorisnika(None)
        elif komanda==4:
            print('Izabrali ste "Brisanje kategorija"')
            brisanjeKategorija(None)            

def brisanjeMenu():
    print("\nNalazite se na mainMenu/brisanjeGrananje")
    print("Dobro dosli u brisanje podataka, molimo Vas izaberite sta zelite")
    print("0 - Idite nazad")
    print("1 - Brisanje namestaja")
    print("2 - Brisanje usluga")
    print("3 - Brisanje korisnika")
    print("4 - Brisanje kategorija")




def brisanjeNamestaja(sifraNamestaja):
    sifra=proveriArgumentSifra(sifraNamestaja)
    listaRecnikaNamestaja=pretraga.pretragaUcitajNamestaj()

    for recnik in listaRecnikaNamestaja:
        if (recnik["sifra"]==sifra and recnik["obrisano"]=="false"):
            recnik["obrisano"]="true"
            print("Uspesno ste obrisali namestaj:",recnik["sifra"],recnik["naziv"])
            stringZaUpis=recnikToStringNamestaj(listaRecnikaNamestaja)
            upisiString(stringZaUpis,"namestaj.txt")
            return
    print("Ovaj komad namestaja ne postoji ili je vec obrisan")



def brisanjeUsluga(naziv):
    naziv=proveriArgumentNaziv(naziv)
    listaRecnikaUsluga=pretraga.napraviListuRecUsluga()

    for recnik in listaRecnikaUsluga:
        if (recnik["naziv"]==naziv and recnik["obrisano"]=="false"):
            recnik["obrisano"]="true"
            print("Uspesno ste obrisali uslugu:",recnik["naziv"])
            stringZaUpis=recnikToStringUsluga(listaRecnikaUsluga)
            upisiString(stringZaUpis,"usluge.txt")  
            return
    print("Ova usluga ne postoji ili je vec obrisana")


def brisanjeKorisnika(username):
    username=proveriArgumentUsername(username)
    listaRecnikaKorisnika=pretraga.pretragaUcitajKorisnike()

    for recnik in listaRecnikaKorisnika:
        if (recnik["username"]==username and recnik["obrisano"]=="false"):
            recnik["obrisano"]="true"
            print("Uspesno ste obrisali korisnika:",recnik["username"])
            stringZaUpis=recnikToStringKorisnika(listaRecnikaKorisnika)
            upisiString(stringZaUpis,"korisnici.txt")   
            return
    print("Ovaj korisnik ne postoji ili je vec obrisan")



def brisanjeKategorija(naziv):
    naziv=proveriArgumentNazivKategorija(naziv)
    listaRecnikaKategorija=pretraga.napraviListuRecKategorija()

    for recnik in listaRecnikaKategorija:
        if (recnik["naziv"]==naziv and recnik["obrisano"]=="false"):
            recnik["obrisano"]="true"
            print("Uspesno ste obrisali kategoriju:",recnik["naziv"])
            stringZaUpis=recnikToStringKategorija(listaRecnikaKategorija)
            upisiString(stringZaUpis,"kategorije.txt")
            return
    print("Ova kategorija ne postoji ili je vec obrisana")



#kad zovem pretrazi obrisane imacu opciju da se vratim nazad ili da restore uradim.
# a ovde dole su funckije koje rade bas to, vracaju obrisane

#funckije za restore, odnosno oni koji su obrisani da ih vratis


def restoreNamestaja(sifraNamestaja):
    sifra=proveriArgumentSifra(sifraNamestaja)
    listaRecnikaNamestaja=pretraga.pretragaUcitajNamestaj()

    for recnik in listaRecnikaNamestaja:
        if (recnik["sifra"]==sifra and recnik["obrisano"]=="true"):
            recnik["obrisano"]="false"
            print("Uspesno ste vratili obrisan namestaj")
            stringZaUpis=recnikToStringNamestaj(listaRecnikaNamestaja)
            upisiString(stringZaUpis,"namestaj.txt")
            return
    print("Ovaj komad namestaja ne postoji")



def restoreUsluga(naziv):
    naziv=proveriArgumentNaziv(naziv)
    listaRecnikaUsluga=pretraga.napraviListuRecUsluga()

    for recnik in listaRecnikaUsluga:
        if (recnik["naziv"]==naziv and recnik["obrisano"]=="true"):
            recnik["obrisano"]="false"
            print("Uspesno ste vratili obrisanu uslugu")
            stringZaUpis=recnikToStringUsluga(listaRecnikaUsluga)
            upisiString(stringZaUpis,"usluge.txt")  
            return
    print("Ova usluga ne postoji")


def restoreKorisnika(username):
    username=proveriArgumentUsername(username)
    listaRecnikaKorisnika=pretraga.pretragaUcitajKorisnike()

    for recnik in listaRecnikaKorisnika:
        if (recnik["username"]==username and recnik["obrisano"]=="true"):
            recnik["obrisano"]="false"
            print("Uspesno ste vratili obrisanog korisnika")
            stringZaUpis=recnikToStringKorisnika(listaRecnikaKorisnika)
            upisiString(stringZaUpis,"korisnici.txt")   
            return
    print("Ovaj korisnik ne postoji")



def restoreKategorija(naziv):
    naziv=proveriArgumentNazivKategorija(naziv)
    listaRecnikaKategorija=pretraga.napraviListuRecKategorija()

    for recnik in listaRecnikaKategorija:
        if (recnik["naziv"]==naziv and recnik["obrisano"]=="true"):
            recnik["obrisano"]="false"
            print("Uspesno ste vratili obrisanu kategoriju")
            stringZaUpis=recnikToStringKategorija(listaRecnikaKategorija)
            upisiString(stringZaUpis,"kategorije.txt")
            return
    print("Ova kategorija ne postoji")



# brisanje racuna(storniranje) to mozda uradim ako bude bilo vremena
#unos
#unos korisnika pozivam installKorisnik koji je u sklopu instalacije programa
#import instalacija #gledaj da ti instalacija bude u posebnom modulu i da importujes ovde i u project to i da koristis funkcije fino

#modul koji se koristi pri instalaciji ( ako nema fajla korisnika da se napravi i da se korisnici unesu, da bi mogao log in da se uradi)
#koristio sam installKorisnik u unosEntiteta da bih uneo korisnike kao menazder

# for ch in "!\"#$%&()*+,-./:;<=>?@[\\]^_’{|}":
#   text = text.replace(ch, " ")


#ovo ce morati da se preimenuje u ubiEntitete.py


#treba da sredim da pored svakog unosa pise formatu kom moze da se unese


#sredi da unos kategorije bude kada se odluci da se upise namestaj ne odmah automatski

#kod unosa imena i sta vec gledaj da ne moze da bude prazan string
# def installPassword():
#     password="naziv"
#     while True:
#         try:
#             password=input("Unesite password korisnika: ")
#             if password=="":
#                 password=installPassword()
#             password=int(password)
#             print("pogresan format password-a")
#         except ValueError:
#             return password

#izmena zove pretragu koja ako nadje 1 proizovd prosledi izmeni sifru 
#sifre su sortirane, tako da kad trazis po sifri radi merge sort(tj binarnu pretragu)

#if argument == None trazi jedinstevni deo entiteta
#else uzmi argument i odradi posao sa njim



# def proba(sifraNamestaja):
#     sifra=proveriArgumentSifra(sifraNamestaja)
#     listaRecnikaNamestaja=pretraga.pretragaUcitajNamestaj()
#     index=utvrdiIndex(listaRecnikaNamestaja,sifra)
#     recnik=proba1(listaRecnikaNamestaja,sifra,index)
#     print(recnik)

# def proba1(listaRecnikaNamestaja,sifra,index):
#     index=utvrdiIndex(listaRecnikaNamestaja,sifra)
#     if listaRecnikaNamestaja[index]["sifra"]==sifra and listaRecnikaNamestaja[index]["sifra"]=="false":
#         return listaRecnikaNamestaja[index]
#     return None

# def utvrdiIndex(listaRecnikaNamestaja,sifra):
#     donja=0
#     gornja=len(listaRecnikaNamestaja)-1

#     while donja<=gornja:
#         srednja=(donja+gornja)//2

#         if srednja==sifra:
#             return srednja
#         elif sifra<srednja:
#             gornja=srednja
#         elif sifra>srednja:
#             donja=srednja

#     return None

#ovde ces morati i funkciju koja trazi sve obrisane i jedna opcija koja mozes je da se vratis nazad u menu ili restore da uradis
#kod brisanja obrati paznju na novi red \n jer zadnji element nece biti false 

#u okviru brisanja cu imati i restore