#Genetic Algorithm - Example 1
import math
import random

inhabitat = []
pop_size = 50
gen_len = 22
xmin = -1
xmax = 3
pc = 0.25
pm = 0.01

def eq(x) :
	return round(x*math.sin(10 * math.pi * x) + 1.0, 6)

def f(x):
	return f(findx(f2t10(x)))

def findx(dec):
	return xmin + dec*(xmax/(math.pow(2, gen_len) - 1))
	
def f2t10(bin):
	return int(bin, 2)
	
def init():
	for i in xrange(3):
		g = ''
		for j in xrange(gen_len):
			g += '1' if random.random() < .5 else '0'
		inhabitat.append(g)
	return 0
	
def di_truyen(x1, x2):
	pos = random.randint(1,gen_len - 2)
	y1 = "%s%s" %(x1[:pos],x2[pos:])
	y2 = "%s%s" %(x2[:pos],x1[pos:])
	return y1, y2
	
def dot_bien(x1):
	pos = random.randint(1,gen_len - 2)
	print pos
	y1 = "%s%s%s" % (x1[:pos],'1' if x1[pos] == '0' else '0',x1[pos + 1:])
	return y1
	
def display():
	for i in xrange(len(inhabitat)):
		print "%02d = %s => f(x) = %s" % (i, inhabitat[i], str(f(inhabitat[i])))

def display_max(gen):
	max = 0
	max_i = 0
	for i in xrange(len(inhabitat)):
		val = f(inhabitat[i])
		max = val if val > max else max
		max_i = i if val > max else max_i
	print "%03d: %s  => f(x) = %s" % (gen, inhabitat[max_i], max)
	
def discard_fail(ar):
	return sorted(ar, key=f)[-pop_size:]
	
init()
#display()
display_max(0)
#y1, y2 = di_truyen(inhabitat[0], inhabitat[1])
#print "x1 = %s\nx2 = %s\ny1 = %s\ny2 = %s" %(inhabitat[0], inhabitat[1], y1, y2)
#y1 = dot_bien(inhabitat[0])
#print "x1 = %s\ny1 = %s" %(inhabitat[0], y1)
for k in xrange(1, 500):
	x1 = ''
	x2 = ''
	for i in xrange(len(inhabitat)):
		if (random.random() < pc):
			if (x1 == ''):
				x1 = inhabitat[i]
			else:
				x2 = inhabitat[i]
			if (x1 != '' and x2 != ''):
				y1, y2 = di_truyen(x1, x2)
				if (y1 not in inhabitat):
					inhabitat.append(y1)
				if (y2 not in inhabitat):
					inhabitat.append(y2)
				print "DI_TRUYEN: =======\nx1 = %s\nx2 = %s\ny1 = %s => f(y1) = %s\ny2 = %s => f(y2) = %s" %(x1, x2, y1, f(y1), y2, f(y2))
				x1 = ''
				x2 = ''
				print x1
				print x2
		inhabitat = discard_fail(inhabitat)
		if (random.random() < pm):
			y1 = dot_bien(inhabitat[i])
			if (y1 not in inhabitat):
				inhabitat.append(y1)
			print "DOT_BIEN: =======\nx1 = %s\ny1 = %s" %(inhabitat[i], y1)
		inhabitat = discard_fail(inhabitat)
			
	display_max(k)
	display()
	print len(inhabitat)