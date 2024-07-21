import var
import verification

choix_1 = choix_2 = choix_3 = choix_4 = choix_5 = choix_6 = choix_7 = choix_8 = choix_9 = ' '

def remplir_humain (case) :
    global case_
    global case_r
    case_ = 'remplie'
    case_r = '0'
    
def remplir_ordi (case) :
    global case_
    global case_r
    case_ = 'remplie-ordi'
    case_r = 'X'
    
def entrer_humain () :
    choix = int (input ('joueur-1 : '))
    global choix_1
    global choix_2
    global choix_3
    global choix_4
    global choix_5
    global choix_6
    global choix_7
    global choix_8
    global choix_9
    if choix == 1 :
        if choix_1 == ' ' :
            remplir_humain (var.case_1)
            var.case_1 = case_
            var.x_1 = case_r
            choix_1 = "pris"

        else :
            entrer_humain ()
        
    elif choix == 2 :
        if choix_2 == " " :
            remplir_humain (var.case_2)
            var.case_2 = case_
            var.x_2 = case_r
            choix_2 = "pris"
       
        else :
            entrer_humain ()
        
    elif choix == 3 :
        if choix_3 == " " :
            remplir_humain (var.case_3)
            var.case_3 = case_
            var.x_3 = case_r
            choix_2 = "pris"
       
        else :
            entrer_humain ()
        
    elif choix == 4 :
        if choix_4 == " " :
            remplir_humain (var.case_4)
            var.case_4 = case_
            var.x_4 = case_r
            choix_4 = "pris"
       
        else :
            entrer_humain ()
        
    elif choix == 5 :
        if choix_5 == " " :
            remplir_humain (var.case_5)
            var.case_5 = case_
            var.x_5 = case_r
            choix_5 = "pris"
        else :
            entrer_humain ()

    elif choix == 6 :
        if choix_6 == ' ' :
            remplir_humain (var.case_6)
            var.case_6 = case_
            var.x_6 = case_r
            choix_6 = 'pris'
        else :
            entrer_humain ()

    elif choix == 7 :
        if choix_7 == ' ' :
            remplir_humain (var.case_7)
            var.case_7 = case_
            var.x_7 = case_r
            choix_7 = 'pris'

        else :
            entrer_humain ()

    elif choix == 8 :
        if choix_8 == ' ' :
            remplir_humain (var.case_8)
            var.case_8 = case_
            var.x_8 = case_r
            choix_8 = 'pris'
        
        else :
            entrer_humain ()

    elif choix == 9 :
        if choix_9 == ' ' :
            remplir_humain (var.case_9)
            var.case_9 = case_
            var.x_9 = case_r
            choix_9 = 'pris'
        
        else :
            entrer_humain ()    
    
    else :
        entrer_humain ()

def entrer_ordi () :
    choix = int (input ('joueur-2 : '))
    global choix_1
    global choix_2
    global choix_3
    global choix_4
    global choix_5
    global choix_6
    global choix_7
    global choix_8
    global choix_9

    if choix == 1 :
        if choix_1 == ' ' :
            remplir_ordi (var.case_1)
            var.case_1 = case_
            var.x_1 = case_r
            choix_1 = "pris"
      
        else :
            entrer_ordi ()
        
    elif choix == 2 :
        if choix_2 == " " :
            remplir_ordi (var.case_2)
            var.case_2 = case_
            var.x_2 = case_r
            choix_2 = "pris"
      
        else :
            entrer_ordi ()

        
    elif choix == 3 :
        if choix_3 == " " :
            remplir_ordi (var.case_3)
            var.case_3 = case_
            var.x_3 = case_r
            choix_2 = "pris"
      
        else :
            entrer_ordi ()
        
        
    elif choix == 4 :
        if choix_4 == " " :
            remplir_ordi (var.case_4)
            var.case_4 = case_
            var.x_4 = case_r
            choix_4 = "pris"
      
        else :
            entrer_ordi ()
        
    elif choix == 5 :
        if choix_5 == " " :
            remplir_ordi (var.case_5)
            var.case_5 = case_
            var.x_5 = case_r
            choix_5 = "pris"
      
        else :
            entrer_ordi ()

    elif choix == 6 :
        if choix_6 == ' ' :
            remplir_ordi (var.case_6)
            var.case_6 = case_
            var.x_6 = case_r
            choix_6 = 'pris'
      
        else :
            entrer_ordi ()

    elif choix == 7 :
        if choix_7 == ' ' :
            remplir_ordi (var.case_7)
            var.case_7 = case_
            var.x_7 = case_r
            choix_7 = 'pris'
      
        else :
            entrer_ordi ()

    elif choix == 8 :
        if choix_8 == ' ' :
            remplir_ordi (var.case_8)
            var.case_8 = case_
            var.x_8 = case_r
            choix_8 = 'pris'
      
        else :
            entrer_ordi ()

    elif choix == 9 :
        if choix_9 == ' ' :
            remplir_ordi (var.case_9)
            var.case_9 = case_
            var.x_9 = case_r
            choix_9 = 'pris'
      
        else :
            entrer_ordi ()

    else : 
        entrer_ordi ()
        
def entrer_choix_humain () :
    x = 1
    while x != 10 :
        print ("Tour n." + str(x))
        entrer_humain ()
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