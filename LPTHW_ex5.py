my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)


print ""
print ""
print "ESERCIZI"
name = 'Valerio Bitetta'
age_y = 26 #not a lie
height_cm = 175 #cm
weight_kg = 50 #kg
eyes = 'brown'
teeth = 'white-ish'
hair = 'every day fewer'

lb_to_kg = 2.20462262185
inches_to_cm = 0.393700787401575

weight_lb = weight_kg*lb_to_kg
height_inches = height_cm*inches_to_cm

print "Let's talk about %s." % name
print "He's %d inches tall." % height_inches
print "He's %d pounds heavy." % weight_lb
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s, depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age_y, height_cm, weight_kg, age_y + height_cm + weight_kg)
