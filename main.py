
import ast

class Ksiazka:
  def __init__(self, tytul, autor):
    self.tytul=tytul
    self.autor=autor

class Egzemplarz:
  def __init__(self, tytul, autor, rok):  
    self.tytul=tytul
    self.autor=autor
    self.rok=rok

class Biblioteka:
  ksiazki_lista=[]
  egzemplarze_lista=[]

  def czy_jest_ksiazka(self, tytul, autor):
    self.tytul=tytul
    self.autor=autor
    czy_ksiazka=False
    for ksiazka in self.ksiazki_lista:
      if ksiazka.tytul==tytul:
        czy_ksiazka=True
    return czy_ksiazka

  def dodaj_egzemplarz(self, tytul, autor, rok):
        ksiazka=self.czy_jest_ksiazka(tytul, autor)
        if ksiazka==False:
            ks=Ksiazka(tytul, autor)
            self.ksiazki_lista.append(ks)
        self.egzemplarze_lista.append(Egzemplarz(tytul, autor, rok)) 


  def pozycja(self, ksiazki_lista, egzemplarze_lista):
    for i in range(len(self.ksiazki_lista)):
      liczba=0
      k=ksiazki_lista[i]
      for i in range(len(self.egzemplarze_lista)):
        eg = egzemplarze_lista[i]
        if k.tytul==eg.tytul and k.autor==eg.autor:
          liczba=liczba + 1
      liczba=str(liczba)      
      print("('"+k.tytul+"',","'"+k.autor+"', "+liczba+")")

   
biblioteka=Biblioteka()
pozycje=[]
n=int(input())
for i in range (0,n):
  eg=eval(input())
  pozycje.append(eg)
  biblioteka.dodaj_egzemplarz(pozycje[i][0],pozycje[i][1],pozycje[i][2])
  
biblioteka.pozycja(sorted(biblioteka.ksiazki_lista,key=lambda ksiazka:ksiazka.tytul),biblioteka.egzemplarze_lista)


import ast

class Ksiazka:
  def __init__(self, tytul, autor):
    self.tytul=tytul
    self.autor=autor

class Egzemplarz:
  def __init__(self, tytul, autor, rok):  
    self.tytul=tytul
    self.autor=autor
    self.rok=rok

class Biblioteka:
  ksiazki_lista=[]
  egzemplarze_lista=[]

  def czy_jest_ksiazka(self, tytul, autor):
    self.tytul=tytul
    self.autor=autor
    czy_ksiazka=False
    for ksiazka in self.ksiazki_lista:
      if ksiazka.tytul==tytul:
        czy_ksiazka=True
    return czy_ksiazka

  def dodaj_egzemplarz(self, tytul, autor, rok):
        ksiazka=self.czy_jest_ksiazka(tytul, autor)
        if ksiazka==False:
            ks=Ksiazka(tytul, autor)
            self.ksiazki_lista.append(ks)
        self.egzemplarze_lista.append(Egzemplarz(tytul, autor, rok)) 


  def pozycja(self, ksiazki_lista, egzemplarze_lista):
    for i in range(len(self.ksiazki_lista)):
      liczba=0
      k=ksiazki_lista[i]
      for i in range(len(self.egzemplarze_lista)):
        eg = egzemplarze_lista[i]
        if k.tytul==eg.tytul and k.autor==eg.autor:
          liczba=liczba + 1
      liczba=str(liczba)      
      print("('"+k.tytul+"',","'"+k.autor+"', "+liczba+")")

   
biblioteka=Biblioteka()
pozycje=[]
n=int(input())
for i in range (0,n):
  eg=eval(input())
  pozycje.append(eg)
  biblioteka.dodaj_egzemplarz(pozycje[i][0],pozycje[i][1],pozycje[i][2])
  
biblioteka.pozycja(sorted(biblioteka.ksiazki_lista,key=lambda ksiazka:ksiazka.tytul),biblioteka.egzemplarze_lista)

