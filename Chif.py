#MMMDCXVIII

def feistel_cipher(N, permutation, left_shift_amount, right_shift_amount, k1, k2):
    # Appliquer la permutation π
    permuted_N = permute(N, permutation)
    
    # Diviser N en deux blocs de 4 bits
    G0 = permuted_N[:4]
    D0 = permuted_N[4:]
    
    # Premier Round
    D1 = xor(permute(G0, [2, 0, 1, 3]), k1)
    G1 = xor(D0, or_operation(G0, k1))
    
    # Deuxième Round
    D2 = xor(permute(G1, [2, 0, 1, 3]), k2)
    G2 = xor(D1, or_operation(G1, k2))
    
    # Concaténation des résultats
    C = G2 + D2
    
    # Appliquer l'inverse de la permutation π^(-1)
    encrypted_text = permute(C, inverse_permutation(permutation))
    
    return encrypted_text

def permute(block, permutation):
    # Appliquer la permutation à un bloc
    permuted_block = [block[i] for i in permutation]
    
    return permuted_block

def xor(block1, block2):
    # Appliquer l'opération XOR entre deux blocs
    result = [bit1 ^ bit2 for bit1, bit2 in zip(block1, block2)]
    
    return result

def or_operation(block1, block2):
    # Appliquer l'opération OR entre deux blocs
    result = [bit1 | bit2 for bit1, bit2 in zip(block1, block2)]
    
    return result

def inverse_permutation(permutation):
    # Calculer l'inverse d'une permutation
    inverse = [0] * len(permutation)
    for i, j in enumerate(permutation):
        inverse[j] = i
    
    return inverse

# Interaction avec l'utilisateur pour obtenir les données d'entrée
N = input("Entrez le bloc N binaire de longueur 8 : ")
N = [int(bit) for bit in N]  # Convertir le bloc N en une liste d'entiers

permutation = input("Entrez la permutation de longueur 8 (indices séparés par des espaces) : ")
permutation = [int(index) for index in permutation.split()]  # Convertir la permutation en une liste d'entiers

left_shift_amount = int(input("Entrez l'ordre du décalage à gauche : "))
right_shift_amount = int(input("Entrez l'ordre du décalage à droite : "))

k1 = input("Entrez la sous-clé k1 binaire de longueur 4 : ")
k1 = [int(bit) for bit in k1]  # Convertir la sous-clé k1 en une liste d'entiers

k2 = input("Entrez la sous-clé k2 binaire de longueur 4 : ")
k2 = [int(bit) for bit in k2]  # Convertir la sous-clé k2 en une liste d'entiers

# Chiffrement de Feistel
encrypted_text = feistel_cipher(N, permutation, left_shift_amount, right_shift_amount, k1, k2)

# Affichage du texte chiffré
print("Le texte chiffré est :", encrypted_text)

