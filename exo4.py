def nombres_pairs(n):
    if isinstance(n, int) and n > 0:
        return [i for i in range(2, n + 1, 2)]
    else:
        return "Erreur : Le parametre doit etre un entier positif."

print(nombres_pairs(10))   
print(nombres_pairs(-5))   
print(nombres_pairs("dix"))  
