import unosEntiteta
import pretraga
import racun
import izvestaj

def logIn():
    f=open("korisnici.txt","r")
    korisnici=f.readlines()
    f.close()    
    print("Dobro dosli, unesite Username i Password da bi ste se ulogovali.")
    username=unosEntiteta.installUsername()
    password=unosEntiteta.installPassword()
    while True:    
        for korisnik in korisnici:
            lKorisnik=korisnik.strip("\n").split("|")
            if lKorisnik[0]==username and lKorisnik[1]==password and lKorisnik[5]=="false":
                print("Dobro dosli: {0} {1}".format(lKorisnik[4],lKorisnik[0]))
                return lKorisnik #ovo obrisi ali ostavi return
        print("Pogresan Username ili Password ili je Account obrisan, pokusajte ponovo.")
        username=unosEntiteta.installUsername()
        password=unosEntiteta.installPassword()

def mainMenu(menadzerBool):
    print("Nalazite se u mainMenu")
    print("__________")
    print("   Menu")
    print("__________")
    print("0 - Izlaz")    
    print("1 - Pretraga")
    if menadzerBool:
        print("2 - Unos")        
        print("3 - Brisanje")
        print("4 - Izmena")
        print("5 - Izvestaj")
        
        
    else:
        print("2 - Prodaja(imace uslugu)")


def uslovmenadzer(komanda):
    return komanda==0 or komanda==1 or komanda==2 or komanda==3 or komanda==4 or komanda==5 or komanda==6

def uslovRadnik(komanda):
    return komanda==0 or komanda==1 or komanda==2 or komanda==3

def logInKomanda(menadzerBool):
    komanda="komanda"
    if menadzerBool:
        while not uslovmenadzer(komanda):
            try:
                komanda=int(input("Unesite komandu: "))
            except ValueError:
                print("Pogresan format komande, unesite broj sa menija")
    else:
        while not uslovRadnik(komanda):
            try:
                komanda=int(input("Unesite komandu: "))
            except ValueError:
                print("Pogresan format komande, unesite broj sa menija")


    return komanda

def grananje(user,menadzerBool):

    while True:
        mainMenu(menadzerBool)
        komanda=logInKomanda(menadzerBool)

        if komanda == 0:
            print("Pozdrav!")
            exit()
        if menadzerBool:
            if komanda==1:
                pretraga.pretragaGrananje()
            if komanda==2:
                unosEntiteta.unosGrananje()
            elif komanda==3:
                unosEntiteta.brisanjeGrananje()
            elif komanda==4:
                unosEntiteta.izmenaGrananje()
            elif komanda==5:
                izvestaj.izvestajGrananje()
        else:
            if komanda==1:
                pretraga.p_pretragaGrananje()
            if komanda==2:
                racun.prodaja(user)#racun.py


def main():
    unosEntiteta.install()
    user=logIn()

    menadzerBool=False
    if user[4]=="menadzer":
        menadzerBool=True

    grananje(user,menadzerBool)
    


if __name__=="__main__":
    main()
