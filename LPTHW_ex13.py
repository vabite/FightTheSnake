from sys import argv 
#sys.argv contiene gli argomenti passati a uno script; argv[0] contiene' il percorso dello script, se noto.

script, first, second, third = argv
#spacchetta il vettore argv, assegnando il contenuto delle sue celle alle variabili indicate

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#riga per verificare che tipo viene assegnato ai parametri passati allo script
print "%r %r %r %r" %(script, first, second, third)
