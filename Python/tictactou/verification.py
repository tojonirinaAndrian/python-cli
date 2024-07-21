import var
joueur2 = 'Joueur 2'
over = ' '

def verification () :
    global over
    if var.x_1 == '0' and var.x_2 == '0' and var.x_3 == '0' :
        print ("Game Over. Joueur1 gagne.")
        over = 'oui'
    
    if var.x_1 == '0' and var.x_5 == '0' and var.x_9 == '0' :
        print ("Game Over. Joueur1 gagne.")
        over = 'oui'
    
    if var.x_1 == '0' and var.x_4 == '0' and var.x_7 == '0' :
        print ("Game Over. Joueur1 gagne.")
        over = 'oui'
    
    if var.x_2 == '0' and var.x_5 == '0' and var.x_8 == '0' :
        print ("Game Over. Joueur1 gagne.")
        over = 'oui'
    
    if var.x_3 == '0' and var.x_5 == '0' and var.x_7 == '0' :
        print ("Game Over. Joueur1 gagne.")
        over = 'oui'
    
    if var.x_3 == '0' and var.x_6 == '0' and var.x_9 == '0' :
        print ("Game Over. Joueur1 gagne.")
        over = 'oui'
    
    if var.x_4 == '0' and var.x_5 == '0' and var.x_6 == '0' :
        print ("Game Over. Joueur1 gagne.")
        over = 'oui'
    
    if var.x_7 == '0' and var.x_8 == '0' and var.x_9 == '0' :
        print ("Game Over. Joueur1 gagne.")
        over = 'oui'

def verification_2 () :
    global over
    if var.x_1 == 'X' and var.x_2 == 'X' and var.x_3 == 'X' :
        print ("Game Over. " + joueur2 + " gagne.")
        over = 'oui'
    
    if var.x_1 == 'X' and var.x_5 == 'X' and var.x_9 == '' :
        print ("Game Over. " + joueur2 + " gagne.")
        over = 'oui'
    
    if var.x_1 == 'X' and var.x_4 == 'X' and var.x_7 == 'X' :
        print ("Game Over. " + joueur2 + " gagne.")
        over = 'oui'
    
    if var.x_2 == 'X' and var.x_5 == 'X' and var.x_8 == 'X' :
        print ("Game Over. " + joueur2 + " gagne.")
        over = 'oui'
    
    if var.x_3 == 'X' and var.x_5 == 'X' and var.x_7 == 'X' :
        print ("Game Over. " + joueur2 + " gagne.")
        over = 'oui'
    
    if var.x_3 == 'X' and var.x_6 == 'X' and var.x_9 == 'X' :
        print ("Game Over. " + joueur2 + " gagne.")
        over = 'oui'
    
    if var.x_4 == 'X' and var.x_5 == 'X' and var.x_6 == 'X' :
        print ("Game Over. " + joueur2 + " gagne.")
        over = 'oui'
    
    if var.x_7 == 'X' and var.x_8 == 'X' and var.x_9 == 'X' :
        print ("Game Over. " + joueur2 + " gagne.")
        over = 'oui'