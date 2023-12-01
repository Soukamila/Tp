p=input("Entrer une phrase")
n=len(p)

li=[]
for i in range (0,n):
    if p[i]=="a" : 
        li.append(i)
print("La liste est :",li,"On compte toujours les espaces")#Pas d'interdiction dans l'enonce
        

