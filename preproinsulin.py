"""
Your module description
"""

import re

# Ouvrir le fichier original
with open("preproinsulin-seq.txt", "r") as file:
    data = file.read()

# Supprimer ORIGIN
data = data.replace("ORIGIN", "")

# Supprimer //
data = data.replace("//", "")

# Supprimer tous les chiffres (1, 61, etc.)
data = re.sub(r"[0-9]", "", data)

# Supprimer espaces
data = data.replace(" ", "")

# Supprimer retours à la ligne
data = data.replace("\n", "")

# Mettre en minuscules
data = data.lower()

# Sauvegarder la séquence propre
with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(data)

# Vérifier la longueur
print("Longueur finale :", len(data))
