
def greet_user(name=None):
    
    
    firstname = name if name else input('Entrer votre prénom : ')
    
    #Vérifier si le prénom saisi n'est pas vide
    if firstname:
        print(f"Merci {firstname} ! ")
        
    else:
        print("Vous n'avez pas saisi un prenom valide")
        
greet_user()
