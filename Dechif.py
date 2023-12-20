#MULAMBA KOBUA CALEB

def feistel_decipher(ciphertext, permutation, p_permutation, k1, k2):
    # Appliquer la permutation initiale
    permuted_ciphertext = permute(ciphertext, permutation)
    
    # Diviser le bloc en deux sous-blocs de 4 bits
    g2 = permuted_ciphertext[:4]
    d2 = permuted_ciphertext[4:]
    
    # Premier round
    g1 = xor(p_permute(d2, p_permutation), k2)
    d1 = xor(g2, or_operation(g1, k2))
    
    # Deuxième round
    g0 = xor(p_permute(d1, p_permutation), k1)
    d0 = xor(g1, or_operation(g0, k1))
    
    # Concaténer les sous-blocs
    plaintext = g0 + d0
    
    # Appliquer l'inverse de la permutation initiale
    plaintext = permute(plaintext, inverse_permutation(permutation))
    
    return plaintext

# Interaction avec l'utilisateur pour obtenir les données d'entrée
ciphertext = input("Entrez le texte chiffré binaire de longueur 8 : ")
ciphertext = [int(bit) for bit in ciphertext]  # Convertir le texte chiffré en une liste d'entiers

permutation = input("Entrez la permutation de longueur 8 (indices séparés par des espaces) : ")
permutation = [int(index) for index in permutation.split()]  # Convertir la permutation en une liste d'entiers

p_permutation = [2, 0, 1, 3]  # Permutation P

k1 = input("Entrez la sous-clé k1 de longueur 4 : ")
k1 = [int(bit) for bit in k1]  # Convertir la sous-clé en une liste d'entiers

k2 = input("Entrez la sous-clé k2 de longueur 4 : ")
k2 = [int(bit) for bit in k2]  # Convertir la sous-clé en une liste d'entiers

# Déchiffrement de Feistel
plaintext = feistel_decipher(ciphertext, permutation, p_permutation, k1, k2)

# Affichage du texte clair
print(f"Texte clair : {plaintext}")
