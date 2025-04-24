
def calcul(a, b, operation):
	
	if operation == "addition":
		return a + b
	elif operation == "soustraction":
		return a - b
	elif operation == "multiplication":
		return a * b
	elif operation == "division":
		if b != 0:
			return a / b
		else:
			return "Erreur"

	else:
		return "Operation non valide"
	
operation = input("Entrez l'opération : ")
a = float(input("Entrez le premier nombre : "))				
b = float(input("Entrez le deuxième nombre : "))
resultat = calcul(a, b, operation)
print("Le résultat est :", resultat)