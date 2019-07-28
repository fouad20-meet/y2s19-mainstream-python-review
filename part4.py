# Part 4 of the Python Review
def isPrime(x):
	for i in range(2,x/2):
		if x/i:
			return False
	return True
class Cipher:

	def __init__(self, secret_message, key, limit,coded_message):
		self.limit = 10000
		if secret_message>1 and key>1:
			if isPrime(secret_message) and isPrime(key):
				if(secret_message + key < limit):
					self.secret_message = secret_message
					self.key = key
				else:
					print("Invalid input: Keys and messages must be at most the limit, which is "+limit+".")
			else:
				print("Invalid input: Both key and message must be prime.")
		else:
			print("Invalid input: Keys and messages must be greater than one.")
		
		
	def encode(self):
		self.coded_message = self.key * self.secret_message


class Decoder:

	def __init__(self, coded_message, limit):
		self.coded_message = coded_message
		self.limit = limit

	def decode(self):
		for i in range(2,coded_message/2):
			if(isPrime(i)):
				if(coded_message%i==0):
					for j in range(2,coded_message/i/2):
						if (coded_message/i)%j:
							break
					return (i,coded_message/i)
			else:
				i += 1
