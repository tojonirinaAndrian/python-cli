def solde_insuffisant () :
print ("""
Votre solde MVola est insuffisant. Votre solde est de 0 Ar. Faire un depot MVola
suffisant pour pouvoir effectuer cette Transaction. Ref:548582205
""")

def confirmation_payement (nom, prix) = "Pour confirmer le payement de l'offre " + nom + " via MVOLA d'un montant de " + ", Entrer code secret"

def mkozy (choix, code_secret) :
    choix = (input ("""
    M KOZY (VOIX-INTERNET)
    1. M KORAGNA (6000 Ar)
    2. M KAIKY (4000 Ar)
    """))
    
    if choix == "1" :
        code_secret = input ("""
        Offre M KORAGNA : 5 Go d Instagram, Facebook et WhatsApp a seulement
        6000 Ar. Pour confirmer ton achat via MVOLA, entre ton code secret :
        """)
        solde_insuffisant ()
    
    elif choix == "2" :
        code_secret = input ("""
        Offre M Kaiky : 1 Go d internet et 15 mn vers tout operateurs a seulement 4000ar.
        Pour confirmer ton achat via Mvola, entre ton code secret :
        """)
        solde_insuffisant ()  

def page_precedente_telma_mora (choix, code_secret) :
    tableau_mora = ['Mora 500', 'Mora One', 'Mora+ 2000', 'Mora+ 5000', 'Mora Night', 'Mora TEAM', 'Mora Intenational']
    tableau_mora_prix = ['500 Ar', '1000 Ar', '2000 Ar', '5000 Ar', '500 Ar', '1000 Ar', '5000 Ar']
 
    choix = input ("""
        MORA (Voix - SMS - Internet)
        1. Mora 500 (500 Ar)
        2. MORA ONE (1000 Ar)
        3. Mora+ 2000 (2000 Ar)
        4. Mora+ 5000 (5000 Ar)
        5. Mora Night (500 Ar)
        # Page suivante
        """)
        if choix == "#" :
            choix = input ("""
            MORA (Voix - SMS - Internet)
            6. Mora TEAM (1000 Ar)
            7. Mora International (5000 Ar)
            * Page Precedente
            ** Top Menu
            """)
            if choix == "*" or choix == "**" :
                page_precedente_telma_mora (choix, code_secret)
        elif choix = "1" :
            code_secret = input (confirmation_payement (tableau_mora[0], tableau_mora_prix[0]))
            solde_insuffisant ()
        elif choix == '2' :
            code_secret = input ( confirmation_payement (tableau_mora[1], tableau_mora_prix[1]))
            solde_insuffisant ()
        elif choix == '3' :
            code_secret = input ( confirmation_payement (tableau_mora[2], tableau_mora_prix[2])) 
            solde_insuffisant ()
        elif choix == '4' :
            code_secret = input ( confirmation_payement (tableau_mora[3], tableau_mora_prix[3]))
            solde_insuffisant ()
        elif choix == '5' :
            code_secret = input ( confirmation_payement (tableau_mora[4], tableau_mora_prix[4]))
            solde_insuffisant ()
        elif choix == '6' :
            code_secret = input ( confirmation_payement (tableau_mora[5], tableau_mora_prix[5]))
            solde_insuffisant ()
        elif choix == '7' :
            code_secret = input ( confirmation_payement (tableau_mora[6], tableau_mora_prix[6]))
            solde_insuffisant ()
        else :
            page_precedente_telma_mora (choix, code_secret)

def telma_net (choix, code_secret) :
    choix = int (input ("""
    TELMA Net (INTERNET)
    1 Net Journalier
    2 Net Hebdomadaire
    3 Net Mensuel
    4 TELMA Net (INTERNET)
    5 M KOZY (Voix - Internet)
    """))
    if choix = 5 :
        mkozy (choix, code_secret)
    
    elif choix = 1 :
        choix = int (input ("""
        Net Journalier
        1. Telma Net nuit (100 Ar)
        """))

        if choix == 1 :
            code_secret = input ( confirmation_payement ('Telma Net Nuit', '100 Ar'))
            solde_insuffisant ()

        else :
            telma_net (choix, code_secret)
    
    elif choix = 2 :
        choix = int (input ("""
            Net Hebdomadaire
            1. Net One Week 350 Mo (3000 Ar)
            2. Net One Week 800 Mo (5000 Ar)
            3. Net One Week 2 Go (10000 Ar)
        """))

        if choix == 1 :
            code_secret = input ( confirmation_payement ('Net One Week 350 Mo', '3000 Ar'))
            solde_insuffisant ()

        elif choix == 2 :
            code_secret = input ( confirmation_payement ('Net One Week 800 Mo', '5000 Ar'))
            solde_insuffisant ()

        elif choix == 3 :
            code_secret = input ( confirmation_payement ('Net One Week 2 Go', '10000 Ar'))
            solde_insuffisant ()
        
        else :
            offres (choix, code secret)

    elif choix = 3 :
        page_precedente_net_mensuel (choix, code_secret)

    elif choix = 4 :
        telma_net (choix, code_secret)
    
    else : 
        telma_net (choix, code_secret)

def page_precedente_net_mensuel (choix, code_secret) :
    tableau_net_mensuel = ['Net one month 2 Go', 'Net one month 4 Go', 'Net one month 12 Go', 'Net one month 25 Go', 'Net one month 50 Go', 'Net one month 100 Go']
    tableau_net_mensuel_prix = ['15000 Ar', '25000 Ar', '75000 Ar', '125000 Ar', '150000 Ar', '159000 Ar']
    choix = (input ("""NET MENSUEL
        1. """ + tableau_net_mensuel[0] + "(" + tableau_net_mensuel_prix[0] + ")" + """
        2. """ + tableau_net_mensuel[1] + "(" + tableau_net_mensuel_prix[1] + ")" + """
        3. """ + tableau_net_mensuel[2] + "(" + tableau_net_mensuel_prix[2] + ")" + """
        4. """ + tableau_net_mensuel[3] + "(" + tableau_net_mensuel_prix[3] + ")" + """
        5. """ + tableau_net_mensuel[4] + "(" + tableau_net_mensuel_prix[4] + ")" + """
        # Page suivante
        """
        ))
        if choix == "#" :
            choix = (input ("""NET MENSUEL
            6. """ + tableau_net_mensuel[5] + "(" + tableau_net_mensuel_prix[5] + ")" + """
            * Page precedente
            ** Top Menu
            """
            ))
            if choix == "*" or choix == "**" :
                page_precedente_net_mensuel (choix, code_secret)
        if choix = "1" :
            code_secret = input ( confirmation_payement (tableau_net_mensuel[0], tableau_net_mensuel_prix[0]))
            solde_insuffisant ()
        elif choix == '2' :
            code_secret = input ( confirmation_payement (tableau_net_mensuel[1], tableau_net_mensuel_prix[1]))
            solde_insuffisant ()
        elif choix == '3' :
            code_secret = input ( confirmation_payement (tableau_net_mensuel[2], tableau_net_mensuel_prix[2])) 
            solde_insuffisant ()
        elif choix == '4' :
            code_secret = input ( confirmation_payement (tableau_net_mensuel[3], tableau_net_mensuel_prix[3]))
            solde_insuffisant ()
        elif choix == '5' :
            code_secret = input ( confirmation_payement (tableau_net_mensuel[4], tableau_net_mensuel_prix[4]))
            solde_insuffisant ()
        elif choix == '6' :
            code_secret = input ( confirmation_payement (tableau_net_mensuel[5], tableau_net_mensuel_prix[5]))
            solde_insuffisant ()
        else :
            page_precedente_net_mensuel (choix, code_secret)

def page_precedente_yellow (choix, code_secret) :
    tableau_yellow = ['Yellow100', 'Yellow SMS', 'Yellow Facebibaka', 'Yellow 1000', 'YEllow Faceboobaka One', 'Yellow 200', 'Yellow Faceboobaka +', 'Yellow One']
    tableau_yellow_prix = ['100 Ar', '200 Ar', '500 Ar', '1000 Ar', '1000 Ar', '200 Ar', '2000 Ar', '1000 Ar']
    choix = (input ("""Yellow (SMS - Internet)
        1. """ + tableau_yellow[0] + "(" + tableau_yellow_prix[0] + ")" + """
        2. """ + tableau_yellow[1] + "(" + tableau_yellow_prix[1] + ")" + """
        3. """ + tableau_yellow[2] + "(" + tableau_yellow_prix[2] + ")" + """
        4. """ + tableau_yellow[3] + "(" + tableau_yellow_prix[3] + ")" + """
        5. """ + tableau_yellow[4] + "(" + tableau_yellow_prix[4] + ")" + """
        # Page suivante
        """
        ))
        if choix == "#" :
            choix = (input ("""Yellow (SMS - Internet)
            6. """ + tableau_yellow[5] + "(" + tableau_yellow_prix[5] + ")" + """
            7. """ + tableau_yellow[6] + "(" + tableau_yellow_prix[6] + ")" + """
            8. """ + tableau_yellow[7] + "(" + tableau_yellow_prix[7] + ")" + """
            * Page precedente
            ** Top Menu
            """
            ))
            if choix == "*" or choix == "**" :
                page_precedente_yellow (choix, code_secret)
        if choix = "1" :
            code_secret = input (confirmation_payement (tableau_yellow[0], tableau_yellow_prix[0]))
            solde_insuffisant ()
        elif choix == '2' :
            code_secret = input ( confirmation_payement (tableau_yellow[1], tableau_yellow_prix[1]))
            solde_insuffisant ()
        elif choix == '3' :
            code_secret = input ( confirmation_payement (tableau_yellow[2], tableau_yellow_prix[2])) 
            solde_insuffisant ()
        elif choix == '4' :
            code_secret = input ( confirmation_payement (tableau_yellow[3], tableau_yellow_prix[3]))
            solde_insuffisant ()
        elif choix == '5' :
            code_secret = input ( confirmation_payement (tableau_yellow[4], tableau_yellow_prix[4]))
            solde_insuffisant ()
        elif choix == '6' :
            code_secret = input ( confirmation_payement (tableau_yellow[5], tableau_yellow_prix[5]))
            solde_insuffisant ()
        elif choix == '7' :
            code_secret = input ( confirmation_payement (tableau_yellow[6], tableau_yellow_prix[6]))
            solde_insuffisant ()
        elif choix == '8' :
            code_secret = input ( confirmation_payement (tableau_yellow[7], tableau_yellow_prix[7]))
            solde_insuffisant ()
        else :
            page_precedente_yellow (choix, code_secret)        

def offres (choix, code_secret) :
    choix = input ("""
    Votre offre tarifaire actuelle est TOKANA.
    0. M KOZY (VOIX-INTERNET)
    1. MORA (VOIX - SMS - INTERNET)
    2. FIRST (VOIX - SMS - INTERNET)
    3. YELLOW (SMS - INTERNET)
    # Page suivante 
    """)
    if choix == "#" :
        choix = input ("""
        Votre offre actuelle est TOKANA.
        4. TELMA Net (Internet)
        * Page Precedente
        ** Top menu
        """)
        
        if choix == "**" or choix == "*":
            offres (choix, code_secret)
    
    if choix == "0" :
        mkozy (choix, code_secret)
    
    elif choix == "1" :
        page_precedente_telma_mora (choix, code_secret) 
    
    elif choix == "2" :
        tableau_first = ['first Premium', 'First Premium +', 'First Prestige', 'First Royal']
        tableau_first_prix = ['10000 Ar', '15000 Ar', '30000 Ar', '50000 Ar']
        choix = int (input ("""First (VOix - SMS - Internet)
        1.""" + tableau_first[0] + "(" + tableau_first_prix[0] + ")" + """
        2.""" + tableau_first[1] + "(" + tableau_first_prix[1] + ")" + """
        3.""" + tableau_first[2] + "(" + tableau_first_prix[2] + ")" + """
        4.""" + tableau_first[3] + "(" + tableau_first_prix[3] + ")"
        ))
        if choix == 1 :
            confirmation_payement (tableau_first[0], tableau_first_prix[0])
            solde_insuffisant ()   
        elif choix == 2 :
            confirmation_payement (tableau_first[1], tableau_first_prix[1])
            solde_insuffisant ()
        elif choix == 3 :
            confirmation_payement (tableau_first[2], tableau_first_prix[2])
            solde_insuffisant ()
        elif choix == 4 :
            confirmation_payement (tableau_first[3], tableau_first_prix[3])
            solde_insuffisant ()
        else offres (choix, code_secret)
    
    elif choix == "3" :
        page_precedente_yellow (choix, code_secret)
    
    elif choix == "4" :
        telma_net (choix, code_secret)
    
    else : 
        offres (choix, code_secret)

def page_precedente_choisir_montant_souhaite (choix, code_recharge) :
    choix = int (input ("""
    Code Recharge :
    1 Acheter code recharge
    2 Renvoyer dernier achat 
    3 Renvoyer mes Codes Recharges
    """))
    if choix == 1 :
        choix = input ("""
        Choisir montant souhaite
        1 Code Recharge 1000
        2 Code Recharge 2000
        3 Code Recharge 5000
        4 Code Recharge 10000
        5 Code Recharge 15000
        6 Code Recharge 25000
        # Page Suivante
        """)
        if choix == '#' :
            choix = input ("""
            Choisir montant souhaite
            7 Code Recharge 30000
            8 Code Recharge 50000
            * page precedente
            ** Menu principal
            """)
            if choix == '*' :
                page_precedente_choisir_montant_souhaite (choix, code_recharge)

            elif choix == '**' :
                retour_au_menu_principal ()
        if choix == '1' or choix == '2' or choix == '3' or choix == '4' or choix == '5' or choix == '6' or choix == '7' or choix == '8' :
            for x in range 2 :
                code_recharge = input ("Saisir nombre de code recharge souhaite: Entre 1 et 20: \n")
            print ("le nombre d'essais maximum est atteint.")

def page_precedente_choisir_montant_souhaite_autre (choix, code_recharge) :
    choix = input ("""
    Choisir montant souhaite
    1 Code Recharge 1000
    2 Code Recharge 2000
    3 Code Recharge 5000
    4 Code Recharge 10000
    5 Code Recharge 15000
    6 Code Recharge 25000
    # Page Suivante
    """)
    if choix == '#' :
        choix = input ("""
        Choisir montant souhaite
        7 Code Recharge 30000
        8 Code Recharge 50000
        * page precedente
        ** Menu principal
        """)
        if choix == '*' :
            page_precedente_choisir_montant_souhaite_autre (choix, code_recharge)

        elif choix == '**' :
            retour_au_menu_principal ()
    if choix == '1' or choix == '2' or choix == '3' or choix == '4' or choix == '5' or choix == '6' or choix == '7' or choix == '8' :
        for x in range 2 :
            code_recharge = input ("Saisir nombre de code recharge souhaite: Entre 1 et 20: \n")
        print ("le nombre d'essais maximum est atteint.")

    
def acheter_credit_ou_offre_telma (choix, code_secret) :
    choix = int (input ("""
    Acheter Credit ou offre Telma
    1 Credit pour mon numero
    2 Credit pour un autre numero
    4 Offre pour mon numero
    5 Offre pour un autre numero
    """))
    if choix == 1 :
        choix = int (input ("""
        Credit pour mon numero 
        1 Recharger directement
        2 Code recharge
        """))
        if choix == 1 :
            montant = int (input ("Entrer montant :"))
            code_secret = input ("Pour accepter de recharger" + montant + "Ar sur votre compte prepaye depuis votre compte Mvola, entrer votre code secret" )
            print ("""
            Votre solde MVola est insuffisant. Votre solde est de 0Ar. Faites un depot MVole suffisant pour pouvoir
            effectuer cette transaction. Ref:421521052
            """)
        elif choix == 2 :
            page_precedente_choisir_montant_souhaite (choix, code_recharge)
        else :
            acheter_credit_ou_offre_telma (choix)
    elif choix == 2 :
        choix = int (input ("""
        Credit pour un autre numero
        1 Recharger directement 
        2 Code recharge 
        """))
        if choix == 1 :
            numero = int (input ("Enter le numero tel. : (9 pour voir le repertoire MVola)"))
            if numero == 9 :
                numero = int (input ("Aucun contact enregistre, entrer le numero beneficier : "))
            else :
                montant = int (input ("Entrer montant :"))
                code_secret = input ("Pour accepter de recharger" + montant + "Ar sur le numero " + numero + " depuis votre compte Mvola, entrer votre code secret" )
                print ("""
                Votre solde MVola est insuffisant. Votre solde est de 0Ar. Faites un depot MVole suffisant pour pouvoir
                effectuer cette transaction. Ref:421521052
                """)
        elif choix == 2 :
            choix = int (input ("""
            Code Recharge :
            1 Acheter code recharge
            2 Renvoyer dernier achat 
            """))
            if choix == 1 :
                numero = input ("Enter numero tel. :")
                page_precedente_choisir_montant_souhaite_autre (choix, code_recharge)
            elif choix == 2 :
                code =  input ("""
                Pour envoyer vos Code(s) Recharge(s) non encore consomme(s), saisir votre
                reference de transaction:
                """)
                print ("""Desole, la reference de transaction que vous avez entre n est pas
                valide.""")
        elif choix == 4 :
            offres (choix)

         else :
            print (message_fin)

    elif choix == 4 : 
        offres (choix, code_secret)

    elif choix == 5 :
        numero = int (input ("Enter le numero tel. : (9 pour voir le repertoire MVola)"))
        if numero == 9 :
            numero = int (input ("Aucun contact enregistre, entrer le numero beneficier : "))
        else :
            offres (choix, code_secret)
    else :
        acheter_credit_ou_offre_telma (choix, code_secret)

                


            
entrer_numero = "Entrer le numero de tel. Destinataire : "

page_services_telma = """
SERVICES TELMA
1 Info credit prepaye
2 Recharge 
3 Gerer Friends and Family
4 Envoyer Credit/Offre/Mega
5 Ajouter des Jours de validite
# Page suivante
"""
services_telma_1 = """
info Conso
1 Info credit prepaye
2 Info Conso Internet
"""
services_telma_1_1 = """
Votre credit est de 0 ar, valable jusqu'au 25/15/2023.
Bonus 0 Ar vers Ami Telma, 0 Ar vers tout destination
"""
services_telma_1_2 = """
Il vous reste 0 Mo de bonus internet sur votre compte, valabke jusqu'au 25/12/2023
"""
services_telma_2 = """
Recharge
1 Recharger mon numero
2 Recharger un autre numero
3 Recharger avec MVola
4 Recharger via 2TMV
"""
services_telma_2_1 = """
Entrer le code recharge :
"""
services_telma_2_2 = entrer_numero

page_suivante_de_la_page_services_telma = """
SERVICES TELMA
6 Acheter une offre
7 Mon numero
8 Changement de Langue
9 Recuperer mon Numero
* Page precedente
** Top menu
"""
def tmv_mora (choix) :
    tableau_mora = ['Mora 500', 'Mora One', 'Mora+ 2000', 'Mora+ 5000', 'Mora Night', 'Mora TEAM', 'Mora Intenational']
    tableau_mora_prix = ['500 Ar', '1000 Ar', '2000 Ar', '5000 Ar', '500 Ar', '1000 Ar', '5000 Ar']
 
    choix = input ("""
    MORA (Voix - SMS - Internet)
    1. Mora 500 (500 Ar)
    2. MORA ONE (1000 Ar)
    3. Mora+ 2000 (2000 Ar)
    4. Mora+ 5000 (5000 Ar)
    5. Mora Night (500 Ar)
    # Page suivante
    """)
    if choix == "#" :
        choix = input ("""
        MORA (Voix - SMS - Internet)
        6. Mora TEAM (1000 Ar)
        7. Mora International (5000 Ar)
        * Page Precedente
        ** Top Menu
        """)
        if choix == "*" or choix == "**" :
            tmv_mora (choix)
    else :
        print ("Le numero saisi ne vend pas de 2TMV")

def tmv_first (choix) :
    tableau_first = ['first Premium', 'First Premium +', 'First Prestige', 'First Royal']
    tableau_first_prix = ['10000 Ar', '15000 Ar', '30000 Ar', '50000 Ar']
    choix = int (input ("""First (VOix - SMS - Internet)
    1.""" + tableau_first[0] + "(" + tableau_first_prix[0] + ")" + """
    2.""" + tableau_first[1] + "(" + tableau_first_prix[1] + ")" + """
    3.""" + tableau_first[2] + "(" + tableau_first_prix[2] + ")" + """
    4.""" + tableau_first[3] + "(" + tableau_first_prix[3] + ")"
    ))
    if choix = 1 or choix = 2 or choix = 3 or choix = 4 :
        print ("Le numero saisi ne vend pas de 2TMV")
    else tmv_first (choix)
        
def tmv_yellow (choix) :
    tableau_yellow = ['Yellow100', 'Yellow SMS', 'Yellow Facebibaka', 'Yellow 1000', 'YEllow Faceboobaka One', 'Yellow 200', 'Yellow Faceboobaka +', 'Yellow One']
    tableau_yellow_prix = ['100 Ar', '200 Ar', '500 Ar', '1000 Ar', '1000 Ar', '200 Ar', '2000 Ar', '1000 Ar']
    choix = (input ("""Yellow (SMS - Internet)
        1. """ + tableau_yellow[0] + "(" + tableau_yellow_prix[0] + ")" + """
        2. """ + tableau_yellow[1] + "(" + tableau_yellow_prix[1] + ")" + """
        3. """ + tableau_yellow[2] + "(" + tableau_yellow_prix[2] + ")" + """
        4. """ + tableau_yellow[3] + "(" + tableau_yellow_prix[3] + ")" + """
        5. """ + tableau_yellow[4] + "(" + tableau_yellow_prix[4] + ")" + """
        # Page suivante
        """
        ))
        if choix == "#" :
            choix = (input ("""Yellow (SMS - Internet)
            6. """ + tableau_yellow[5] + "(" + tableau_yellow_prix[5] + ")" + """
            7. """ + tableau_yellow[6] + "(" + tableau_yellow_prix[6] + ")" + """
            8. """ + tableau_yellow[7] + "(" + tableau_yellow_prix[7] + ")" + """
            * Page precedente
            ** Top Menu
            """
            ))
            if choix == "*" or choix == "**" :
                tmv_yellow (choix)
        else :
            print ("Le numero saisi ne vend pas de 2TMV")

def tmv_net_mensuel (choix) :
    tableau_net_mensuel = ['Net one month 2 Go', 'Net one month 4 Go', 'Net one month 12 Go', 'Net one month 25 Go', 'Net one month 50 Go', 'Net one month 100 Go']
    tableau_net_mensuel_prix = ['15000 Ar', '25000 Ar', '75000 Ar', '125000 Ar', '150000 Ar', '159000 Ar']
    choix = (input ("""NET MENSUEL
    1. """ + tableau_net_mensuel[0] + "(" + tableau_net_mensuel_prix[0] + ")" + """
    2. """ + tableau_net_mensuel[1] + "(" + tableau_net_mensuel_prix[1] + ")" + """
    3. """ + tableau_net_mensuel[2] + "(" + tableau_net_mensuel_prix[2] + ")" + """
    4. """ + tableau_net_mensuel[3] + "(" + tableau_net_mensuel_prix[3] + ")" + """
    5. """ + tableau_net_mensuel[4] + "(" + tableau_net_mensuel_prix[4] + ")" + """
    # Page suivante
    """
    ))
    if choix == "#" :
        choix = (input ("""NET MENSUEL
        6. """ + tableau_net_mensuel[5] + "(" + tableau_net_mensuel_prix[5] + ")" + """
        * Page precedente
        ** Top Menu
        """
        ))
        if choix == "*" or choix == "**" :
            tmv_net_mensuel (choix)
    if choix == '1' or choix == '2' or choix == '3' or choix == '4' or choix == '6' or choix == '5'
        print = ("Le numero saisi ne vend pas de 2TMV")
    else :
        tmv_net_mensuel (choix)

def tmv_mkozy (choix) :
    choix = int (input ("""
    M KOZY (VOIX-INTERNET)
    1. M KORAGNA (6000 Ar)
    2. M KAIKY (4000 Ar)
    """))
    
    if choix == 1 or choix == 2 :
        print ("Le numero saisi ne vend pas de 2TMV")
    
    else :
        tmv_mkozy (choix)

def tmv_telma_net (choix) :
    choix = int (input ("""
    TELMA Net (INTERNET)
    1 Net Journalier
    2 Net Hebdomadaire
    3 Net Mensuel
    4 TELMA Net (INTERNET)
    5 M KOZY (Voix - Internet)
    """))
    if choix = 1 :
        choix = int (input ("""
        Net Journalier
        1. Telma Net nuit (100 Ar)
        """))

        if choix == 1 :
            print ("Le numero saisi ne vend pas de 2TMV")

        else :
            tmv_telma_net (choix)
    
    elif choix = 2 :
        choix = int (input ("""
            Net Hebdomadaire
            1. Net One Week 350 Mo (3000 Ar)
            2. Net One Week 800 Mo (5000 Ar)
            3. Net One Week 2 Go (10000 Ar)
        """))

        if choix == 1 or choix == 2 or choix == 3:
            print ("Le numero saisi ne vend pas de 2TMV")

        else :
            tmv_telma_net (choix)

    elif choix = 3 :
        tmv_net_mensuel (choix)

    elif choix = 4 :
        tmv_telma_net (choix)
    
    elif choix = 5 :
        choix = int (input ("""
        M KOZY (VOIX-INTERNET)
        1. M KORAGNA (6000 Ar)
        2. M KAIKY (4000 Ar)
        """))
        
        if choix == 1 or choix == 2 :
            print ("Le numero saisi ne vend pas de 2TMV")
        
        else :
            tmv_mkozy (choix)

    else : 
        tmv_telma_net (choix)


choix = input (page_services_telma)

if choix == '1' :
    choix = int (input (services_telma_1))
    if choix == 1 :
        print (services_telma_1_1)

    elif choix == 2 :
        print (services_telma_1_2)

elif choix == '2' :
    choix = int (input (services_telma_2))
    if choix == 1 :
        code_recharge = input (services_telma_2_1)
        print ("Votre code de recharge est invalide.")

    elif choix == 2 :
        numero = input (services_telma_2_2)
        code_recharge = input (services_telma_2_1)
        print ("Votre code de recharge est invalide.")

    elif choix == 3 :
        acheter_credit_ou_offre_telma (choix, code_secret)

    elif choix == 4 :
        numero = input ("Saisir le numero du revendeur :")
        choix = int (input ("""
        1 Credit
        2 offre
        """))
        
        if choix == 1 :
            montant = input ("ENtrer montant :")
            print ("Le numero que vous avez saisi ne vend pas de 2TMV")
        
        elif choix == 2 :
            choix = input ("""
            Votre offre tarifaire actuelle est TOKANA.
            1. MORA (VOIX - SMS - INTERNET)
            2. FIRST (VOIX - SMS - INTERNET)
            3. YELLOW (SMS - INTERNET)
            4. TELMA Net (Internet)
            """)
            if choix = 1 :
                tmv_mora (choix)
            elif choix = 2 :
                tmv_first (choix)
            elif choix = 3 :
                tmv_yellow (choix)
            elif choix = 4 :
                tmv_telma_net (choix)


elif choix == '3' :
    choix = int (input ("""
    Gerer Friends and Family
    1 Ajouter un contact
    2 Effacer un contact
    3 Liste Friends and Family
    """))

    if choix = 1 :
        numero = input ('Entrer le numero : ')
        print ("Le numero " + numero + " a ete rajoute avec succes.")
    
    elif choix = 2 :
        print ("Ne peut pas supprimer le numero FAF. Vous devez remplir votre liste de numero FAF.")

    elif choix = 3 :
        print ("Vous n'avez pas de numeros FRIENDS & FAMiLY. Pour ajouter un numero, composez #344*1*numero#")

elif choix == '4' :
    print ("indisponible")

elif choix == '5' :
    print ("indisponible")
elif choix == '#' :

    choix = input (page_suivante_de_la_page_services_telma)
    if choix == '6' :
        print ("indisponible")
    elif choix == '7' :
        print ("indisponible")
    elif choix == '8' :
        print ("indisponible")
    elif choix == '*' or choix == "**" :
        print ("indisponible")
    