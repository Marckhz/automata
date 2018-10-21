import re

""" Marco Hernandez 4-1 """

def myautomata():


	print("Hola por favor introduce  solo symbolos de 'a' , 'b' y 'c '")
	cadena = input("introduce tu cadena por favor : ")
	

	#alphabet = "a,b,c"
	if not re.match("^[a-b-c]*$", cadena):
		print("error solo a,b y c estan permitidos")
		return None

	r1 = re.compile(r"ca$")
	r2 = re.compile(r"^a")

	
	if r1.search(cadena):
		print("valid")

	elif r2.search(cadena):
		print("valido")
	else:
		print("inValido")
if __name__ == '__main__':
	myautomata()
