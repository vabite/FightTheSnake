import LPTHW_ex25
 
#acquisisce una frase   
#sentence = raw_input("Scrivi una frase: ")
sentence = "mamma mia, sono diventato blu!"

print "La lista delle parole ottenute dalla frase inserita e': ", LPTHW_ex25.break_words(sentence)
print

print "La lista ordinata delle parole ottenute dalla frase inserita e': ", LPTHW_ex25.sort_words(LPTHW_ex25.break_words(sentence))
print

print "Come sopra, ma con una altra funzione: ", LPTHW_ex25.sort_words(LPTHW_ex25.break_words(sentence))
print

print "La prima parola in ordine alfabetico della frase inserita e': ", LPTHW_ex25.print_first_word(LPTHW_ex25.sort_words(LPTHW_ex25.break_words(sentence)))
print

print "L'ultima parola in ordine alfabetico della frase inserita e': ", LPTHW_ex25.print_last_word(LPTHW_ex25.sort_words(LPTHW_ex25.break_words(sentence)))
print

print "Come sopra, ma con una altra funzione.La prima e l'ultima parola della frase inserita sono: ", LPTHW_ex25.print_first_and_last(sentence)
print

print "Come sopra, ma con una altra funzione. La prima e l'ultima parola in ordine alfabetico della frase inserita sono: ", LPTHW_ex25.print_first_and_last_sorted(sentence)
print
