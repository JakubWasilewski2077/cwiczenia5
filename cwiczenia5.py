# Opercaje na plikach można podzielić na trzy etapy:
# 1.Otwarcie pliku
# 2.Działanie na pliku (odczyt lub zapis)
# 3.Zamknięcie plikuplik = open(nazwa, tryb, bufor)
# gdzie:
# plik –nazwa obiektu, którą sami nadajemy
# nazwa –nazwa pliku na dysku, jaka jest
# tryb –tryb otwarcia pliku (np. do odczytu, do zapisu itd.)
# bufor –obszar pamięci przechowujący dane w oczekiwaniu na zapis i odczyt


# Wybrane tryby otwarcia plików:
# r –tylko do odczytu. Plik musi istnieć:
# w –tylko do zapisu. Jeżeli pliku nie ma to zostanie utworzony a jeżeli jest to jego zawartość zostanie zastąpiona nową.
# a –do dopisywania. Dane dopisują się na końcu pliku. Jeśli plik nie istnieje to zostanie utworzony
# r+ -do odczytu i zapisu. Plik musi istnieć.w+ -do odczytu i zapisu. Jeśli plik nie istnieje zostanie utworzony.
# a+ -do odczytu i zapisu. Jeśli plik nie istnieje zostanie utworzony.

#zadanie1
zbiorA = []
for x in range(0,31):
    zbiorA.append(x)
zbiorB = []
for x in zbiorA:
    zbiorB.append(x * 2)
print(zbiorB)
plik1 = open("zadanie1_22_03.txt","w+")
plik1.write(str(zbiorB))
plik1.close()

#zadanie2
plik2 =  open("tekst.txt","r",encoding='utf-8')
textpliku2 = plik2.read()
print(textpliku2)
plik2.close()

#zadanie3
with open("zadanie3_22_03.txt","w+") as plik3:
    plik3.write("ABCD abcd 2137")
    plik3.close()
with open("zadanie3_22_03.txt","r") as plik3:
    plik3b = plik3.read()
    print(plik3b)
    plik3.close()

# #zadanie4
# class NaZakupy:
#     nazwa_produktu
#     ilosc
#     jednostka_miary
#     cena_jed

