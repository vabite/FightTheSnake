#questo script serve a me per testare alcune cose su tuple e liste

from sys import argv

print "TUPLE: impacchettamento, spacchettamento; accessibilita', inizializzazione tramite indicizzazione"

tupla0 = (1, 4, 5)
print "Se si puo' impacchettare & accedere a una tupla tramite indicizzazione, qui di seguito deve comparire il numero 4: ", tupla0[1]

(pippo, pluto, paperino) = tupla0
print "Se si puo' spacchettare una tupla, qui di seguito deve comparire la serie 1 4 5: ", pippo, pluto, paperino
#per vedere se le tuple hanno il metodo len()
print "La lunghezza della tupla e' ", len(tupla0)

tupla1 = (pippo, pluto, paperino)
#tupla1[0] = 5
print "Se si puo' inizializzare una tupla tramite indicizzazione, qui di seguito deve comparire una tupla: ", #tupla1

#--> siccome ottengo un errore nella parte di inizializzazione di una tupla tramite indicizzazione, suppongo sia possibile solo accedere alla tupla tramite indicizzazione


print "\n-----------------------------------------------------------"
print "LISTE: impacchettamento, spacchettamento; accessibilita', inizializzazione tramite indicizzazione"

lista0 = [1, 4, 5]
print "Se si puo' impacchettare & accedere a una lista tramite indicizzazione, qui di seguito deve comparire il numero 4: ", lista0[1]

(pippo, pluto, paperino) = lista0
print "Se si puo' spacchettare una lista, qui di seguito deve comparire la serie 1 4 5: ", pippo, pluto, paperino

lista1 =[pippo, pluto, paperino]
lista1[0] =5
print "Se si puo' inizializzare una lista tramite indicizzazione, qui di seguito deve comparire una lista: ", lista1

print "\n-----------------------------------------------------------"
print "ARGV: qui testo se vari elementi visti finora sono o meno delle tuple"

argv.append(5)

print "Se sys.argv e' una lista, allora qui di seguito deve essere mostrata una lista contenente il nome dello script seguito dagli argomenti passati allo script e infine dal numero 5", argv

print "\n-----------------------------------------------------------"
print "DICTIONARY"

dic1 = {'a':1, 2:2, 'c':'a'}
key = 'c'
elem = dic1[key]
print "\nIl valore associato alla chiave \'%s\' e': " % key, elem
print "La seguente stampa del dizionario mostra come key e value possano essere insiemi eterogenei: ", dic1

dic2={'Panda':(1, 4), 5:'Foca'}
dic1['a']=dic2
print "La seguente stampa del dizionario mostra come i dizionari possano essere annidabili: ", dic1
print len(dic2)

print "\n-----------------------------------------------------------"
print "SET"

set1 = {'Mele', 2 , 2, 4.5}
print "La seguente stampa mostra come i set possano essere eterogenei: ", set1
#set2 = {3, 5, 6, {4, 'd', 4.3}}
#print "La seguente stampa mostra come i set possano essere annidati: ", set2
#non e' possibile annidare i set!



