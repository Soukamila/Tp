p=input("Entrer une phrase")
n=len(p)
s=0
for i in range (0,n):
    if p[i]=="a" or p[i]== "A":
        s=s+i
print("la somme est: ",s, "\n" "Ce code compte aussi les espaces")#Aucune restriction dans l'enonce
