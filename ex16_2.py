from sys import argv

script, filename = argv

print "Opening the file %r..." % filename
target = open(filename, 'r')
print target.read()
