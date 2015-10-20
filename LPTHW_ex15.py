#importa l'attributo argv del modulo sys.
#sys.argv permette di leggere input passati come argomenti allo script python
from sys import argv

#spacchettto la lista argv in due variabili: script = argv[0], contenente il nome dello script; filename = argv[1], contenete una stringa (percorso di un file) passato come parametro allo script
script, filename = argv

#open apre il file dal percorso filename e restituisce un oggetto della classe file associato al file aperto. Quest'ultimo oggetto della classe file e' salvato nella variabile txt.
txt = open(filename)

#stampa a std output, ponendo al posto della format string %r l'argomento filename passato come parametro allo script.
print "Here's your file %r:" % filename
#il metodo read restituisce il contenuto del file cui si riferisce l'oggetto di tipo file salvato nella variabile txt
print txt.read()pydoc close
txt.close()

#come sopra, ma questa volta il percorso del file da aprire e' letto da standard input
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
