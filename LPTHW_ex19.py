#sys.argv non e' utilizzato dal programma di LPTHW, ma la utilizzo io nel mio esercizio
from sys import argv


#intestazione della funzione, iniziata con la proposizione def e terminata dai due punti
#Nome: cheese_and_crackers
#Argomenti: cheese_count, boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#corpo della funzione, indentato rispetto alla intestazione della funzione
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blancket. \n"

print "We can just give the function numbers directly:"
#chiama la funzione cheese_and_crackers, passandole:
#cheese_count= 20, 
#boxes_of_crackers= 20
cheese_and_crackers(20, 20)

print "OR, we can use the variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#chiama la funzione cheese_and_crackers, passandole:
#cheese_count = amount_of_cheese =10, 
#boxes_of_crackers = amount_of_crackers = 20
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math insede too:"
#chiama la funzione cheese_and_crackers, passandole:
#cheese_count = 10+20 = 30, 
#boxes_of_crackers = 5+6 = 11
cheese_and_crackers(10+20,5+6)

print "And we can combine the two, variables and math:"
#chiama la funzione cheese_and_crackers, passandole:
#cheese_count = amount_of_cheese + 100 = 110, 
#boxes_of_crackers = amount_of_crackers + 1000 = 1050
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print "-------------------------------------------------------------------------------------"
print
print "ESERCIZIO"

def toSec(y, d, h, m):
    s = 60 * ( m + 60 * ( h + 24 * (d + 365 * y)))
    print "%s anni, %s giorni, %s ore, %s minuti sono %s secondi" % (str(y), str(d), str(h), str(m), str(s))

print "Questo programma converte un numero di anni, giorni, ore e minuti in secondi."   

#presi valori da passare come argomenti da script
y_script = int(argv[1])
d_script = int(argv[2])
h_script = int(argv[3])
m_script = int(argv[4])

#presi valori da passare come argomenti da standard input
y_var = int(raw_input("Inserire il numero di anni: "))
d_var = int(raw_input("Inserire il numero di giorni: "))
h_var = int(raw_input("Inserire il numero di ore: "))
m_var = int(raw_input("Inserire il numero di minuti: "))

#presi valori da passare come argomenti da file. Le istruzioni datafile.readline(1) servono per scartare i \n alla fine delle varie linee, che viceversa sarebbero inclusi. L'argomento 1 passato ai comandi readline indica di leggere dalla linea un solo carattere.
datafile = open("LPTHW_ex19_data.txt", 'r') #LPTHW_ex19_data.txt contiene il valore 3 riportato sulle prime 4 linee
y_file = int(datafile.readline(1))
datafile.readline(1)
d_file = int(datafile.readline(1))
datafile.readline(1)
h_file = int(datafile.readline(1))
datafile.readline(1)
m_file = int(datafile.readline(1))
datafile.readline(1)
datafile.close()

#lanciata la funzione toSec passando come argomenti dei valori presi da script, da linea di comando, e inseriti manualmente
toSec(y_var, d_var, h_var, m_var)
toSec(y_var, d_var, h_var, 0)
toSec(y_var, d_var, 0, 0)
toSec(y_var, 0, 0, 0)
toSec(y_script, d_script, h_script, m_script)
toSec(y_script, d_script, h_script, 0)
toSec(y_script, d_script, 0, 0)
toSec(y_script, 0, 0, 0)
toSec(0, 0, 0, 0)
toSec(y_script, d_script, h_script, m_var)
toSec(y_script, d_script, h_var, m_var)
toSec(y_script, d_var, h_var, m_var)
toSec(y_file, d_file, h_file, m_file)
toSec(y_file, d_file, h_file, 0)
toSec(y_file, 0, 0, 0)
