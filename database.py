import sqlite3
plik = sqlite3.connect('baza_osoby.db')
print("Otorzono baze\n")
plik_baza = plik.cursor()
class baza():
    def start():
        plik_baza.executescript('''
            CREATE TABLE IF NOT EXISTS Osoby
            (ID INT PRIMARY KEY ASC,
            Imie CHAR(50) NOT NULL,
            Wiek INT NOT NULL,
            ADRES CHAR(50) NOT NULL,
            ZAROBKI REAL)''')
        print("Utworzono tabele\n")

    def dodawanie():
        x=int(input('Ile osob chcesz dodac ?\n'))
        for i in range(x):
            ID=int(input('Podaj ID:\n'))
            Imie=str(input('Podaj imie:\n'))
            Wiek=int(input('Podaj wiek:\n'))
            Adres=str(input('Podaj adres:\n'))
            Zarobki=float(input('Podaj zarobki:\n'))
            plik_baza.execute("INSERT INTO Osoby VALUES(?,?,?,?,?)",(ID, Imie, Wiek, Adres, Zarobki));
            plik.commit()
            
    def wyswietlanie():
        cursor = plik_baza.execute("SELECT ID, Imie, Wiek, Adres, Zarobki  FROM Osoby ORDER BY Imie")
        for row in cursor:
            print("ID = ", row[0])
            print("Imie = ", row[1])
            print("Wiek = ", row[2])
            print("Adres = ", row[3])
            print("Zarobki = ", row[4], "\n")

    def modyfikowanie():
        while(1):
            a=int(input('Podaj ID osoby ktorej dane chcesz zmienic: (wpisz 0 aby wyjsc)\n'))
            if a!=0:
                while(1):
                    print("ID, Imie, Wiek, Adres, Zarobki")
                    c=str(input('Podaj atrybut który chcesz zmienic (wpisz 00 aby wyjsc)\n'))
                    if c=='ID':
                        c=int(input('Podaj nowa wartosc atrybutu\n'))
                        plik_baza.execute('UPDATE Osoby SET ID=? WHERE ID=?', (c, a))
                        plik.commit
                    elif c=="Imie":
                        c=str(input('Podaj nowa wartosc atrybutu\n'))
                        plik_baza.execute('UPDATE Osoby SET Imie=? WHERE ID=?', (c, a))
                        plik.commit
                    elif c=="Wiek":
                        c=int(input('Podaj nowa wartosc atrybutu\n'))
                        plik_baza.execute('UPDATE Osoby SET Wiek=? WHERE ID=?', (c, a))
                        plik.commit
                    elif c=="Adres":
                        x=str(input('Podaj nowa wartosc atrybutu\n'))
                        plik_baza.execute('UPDATE Osoby SET Adres=? WHERE ID=?', (c, a))
                        plik.commit
                    elif c=="Zarobki":
                        c=str(input('Podaj nowa wartosc atrybutu\n'))
                        plik_baza.execute('UPDATE Osoby SET Zarobki=? WHERE ID=?', (c, a))
                        plik.commit
                    elif c=='00':
                        break;
                    else:
                        print("Zly atrybut")
            elif a==0:
                break;
                menu()
            else:
                print("Zly numer")

    def usuwanie():
            a=int(input('Podaj ID osoby ktora chcesz usunac: (wpisz 0 aby wyjsc)\n'))
            if a!=0:
                plik_baza.execute("DELETE from Osoby where ID=?", (a,))
                plik.commit
            elif a==0:
                menu()
            else:
                print("Zly numer")
    def opcja5():
        a=int(input('Podaj dolna granice przedzialu\n'))
        b=int(input('Podaj gorna granice przedzialu\n'))
        cursor = plik_baza.execute("SELECT ID, Imie, Wiek, Adres, Zarobki  FROM Osoby WHERE Wiek>=? and Wiek<=?", (a,b))
        for row in cursor:
            print("ID = ", row[0])
            print("Imie = ", row[1])
            print("Wiek = ", row[2])
            print("Adres = ", row[3])
            print("Zarobki = ", row[4], "\n")

    def opcja6():
        cursor = plik_baza.execute('SELECT ID, Osoby.Zarobki FROM Osoby WHERE Osoby.Zarobki In (SELECT MAX(Osoby.Zarobki) FROM Osoby);')
        for row in cursor:
            print("ID = ", row[0])
            print("Zarobki = ", row[1], "\n")

    def opcja7():
        cursor = plik_baza.execute("SELECT ID, Imie, Wiek, Adres, Zarobki  FROM Osoby ORDER BY Wiek DESC")
        for row in cursor:
            print("ID = ", row[0])
            print("Imie = ", row[1])
            print("Wiek = ", row[2])
            print("Adres = ", row[3])
            print("Zarobki = ", row[4], "\n")
            
        
    def koniec():
        plik.commit()
        plik_baza.close()
        print("Zamknieto baze")




def menu():
    while(1):
        print("1-Dodaj nowe osoby\n2-Wyświetl osóby posortowane alfabetycznie po imieniu\n3-Modyfikuj wpisy w bazie\n4-Usun osoby\n5-Wyświetl osóby, które mają wiek w konkretnym przedziale\n6-Wyświetl najwieksze zarobki\n7-Wyswietl osoby od najmlodszych do najstarszych\n8-Wyjscie")
        x=int(input('Podaj numer opcji:\n'))
        if x==1:
            baza.dodawanie()
        elif x==2:
            baza.wyswietlanie()
        elif x==3:
            baza.modyfikowanie()
        elif x==4:
            baza.usuwanie()
        elif x==5:
            baza.opcja5()
        elif x==6:
            baza.opcja6()
        elif x==7:
            baza.opcja7()
        elif x==8:
            baza.koniec()
            break;
        else:
            print("Zly numer")




def main():
    baza.start()
    menu()
    
if __name__=="__main__":
    main() 
