#inizializza le variabili people, cars e trucks
people = 30
cars = 40
trucks = 15

    #if cars greater than people, then it prints "We should take cars."...
if cars > people:
    print "We should take cars."
    #...if cars lower than people, then it prints "We should not take cars."...
elif cars < people:
    print "We should not take the cars."
    #...else (if cars equals people) it prints "We can't decide."
else:
    print "We can't decide."
    
    #if trucks greater than cars, then it prints "There's too many trucks."...
if trucks > cars:
    print "That's too many trucks."
    #...if trucks lower than cars, then it prints "Maybe we couls take the trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
    #...else (if trucks equals cars) it prints "We still can't decide."
else:
    print "We still can't decide."
    
    #if people greater than trucks, it prints "Let's just take trucks."...
if people > trucks:
    print "Allright, let's just take the trucks."
    #...else (if people lower or equal to trucks) it prints "Fine, let's stay home then."
else:
    print "Fine, let's stay home then."

if people < trucks and people < cars and cars > 0 and trucks > 0 :
    print "We have a lot of vehicles!"
elif people < cars + trucks:
    print "We are not in short of vehicles."
else:
    print "We are in short of vehicles"

  
