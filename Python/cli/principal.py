import calculatrice as cal
import liste
import presentation as pres

def recommencer () :

    # presente les actions a choisir de l'utiliateur :
    pres.action ()
    
    # 1. Calculs basiques :
    if pres.choix == 1 :
        cal.calculatrice_globale ()
        choix = input (cal.un_ou_deux)
        
        # 1. Entrer des chiffres concecutifs :
        if choix == '1' :
            cal.action_1 ()
        
        # 2. Entrer des chiffres 1 par 1 :
        elif choix == '2' :
            a = int (input ('a = '))
            cal.action_2 (a)
        
        # Si jamais c'est autre que 1 ou 2, on redemande*** :
        else :
            choix_1_recommencer ()

    # 2. Ranger une liste :
    elif pres.choix == 2 :
        liste.arranger ()

    # Si jamais l'utilisateur entre autre chose :
    else :
        print ("On recommence : ")
        recommencer ()

    print ("\nService termine. Continuer ?")
    grand_choix = int (input ("1. oui ou 2. non : "))
        
    if grand_choix == 1 :
        recommencer ()
    
    else :
        print ("Merci de m'avoir utilise.")


# Pour le calcul, si l'utilisateur ne tape ni 1 ni 2, on recommence :
# ***redemande : 
def choix_1_recommencer () :
    
    # presentation :
    cal.calculatrice_globale ()
    
    # choix :
    choix = input (cal.un_ou_deux)
    
    if choix == '1' :
        cal.action_1 ()
    
    elif choix == '2' :
        a = int (input ('a = '))
        cal.action_2 (a)
    
    else :
        choix_1_recommencer ()


# presentation gloabale de tout :
pres.presentation ()
recommencer ()