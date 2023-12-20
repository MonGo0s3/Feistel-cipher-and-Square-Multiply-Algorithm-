#MMMDCXVIII

def square_and_multiply(x, b, n):
    # Conversion de l'exposant b en binaire
    binary_b = bin(b)[2:]
    
    # Initialisation
    result = 1
    power = x % n
    
    # Parcours des bits de l'exposant de gauche à droite
    for bit in binary_b[::-1]:
        if bit == '1':
            result = (result * power) % n
        power = (power * power) % n
    
    return result

# Interaction avec l'utilisateur pour obtenir les valeurs de x, b et n
x = int(input("Entrez la valeur de x : "))
b = int(input("Entrez la valeur de b : "))
n = int(input("Entrez la valeur de n : "))

# Calcul de x^b modulo n en utilisant l'algorithme des carrés et des multiplications
result = square_and_multiply(x, b, n)

# Affichage du résultat
print(f"Le résultat de {x}^{b} (mod {n}) est : {result}")


