chen = input("Entrez une phrase : ")

initiales = ""


for mots in chen.split():
    initiales += mots[0]

print("Les initiales sont :", initiales)
