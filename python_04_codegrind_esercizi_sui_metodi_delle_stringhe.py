# esercizio 1
stringa = "hello world"
stringa_maiuscola = stringa.upper()
print(stringa_maiuscola)
# esercizio 2
stringa = "BENVENUTI a roma"
stringa_minuscola = stringa.lower()
print(stringa_minuscola)
# esercizio 3
stringa = "il meglio deve ancora venire"
lista_parole = stringa.split()
print(lista_parole)
# esercizio 4
stringa = "hello world"
stringa_modificata = stringa.replace("world", "python")
print(stringa_modificata)
# esercizio 5
stringa = "                                                   ciao                                                                          "
stringa_modificata = stringa.strip()
print(stringa_modificata)
# esercizio 6
stringa = "abcdefghijklmnopqrstuvwxyz"
tre_caratteri = stringa[:3]
print(tre_caratteri)
# esercizio 7
stringa = "Python"
starts_with_Py = stringa.startswith("Py")
print(starts_with_Py)
# esercizio 8
stringa = "Ciao mondo"
conteggio = stringa.count("o")
print(conteggio)
# esercizio 9
stringa = "Ciao mondo"
risultato = stringa[-5:].upper().replace("o", "k")