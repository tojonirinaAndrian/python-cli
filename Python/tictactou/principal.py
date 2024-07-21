import fonction_principale as fp
import fonction_principale_ordi as fpo
import var
import verification as ver

print ("C'est le jeu TIC-TAC-TOU !")
print ("1. Etes-vous 2 joueurs ou \n2. voulez-vous jouer seul contre l'ordinateur ?")

choix_principal = int (input (": "))

print ("\nAllons-y !!!\nVoici le terrain de jeu :")

var.affichage (var.x_1, var.x_2, var.x_3, var.x_4, var.x_5, var.x_6, var.x_7, var.x_8, var.x_9)

if choix_principal == 1 :
    fp.entrer_choix_humain ()

if choix_principal == 2 :
    ver.joueur2 = 'L ordinateur'
    fpo.entrer_choix_ordi ()

print ("Merci d'avoir joue.")