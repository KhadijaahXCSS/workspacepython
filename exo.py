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
		return "Erreur d'operation"