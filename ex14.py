from sys import argv

script, user_name, user_sex = argv
vvod = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(vvod)

print "Where do you live %s?" % user_name
lives = raw_input(vvod)

print "What kind of computer do you have?"
computer = raw_input(vvod)

print """
Alright, so you said %r about liking me.
Your user_sex is %r.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, user_sex, lives, computer)
