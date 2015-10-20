formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) #la stringa di formattazione %r applicata agli integer stampa il loro valore trasposto in stringa senza modifiche
print formatter % ("one", "two", "three", "four") #la stringa di formattazione %r applicata ad una stringa stampa la stessa o tra ' o tra "
print formatter % (True, False, False, True) #la stringa di formattazione %r applicata ai boolean stampa il loro valore trasposto in stringa senza modifiche
print formatter % (formatter, formatter, formatter, formatter) #la stringa di formattazione %r applicata ad una stringa stampa la stessa o tra ' o tra "
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) #la stringa di formattazione %r applicata ad una stringa stampa la stessa o tra ' o tra "
