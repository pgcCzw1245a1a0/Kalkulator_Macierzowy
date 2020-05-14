#!/usr/bin/python
# -*- coding: utf-8 -*-

#funkcja zbierajaca zapisujaca  macierz w pliku txt
def save_matrix():
    filepath = "\memory\\" + filename #do uzgodnienia
    file = open(filepath,"r")
    lines = ['pierwsza\n', 'druga\n', 'trzecia\n']
    file.writelines(lines)

#Jeśli mamy liste bez znakow konca linii
#>>> lines = ['pierwsza', 'druga', 'trzecia']
#>>> lines = [line + "\n" for line in lines]
#>>> lines
    file.close()
    pass

#funkcja wczytujaca z pliku jedno z dziesieciu zadań
def load_exercise():
    filepath = ".\memory\ " + filename
    file = open(filepath, "w")
    # funkcja odczytujaca konkretne linie
    for line in file:
        ##tutaj wczytujemy odpowiednie dane
    file.close()
    pass
