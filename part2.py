# Part 2 of the Python Review lab.
def isPrime(z):
	for i in range(2,z/2):
		if z%i==0:
			return False
	return True
def encode(x, y):
	for i in range(2,250):
		if 1<y<250:
			if not(isPrime(y)):
				y += 1
			else:
				break
	else:
		print("Invalid input: Outside range.")
		return None
	for i in range(500,1000):
		if 500<x<1000:
			if not(isPrime(x)):
				x += 1
			else:
				break
	else:
		print("Invalid input: Outside range.")
		return None
	return x*y

def decode(coded_message):
		for i in range(2,coded_message/2):
			if(isPrime(i)):
				if(coded_message%i==0):
					for j in range(2,coded_message/i/2):
						if (coded_message/i)%j:
							break
					return (i,coded_message/i)
			else:
				i += 1

print(decode(encode(700,6)))

