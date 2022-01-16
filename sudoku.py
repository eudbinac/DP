import sys, math, time, os, random

sys.path.append("./python-constraint-1.4.0")

from constraint import *

velicinaIgre = 0
sudokuIme=""
izlazIzIgre="IZLAZ IZ IGRE"
upute="UPUTE"
mrezaIgre=[]
prvaRazinaIgreUspjesnoRijesena=False
drugaRazinaIgreUspjesnoRijesena=False

def zapisiImeIgraca():
    print("\n\n\n")
    print("______________________________________SUDOKU______________________________________")
    print("Igra koja razvija mozak, potice na razmisljanje i tjera na strpljivo promisljanje.\n")
    print("Molimo Vas da odaberete svoje 'sudoku ime'. ")
    global sudokuIme
    sudokuIme = input("Moje sudoku ime: ")
    print("\n")

def rijesiSudoku(velicinaSudokuIgre, igra = None):
    if(velicinaSudokuIgre==4):
        zbroj=10
    if(velicinaSudokuIgre==9):
        zbroj=45
        
    sudoku = Problem()

    redoviMreze = range(velicinaSudokuIgre)
    stupciMreze = range(velicinaSudokuIgre) 
 
    mreza = [(red, stupac) for red in redoviMreze for stupac in stupciMreze]
    sudoku.addVariables(mreza, range(1, velicinaSudokuIgre * velicinaSudokuIgre + 1))
 
    postaviRed = [list(zip([elem] * len(stupciMreze), stupciMreze)) for elem in redoviMreze]
    postaviStupac = [list(zip(redoviMreze, [elem] * len(redoviMreze))) for elem in stupciMreze]
 
    if igra is not None:
        for i in range(0, velicinaSudokuIgre):
            for j in range(0, velicinaSudokuIgre):
                zapisaniBroj = igra[i][j]
                if zapisaniBroj > 0:
                    parRedStupac = (redoviMreze[i],stupciMreze[j])
                    sudoku.addConstraint(lambda var, val=zapisaniBroj: var == val, (parRedStupac,))
    for red in postaviRed:
        sudoku.addConstraint(ExactSumConstraint(zbroj), red)
        sudoku.addConstraint(AllDifferentConstraint(), red)
    for stupac in postaviStupac :
        sudoku.addConstraint(ExactSumConstraint(zbroj), stupac)
        sudoku.addConstraint(AllDifferentConstraint(), stupac)
 
    korijenVelicinaSudokuIgre=0
    if(velicinaSudokuIgre==4):
        korijenVelicinaSudokuIgre=2
    if(velicinaSudokuIgre==9):
       korijenVelicinaSudokuIgre=3
 
    for i in range(0,velicinaSudokuIgre,korijenVelicinaSudokuIgre):
        for j in range(0,velicinaSudokuIgre,korijenVelicinaSudokuIgre):
            polje = []
            for k in range(0, korijenVelicinaSudokuIgre):
                for l in range(0, korijenVelicinaSudokuIgre):
                    polje.append( (i+k, j+l) )
            sudoku.addConstraint(ExactSumConstraint(zbroj), polje)
            sudoku.addConstraint(AllDifferentConstraint(), polje)
    return sudoku.getSolution()

def imaNulaUMatrici(mrezaIgre):
    for i in mrezaIgre:
        if 0 in i:
            return True
    return False

def imaUpisanuVrijednost(mrezaIgre, stupac, redak):
    if mrezaIgre[redak][stupac] > 0:
        return True
    return False

def ispisMrezeIgre():
    global velicinaIgre
    global mrezaIgre
    if(velicinaIgre==4):
        print("\n-----------")
        print("   A B  C D")
        for i in range(0, velicinaIgre):
            oneLine = str(i+1) + "  "
            for j in range(0, velicinaIgre):
                oneLine += str(mrezaIgre[i][j]) + " "
                if j==1 or j==5:
                    oneLine += " "
            print(oneLine)
            if i==1 or i==5:
                print()
        print("-----------\n")
        
    if(velicinaIgre==9):
        print("\n----------------------")
        print("   A B C  D E F  G H I")
        for i in range(0, velicinaIgre):
            oneLine = str(i+1) + "  "
            for j in range(0, velicinaIgre):
                oneLine += str(mrezaIgre[i][j]) + " "
                if j==2 or j==5 or j==8:
                    oneLine += " "
            print(oneLine)
            if i==2 or i==5 or i==8:
                print()
        print("----------------------\n")

def izlazakIzIgre():
        sys.exit("Bok!")

def prikaziUpute():
        os.startfile('sudokuUpute.txt')

def poloziSudokuTreningIgru():
        global sudokuIme
        global mrezaIgre
        global velicinaIgre
        velicinaIgre=4
        uspjesnoPolozenTestniZadatak = False
        print (sudokuIme,"za pocetak se zagrij uz 4x4 SUDOKU TRENING IGRU.")
        print ("Uspješno položena trening igra omogucujete ti ulazak u svijet Sudoka.\n")
        time.sleep(1)
        print("  Sretno!\n")
        global inicijalnaMreza
        inicijalnaMreza = [[0, 2, 4, 0],
                          [1, 0, 0, 3],
                          [4, 0, 0, 2],
                          [0, 1, 3, 0]]
        oznakeStupaca = ['A', 'B', 'C', 'D']
        oznakeRedaka = ['1', '2', '3', '4']
        mrezaIgre=inicijalnaMreza
        while imaNulaUMatrici(mrezaIgre) == True:
            ispisMrezeIgre()
            while True == True:
                stupac = ""
                redak = ""
                broj = ""
                stupacBroj = ""
                while (stupac not in oznakeStupaca): 
                    print("Unesite oznaku stupca: ")
                    stupac = input().upper()
                    if (stupac not in oznakeStupaca):
                        print("Molimo unesite ispravnu oznaku stupca.")                
                while (redak not in oznakeRedaka):
                    print("Unesite oznaku retka: ")
                    redak = input()
                    if (redak not in oznakeRedaka):
                        print("Molimo unesite ispravnu oznaku retka.\n")
                redakInt = int(redak)-1
                if stupac=="A":
                    stupacBroj = 0
                if stupac=="B":
                    stupacBroj = 1
                if stupac=="C":
                    stupacBroj = 2
                if stupac=="D":
                    stupacBroj = 3
                if imaUpisanuVrijednost(mrezaIgre, stupacBroj, redakInt) == False:
                    while(broj!="1" and broj!="2" and broj!="3" and broj!="4"): 
                        print("Unesite broj: ")
                        broj = input()
                        if (broj!="1" and broj!="2" and broj!="3" and broj!="4"):
                            print("Oznaka koju želite unijeti u polje ne odgovara brojevima koji se trebaju unijeti unutar ploce za igranje.")
                    break
                else:
                    print("Polje s danim oznakama vec ima upisanu vrijednost!")
            brojInt = int(broj)
            mrezaIgre[redakInt][stupacBroj] = brojInt
            konacnoRjesenje = rijesiSudoku(velicinaIgre, mrezaIgre)
            print
            if konacnoRjesenje is None:
                mrezaIgre[redakInt][stupacBroj] = 0
                print("Neispravan unos koji ne vodi do ispravnog rješenja igre.\n")
                print("Nastavite s igrom.\n")

        print("Uspjesno ste rijesili SUDOKU TRENING IGRU!")
        uspjesnoPolozenTestniZadatak = True
        ispisMrezeIgre()
        if(uspjesnoPolozenTestniZadatak == True):
            ispisGlavnogIzbornika()

def ispisPocetnogIzbornika():
    pocetakIgre="ZAPOCNI IGRU"
    while True == True:
        izbor = ""
        izbor = input("Za pocetak igre unesi 'Zapocni igru'.\nZa upute kako igrati unesi 'Upute'.\nZa izlaz iz igre unesi 'Izlaz iz igre'.\n ").upper()
        print("\n")
        if(izbor!=pocetakIgre and izbor!="IZLAZ IZ IGRE" and izbor!="UPUTE"):
            print("Niste unijeli ispravan izbor.\n")
        if(izbor==izlazIzIgre):
            izlazakIzIgre()
        if(izbor==upute):
            prikaziUpute()
        if (izbor==pocetakIgre):
            poloziSudokuTreningIgru()

def ispisGlavnogIzbornika():
    odabirOpcijeRazinaIgre="ODABIR RAZINE IGRE"
    izbor = ""
    global izlazIzIgre
    global upute
    while True == True:
        izbor=input("Za novu igru unesi 'Odabir razine igre'.\nZa upute kako igrati unesi 'Upute'.\nZa izlaz iz igre unesi 'Izlaz iz igre'.\n").upper()
        print("")
        if(izbor!="ODABIR RAZINE IGRE" and izbor!="IZLAZ IZ IGRE" and izbor!="UPUTE"):
            print("Niste unijeli ispravan izbor.\n")
        if(izbor==izlazIzIgre):
            izlazakIzIgre()
        if(izbor==upute):
            prikaziUpute()
        if(izbor==odabirOpcijeRazinaIgre):
            odabirRazineIgre()

def ucitajIgruIzDatoteke(nazivDatoteke):
    mrezaIgre = []
    datoteka = open(nazivDatoteke, 'r')
    sadrzaj = datoteka.readlines()
    for linija in sadrzaj:
        redak = linija.split(" ")
        red = []
        for elem in redak:
            red.append(int(elem))
        mrezaIgre.append(red)
    datoteka.close()
    return mrezaIgre
    
def igrajIgru(mrezaIgre, razina):
    global sudokuIme
    global velicinaIgre
    time.sleep(1)
    velicinaIgre=9
    oznakeStupaca = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    oznakeRedaka = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while imaNulaUMatrici(mrezaIgre) == True:
        ispisMrezeIgre()
        while True == True:
            stupac = ""
            redak = ""
            broj = ""
            stupacBroj = ""
            while (stupac not in oznakeStupaca): 
                print("Unesite oznaku stupca: ")
                stupac = input().upper()
                if (stupac not in oznakeStupaca):
                    print("Molimo unesite ispravnu oznaku stupca.")                
            while (redak not in oznakeRedaka):
                print("Unesite oznaku retka: ")
                redak = input()
                if (redak not in oznakeRedaka):
                    print("Molimo unesite ispravnu oznaku retka.\n")
            redakInt = int(redak)-1
            if stupac=="A":
                stupacBroj = 0
            if stupac=="B":
                stupacBroj = 1
            if stupac=="C":
                stupacBroj = 2
            if stupac=="D":
                stupacBroj = 3
            if stupac=="E":
                stupacBroj = 4
            if stupac=="F":
                stupacBroj = 5
            if stupac=="G":
                stupacBroj = 6
            if stupac=="H":
                stupacBroj = 7
            if stupac=="I":
                stupacBroj = 8
            if imaUpisanuVrijednost(mrezaIgre, stupacBroj, redakInt) == False:
                while(broj!="1" and broj!="2" and broj!="3" and broj!="4" and broj !="5" and broj!="6" and broj!="7" and broj!="8" and broj!="9"): 
                    print("Unesite broj: ")
                    broj = input()
                    if (broj!="1" and broj!="2" and broj!="3" and broj!="4" and broj !="5" and broj!="6" and broj!="7" and broj!="8" and broj!="9"):
                        print("Oznaka koju želite unijeti u polje ne odgovara brojevima koji se trebaju unijeti unutar ploce za igranje.")
                break
            else:
                print("Polje s danim oznakama vec ima upisanu vrijednost!")
        brojInt = int(broj)
        mrezaIgre[redakInt][stupacBroj] = brojInt
        konacnoRjesenje = rijesiSudoku(velicinaIgre, mrezaIgre)
        print
        if konacnoRjesenje is None:
            mrezaIgre[redakInt][stupacBroj] = 0
            print("Neispravan unos koji ne vodi do ispravnog rješenja igre.\n")
            print("Nastavite s igrom.\n")

    print(sudokuIme," uspjesno ste rijesili SUDOKU IGRU!")

    global prvaRazinaIgreUspjesnoRijesena
    global drugaRazinaIgreUspjesnoRijesena
    if(razina==1):
        prvaRazinaIgreUspjesnoRijesena = True
    if(razina==2):
        drugaRazinaIgreUspjesnoRijesena = True

def odabirRazineIgre():
    global velicinaIgre
    velicinaIgre=9
    razinaJedan="1"
    razinaDva="2"
    razinaTri="3"
    odabranaRazina=""
    global prvaRazinaIgreUspjesnoRijesena
    global drugaRazinaIgreUspjesnoRijesena
    global mrezaIgre
    while True==True:
        print("\n____________Odaberi razinu igre._____________")
        print("Za odabir razine igre, unesi broj: 1, 2 ili 3.")
        print("Za pregled uputa, unesi Upute.")
        print("Za izlazak iz igre, unesi Izlaz.\n")
        print("1 - Tek se ucim igrati Sudoku")
        print("2 - Znam igrati Sudoku")
        print("3 - Ima li tko bolji od mene")
        print("Napomena: Visu razinu moguce je otkljucati ako je niza razina uspjesno rijesena barem jednom.\n")
        odabranaRazina=input("Razina igre koju zelim igrati: ").upper()
        if(odabranaRazina!=razinaJedan and odabranaRazina!=razinaDva and odabranaRazina!=razinaTri):
            print("\nNiste unijeli ispravan broj koji označava razinu igre koju želite odabrati.\nUnesite Vaš izbor ponovno.\n")
            print(" ")
        if(odabranaRazina==razinaJedan):
            print("\nOdabrali ste razinu igre 'Tek se ucim igrati'.\n_______SRETNO_______")
            mrezaIgre = ucitajIgruIzDatoteke("prva" + str(random.randrange(1, 3)) + ".txt")
            igrajIgru(mrezaIgre, 1)
        if(odabranaRazina==razinaDva):
            if(prvaRazinaIgreUspjesnoRijesena==True):
                print("\nOdabrali ste razinu igre 'Znam igrati Sudoku'.\n_______SRETNO_______")
                mrezaIgre = ucitajIgruIzDatoteke("druga" + str(random.randrange(1, 3)) + ".txt")
                igrajIgru(mrezaIgre, 2)
            else:
                print("\nNiste uspješno prošli prvu razinu.")
        if(odabranaRazina==razinaTri):
            if(prvaRazinaIgreUspjesnoRijesena==True and drugaRazinaIgreUspjesnoRijesena==True):
                print("\nOdabrali ste razinu igre 'Ima li tko bolji od mene'.\n_______SRETNO_______")
                mrezaIgre = ucitajIgruIzDatoteke("treca" + str(random.randrange(1, 3)) + ".txt")
                igrajIgru(mrezaIgre, 3)
            if(prvaRazinaIgreUspjesnoRijesena==False and drugaRazinaIgreUspjesnoRijesena==False):
                print("\nNiste uspješno prošli prvu i drugu razinu.")
            elif(drugaRazinaIgreUspjesnoRijesena==False):
                print("\nNiste uspješno prošli drugu razinu.")
        if(odabranaRazina=="IZLAZ"):
            izlazakIzIgre()
        if(odabranaRazina=="UPUTE"):
            prikaziUpute()
            
                
if __name__ == '__main__':
    zapisiImeIgraca()
    
    ispisPocetnogIzbornika()

