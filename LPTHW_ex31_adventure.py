
# coding: utf-8

# # Adventure

# In[8]:

name = raw_input("Come ti chiami, avventuriero? ")


# In[9]:

print "Ciao %s. Ora inizia la tua avventura" % name


# In[10]:

bivio1 = raw_input("Sei in un corridoio lungo e buio. Hai tre porte davanti a te. Entri nella 1, nella 2 o nella 3?")


# ##Bivio 1

# In[ ]:

if bivio1 == "1":
    bivio2 = raw_input(
        """
        Trovi Edoardo Vacchi, con un biglietto per la California fresco fresco. Cosa fai? \n
            1. Provo a rubarglielo di mano.\n
            2. Gli dico che ora i prezzi dello stessa tratta si sono dimezzati.\n
            3. "Californiaaa, Californiaaaaaaa, here we coooooooome!".\n
            
        """)
elif bivio1== "2":
    bivio2 = raw_input(
        '''
        Trovi Stefano Pascolutti, che maneggia un cubo di Rubrik in modo molto ambiguo. cosa fai?   \n    
            1. Gli consiglio di passare al livello successivo e aggiungere la 4a dimensione al suo gioco.\n
            2. Gli consiglio di risolvere il cubo in maniera algoritmica.\n
            3. "Ma la PlayStation no?"\n
        ''' )
else:
    bivio2 = raw_input(
        '''
        Trovi Fabio che mangia i muffin della Milka. Cosa fai?\n
            1. Gli dici che la glassa in effetti non è cioccolata ma sono conservanti condensati.\n
            2. Gli dici che non mi fiderei di mangiare cioccolato prodotto con il latte di una mucca viola.\n
            3. "Le mucche fanno \'Muuuu\', ma una fa \'Mu muuuuu\'!!". Ah, no, quello era Fruttolo...\n
        ''')


# In[12]:

if bivio2 == "1": 
    print "Fabio Ramponi conferma."
elif bivio2 == "2":
    print "Fabio Ramponi ti azzanna"
else:
    print "Fabio Ramponi dice di rinchiude in un Bit Coin."


# In[ ]:

print "Fine della storia."


# ##The end
