



def calculMoyenne(listeNote):
    additionNote = 0
    for i in range(len(listeNote)):
        additionNote = additionNote + listeNote[i]
    
    moyenne = additionNote / len(listeNote)
    return moyenne
 
listeNote1=[12,20,7,15]   
print(calculMoyenne(listeNote1))