page_rappelle_moi = """
1 Envoyer un Rappelle Moi
2 Aide 
"""
rappelle_moi_1 = """
Entrer le numero de tel. Destinataire :
"""
rappelle_moi_2 = """
Bienvenue. Pour le Rappelle-Moi composez #555*Numero TELMA MOBILE#. Pour SOS credit composez #555*1*Numero 
TELMA Mobile*somme a demander# 
"""


choix = int (input (page_rappelle_moi))
if choix == 1 :
    numero = input (rappelle_moi_1)
    print ("Votre demande de Rappelle-moi a ete envoyee")

if choix == 2 :
    print (rappelle_moi_2)