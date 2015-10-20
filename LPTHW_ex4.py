#assegna a cars l'integer 100
cars = 100
#assegna a space_in_a_car il floating point 4.0
space_in_a_car = 4.0
#assegna alla variabile drivers l'integer 30
drivers = 30
#assegna alla variabile passengers l'intero 90
passengers = 90
#assegna alla variabile cars_not_driven la variabile cars-drivers. E' una variabile ottenuta a partire da altre due variabili: le macchine non guidate saranno quelle totali meno il numero di autisti
cars_not_driven = cars- drivers
#assegna alla variabile cars_driven la variabile drivers. E' una variabile ottenuta a partire da altre due variabili: le macchine non guidate saranno pari agli autisti
cars_driven = drivers
#assegna a carpool_capacity la variabile cars_driven*space in a car. Vedi sopra
carpool_capacity = cars_driven*space_in_a_car
#siccome average_passengers_per_car è ottenuta da una divisione, è necessario essa sia una variabile di tipo floating point. Per questo la variabile passengers è assegnata a un valore floating point
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
