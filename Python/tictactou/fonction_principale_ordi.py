import fonction_principale as fp
import var
import verification
import random 

def entrer_ordi () :
    choix = random.randint (1, 9)
    
    if choix == 1 :
        if fp.choix_1 == ' ' :
            fp.remplir_ordi (var.case_1)
            var.case_1 = fp.case_
            var.x_1 = fp.case_r
            fp.choix_1 = "pris"
    
        else :
            entrer_ordi ()
        
    elif choix == 2 :
        if fp.choix_2 == " " :
            fp.remplir_ordi (var.case_2)
            var.case_2 = fp.case_
            var.x_2 = fp.case_r
            fp.choix_2 = "pris"
    
        else :
            entrer_ordi ()

        
    elif choix == 3 :
        if fp.choix_3 == " " :
            fp.remplir_ordi (var.case_3)
            var.case_3 = fp.case_
            var.x_3 = fp.case_r
            fp.choix_2 = "pris"
    
        else :
            entrer_ordi ()
        
        
    elif choix == 4 :
        if fp.choix_4 == " " :
            fp.remplir_ordi (var.case_4)
            var.case_4 = fp.case_
            var.x_4 = fp.case_r
            fp.choix_4 = "pris"
    
        else :
            entrer_ordi ()
        
    elif choix == 5 :
        if fp.choix_5 == " " :
            fp.remplir_ordi (var.case_5)
            var.case_5 = fp.case_
            var.x_5 = fp.case_r
            fp.choix_5 = "pris"
    
        else :
            entrer_ordi ()

    elif choix == 6 :
        if fp.choix_6 == ' ' :
            fp.remplir_ordi (var.case_6)
            var.case_6 = fp.case_
            var.x_6 = fp.case_r
            fp.choix_6 = 'pris'
    
        else :
            entrer_ordi ()

    elif choix == 7 :
        if fp.choix_7 == ' ' :
            fp.remplir_ordi (var.case_7)
            var.case_7 = fp.case_
            var.x_7 = fp.case_r
            fp.choix_7 = 'pris'
    
        else :
            entrer_ordi ()

    elif choix == 8 :
        if fp.choix_8 == ' ' :
            fp.remplir_ordi (var.case_8)
            var.case_8 = fp.case_
            var.x_8 = fp.case_r
            fp.choix_8 = 'pris'
    
        else :
            entrer_ordi ()

    elif choix == 9 :
        if fp.choix_9 == ' ' :
            fp.remplir_ordi (var.case_9)
            var.case_9 = fp.case_
            var.x_9 = fp.case_r
            fp.choix_9 = 'pris'
    
        else :
            entrer_ordi ()

def entrer_choix_ordi () :
    x = 1
    while x != 10 :
        print ("Tour n." + str(x))
        fp.entrer_humain ()
        var.affirmation (var.x_1, var.x_2, var.x_3, var.x_4, var.x_5, var.x_6, var.x_7, var.x_8, var.x_9, var.case_1, var.case_2, var.case_3, var.case_4, var.case_5, var.case_6, var.case_7, var.case_8, var.case_9)

        var.affichage (var.x_1, var.x_2, var.x_3, var.x_4, var.x_5, var.x_6, var.x_7, var.x_8, var.x_9)
        
        verification.verification ()
        if verification.over == 'oui' :
            break

        x += 1
        
        if x == 10 : 
            break
        
        print ("Tour n." + str(x))
        entrer_ordi ()
        var.affirmation (var.x_1, var.x_2, var.x_3, var.x_4, var.x_5, var.x_6, var.x_7, var.x_8, var.x_9, var.case_1, var.case_2, var.case_3, var.case_4, var.case_5, var.case_6, var.case_7, var.case_8, var.case_9)
        
        var.affichage (var.x_1, var.x_2, var.x_3, var.x_4, var.x_5, var.x_6, var.x_7, var.x_8, var.x_9)    

        verification.verification_2 ()
        if verification.over == 'oui' :
            break

        x += 1