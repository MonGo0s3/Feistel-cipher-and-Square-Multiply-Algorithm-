#MMMDCXVIII
 
def feistel_decipher(C, permutation, left_shift_amount, right_shift_amount, k1, k2):
    # Appliquer la permutation π
    permuted_C = permute(C, permutation)

    # Diviser C en deux blocs de 4 bits
    G2 = permuted_C[:4]
    D2 = permuted_C[4:]

    # Premier Round
    G1 = xor(inverse_permute(D2, [2, 0, 1, 3]), k2)
    D1 = xor(G2, or_operation(G1, k2))

    # Deuxième Round
    G0 = xor(inverse_permute(D1, [2, 0, 1, 3]), k1)
    D0 = xor(G1, or_operation(G0, k1))

    # Concaténation des résultats
    N = G0 + D0

    # Appliquer l'inverse de la permutation π^(-1)
    decrypted_text = permute(N, inverse_permute(N, permutation))

    return decrypted_text

def permute(block, permutation):
    # Appliquer la permutation à un bloc
    permuted_block = [block[i] for i in permutation]

    return permuted_block

def inverse_permute(block, permutation):
    # Appliquer l'inverse de la permutation à un bloc
    inverse_permuted_block = [0] * len(block)
    for i, j in enumerate(permutation):
        inverse_permuted_block[j] = block[i]

    return inverse_permuted_block

def xor(block1, block2):
    # Appliquer l'opération XOR entre deux blocs
    result = [bit1 ^ bit2 for bit1, bit2 in zip(block1, block2)]

    return result

def or_operation(block1, block2):
    # Appliquer l'opération OR entre deux blocs
    result = [bit1 | bit2 for bit1, bit2 in zip(block1, block2)]

    return result

# Interaction avec l'utilisateur pour obtenir les données d'entrée
C = input("Entrez le bloc C binaire de longueur 8 : ")
C = [int(bit) for bit in C]  # Convertir le bloc C en une liste d'entiers

permutation = input("Entrez la permutation de longueur 8 (indices séparés par des espaces) : ")
permutation = [int(index) for index in permutation.split()]  # Convertir la permutation en une liste d'entiers

left_shift_amount = int(input("Entrez l'ordre du décalage à gauche : "))
right_shift_amount = int(input("Entrez l'ordre du décalage à droite : "))

k1 = input("Entrez la sous-clé k1 binaire de longueur 4 : ")
k1 = [int(bit) for bit in k1]  # Convertir la sous-clé k1 en une liste d'entiers

k2 = input("Entrez la sous-clé k2 binaire de longueur 4 : ")
k2 = [int(bit) for bit in k2]  # Convertir la sous-clé k2 en une liste d'entiers

# Déchiffrement de Feistel
decrypted_text = feistel_decipher(C, permutation, left_shift_amount, right_shift_amount, k1, k2)

# Affichage du texte clair
print("Le texte clair est :", decrypted_text)
