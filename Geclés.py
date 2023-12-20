#MMMDCXVIII

def generate_subkeys(key, permutation, left_shift, right_shift):
    # Appliquer la fonction de permutation
    permuted_key = permute(key, permutation)
    
    # Diviser la clé en deux blocs de 4 bits
    k1 = permuted_key[:4]
    k2 = permuted_key[4:]
    
    # Appliquer les opérations XOR et AND entre les blocs de clé
    k1 = xor(k1, k2)
    k2 = and_operation(k2, k1)
    
    # Appliquer les décalages à gauche et à droite
    k1 = left_shift(k1, 2)
    k2 = right_shift(k2, 1)
    
    return k1, k2

def permute(key, permutation):
    # Appliquer la permutation à la clé
    permuted_key = [key[i] for i in permutation]
    
    return permuted_key

def xor(block1, block2):
    # Appliquer l'opération XOR entre deux blocs
    result = [bit1 ^ bit2 for bit1, bit2 in zip(block1, block2)]
    
    return result

def and_operation(block1, block2):
    # Appliquer l'opération AND entre deux blocs
    result = [bit1 & bit2 for bit1, bit2 in zip(block1, block2)]
    
    return result

def left_shift(block, shift_amount):
    # Effectuer un décalage à gauche sur un bloc de bits
    shifted_block = block[shift_amount:] + block[:shift_amount]
    
    return shifted_block

def right_shift(block, shift_amount):
    # Effectuer un décalage à droite sur un bloc de bits
    shifted_block = block[-shift_amount:] + block[:-shift_amount]
    
    return shifted_block

# Interaction avec l'utilisateur pour obtenir les données d'entrée
key = input("Entrez la clé binaire de longueur 8 : ")
key = [int(bit) for bit in key]  # Convertir la clé en une liste d'entiers

permutation = input("Entrez la permutation de longueur 8 (indices séparés par des espaces) : ")
permutation = [int(index) for index in permutation.split()]  # Convertir la permutation en une liste d'entiers

left_shift_amount = int(input("Entrez l'ordre du décalage à gauche : "))
right_shift_amount = int(input("Entrez l'ordre du décalage à droite : "))

# Génération des sous-clés
k1, k2 = generate_subkeys(key, permutation, left_shift, right_shift)

# Affichage des résultats
print(f"k1: {k1}")
print(f"k2: {k2}")
