def isPrime(num: int) -> bool:
	if(num == 1):
		return False
	for i in range(2,int(num**0.5) + 1):
		if not(num%i):
			#print(num,"is devied by",i)
			return False
	#print(num,"is prime")
	return True

def isPrimeday(day: int) -> bool:
	i = 10
	while day//i:
		if(isPrime(day%i)):
			i = i * 10
		else:
			#print(day,'is not prime')
			return False
	if(not isPrime(day)):
		return False

	return True


def isDate(day: int) -> bool:
	if day%100 > 31 or day%100 < 0:
		return False
	if (day%10000)//100 > 12 or (day%10000)//100 < 1:
		return False
	if (day%10000 == 230 or day%10000 == 231 or day%10000 == 431 or day%10000 == 631 or day%10000 == 931 or day%10000 == 1131):
		return False
	return True

if(__name__ == '__main__'):
	for i in range(10000,21191232):
	#for i in range(20190523, 20200000):
		if isDate(i):
			if isPrimeday(i):
				print(i,"++++++++++++++is primeday!++++++++++++++")
				#isPrimedayProof(i)
else:
	print("not imported")