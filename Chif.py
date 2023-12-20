#MULAMBA KOBUA CALEB

def feistel_cipher(block, permutation, p_permutation, k1, k2):
    # Appliquer la permutation initiale
    permuted_block = permute(block, permutation)
    
    # Diviser le bloc en deux sous-blocs de 4 bits
    g0 = permuted_block[:4]
    d0 = permuted_block[4:]
    
    # Premier round
    d1 = xor(p_permute(g0, p_permutation), k1)
    g1 = xor(d0, or_operation(g0, k1))
    
    # Deuxième round
    d2 = xor(p_permute(g1, p_permutation), k2)
    g2 = xor(d1, or_operation(g1, k2))
    
    # Concaténer les sous-blocs
    ciphertext = g2 + d2
    
    # Appliquer l'inverse de la permutation initiale
    ciphertext = permute(ciphertext, inverse_permutation(permutation))
    
    return ciphertext

def permute(block, permutation):
    # Appliquer la permutation à un bloc
    permuted_block = [block[i] for i in permutation]
    
    return permuted_block

def inverse_permutation(permutation):
    # Calculer l'inverse d'une permutation
    inverse = [permutation.index(i) for i in range(len(permutation))]
    
    return inverse

def p_permute(block, p_permutation):
    # Appliquer la permutation P à un bloc
    permuted_block = [block[i] for i in p_permutation]
    
    return permuted_block

def xor(block1, block2):
    # Appliquer l'opération XOR entre deux blocs
    result = [bit1 ^ bit2 for bit1, bit2 in zip(block1, block2)]
    
    return result

def or_operation(block1, block2):
    # Appliquer l'opération OR entre deux blocs
    result = [bit1 | bit2 for bit1, bit2 in zip(block1, block2)]
    
    return result

# Interaction avec l'utilisateur pour obtenir les données d'entrée
block = input("Entrez le bloc binaire de longueur 8 : ")
block = [int(bit) for bit in block]  # Convertir le bloc en une liste d'entiers

permutation = input("Entrez la permutation de longueur 8 (indices séparés par des espaces) : ")
permutation = [int(index) for index in permutation.split()]  # Convertir la permutation en une liste d'entiers

p_permutation = [2, 0, 1, 3]  # Permutation P

k1 = input("Entrez la sous-clé k1 de longueur 4 : ")
k1 = [int(bit) for bit in k1]  # Convertir la sous-clé en une liste d'entiers

k2 = input("Entrez la sous-clé k2 de longueur 4 : ")
k2 = [int(bit) for bit in k2]  # Convertir la sous-clé en une liste d'entiers

# Chiffrement de Feistel
ciphertext = feistel_cipher(block, permutation, p_permutation, k1, k2)

# Affichage du texte chiffré
print(f"Texte chiffré : {ciphertext}")
