def listes(elements):
    if all(isinstance(e, (int, float)) for e in elements):
        return sum(elements)
    else:
        return "erreur : La liste contient des elements non numeriques"

 
elements = [1, 2, 3, 4, 5]
print(listes(elements)) 
elements = [1, 2, "a", 4, 5]   
print(listes(elements)) 

