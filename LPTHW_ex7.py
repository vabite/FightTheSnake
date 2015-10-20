#Il comando print, senza virgola finale, inserisce un a capo al termine della stringa stampata a standard input
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
#sembra che la moltiplicazione di una stringa per un integer restituisca la stringa concatenata con se stessa tante volte quante il valore dell'integer
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# whatch that comma at the end. Try removing it to see what happens
#L'inserzione di una virgola al termine del comando di print fa sì che la stampa a standard input termini con uno spazio, ma senza un a capo
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 +end10 + end11 +end12
