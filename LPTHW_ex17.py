from sys import argv
from os.path import exists

##script, from_file, to_file = argv

print
print "-----------------------------------start----------------------------------------"
#print "Copying form %s to %s" % (from_file, to_file)
print "This file reads a file and writes its content to another file.\n"
from_file = raw_input("Insert the name of the file to read: ")
to_file = raw_input("Insert the name of the file to write: ")
print

#we could do these two on one line, how?
##in_file = open(from_file)
##indata = in_file.read()
indata = open(from_file).read()

print "The input file %s is %d bytes long" % (from_file, len(indata)) #supp: len() prende una stringa e ne restituisce le dimensioni in byte
print "Does the output file %s exist? %r \n" % (to_file, exists(to_file)) #supp: exists() prende un oggetto di tipo file e restituisce True se esso esiste, False se esso non esiste

print "I am ready to copy: hit RETURN to continue, CTRL-C to abort."
raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)
open(to_file, 'w').write(indata)

print "Allright, all done."

#out_file.close()
open(from_file).close()
#in_file.close()
open(to_file).close()
print "------------------------------------end-----------------------------------------"
print


print
print "ESERCIZIO"

script, from_file, to_file = argv

print
print "-----------------------------------start----------------------------------------"

open(argv[2], 'w').write(open(argv[1]).read())

open(from_file).close()
#open(to_file).close()
print "------------------------------------end-----------------------------------------"
print

