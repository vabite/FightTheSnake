
# coding: utf-8

# #While Loops

# In[20]:

numbers = []


# ##Definizione funzioni

# Definisce una funzione while_loop che prende il numero di iterazioni da effettuare

# In[21]:

def while_loop(iterations, step, numbers):
    if iterations <= 0: #il numero di iterazioni dev'essere >= 0
        print "The number of iterations given is zero or negative. Impossible to end the cicle. Cicle aborted."
    elif iterations != 0: #se il numero di iterazioni è minore o uguale a zero non fa nulla (anche se step = 0)
        iterations = iterations * step #decrementa iterations in quanto il contatore parte da 0
        i = 0 #inizializza il contatore del ciclo
        if step == 0:
            print "The step given is zero. Impossible to end the cicle. Cicle aborted."
        if step > 0:
            while i < iterations:
                print "At the top i is %d" % i
                numbers.append(i) #appende alla lista un elemento contenente il valore corrente del contatore del ciclo

                i += step    
                print "Numbers now: ", numbers
                print "At the bottom i is %d" % i
                print
        if step < 0:
            while i > iterations:
                print "At the top i is %d" % i
                numbers.append(i) #appende alla lista un elemento contenente il valore corrente del contatore del ciclo

                i += step    
                print "Numbers now: ", numbers
                print "At the bottom i is %d" % i
                print
        return numbers


# ##Istruzioni

# In[22]:

numbers = while_loop(5, -20, numbers)


# In[23]:

print "The numbers: "


# In[24]:

for num in numbers:
    print num


# In[ ]:




# In[ ]:



