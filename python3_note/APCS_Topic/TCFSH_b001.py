## Question : GCD

## TCFSH b001

## Tool remembered

# Euclidean algorithm

def gcd (a,b):
	if (b==0):
		return a
	else :
		return gcd(b,a%b)
try : 
	while True :
		intlist =list(map(int, input().split(' ')))
		print (gcd(intlist[0],intlist[1]))
except EOFError:
	pass
