name = 'Vasily A. Frolov'
age = 34  # not a lie
height = 176  # cm
weight = 90  # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilograms heavy." % weight
print "Actually thats too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cofee." % teeth

# this linke is tricky, try to get it exactly right
print "If I add %r, %d, and %d I get %d." \
    % (age, height, weight, age + height + weight)
