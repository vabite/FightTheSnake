#LPTHW_ex11.py
print "How old are you?",
#raw_input documentation: 
#Raw_input([prompt]). If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy." %(age, height, weight)

print
print
print

#LPTHW_ex12.py
print "ESERCITAZIONE"
age = raw_input("How old are you? ")
weight = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you are %r old, %r tall and %r heavy." %(age, height, weight)
