case_1 = case_2 = case_3 = case_4 = case_5 = case_6 = case_7 = case_8 = case_9 = 'non_remplie'
cases = [case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9]

x_1 = x_2 = x_3 = x_4 = x_5 = x_6 = x_7 = x_8 = x_9 = ' '
cases_remplies = [x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9]

def affirmation (x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9) :
    global cases
    cases = [case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9]
    global cases_remplies
    cases_remplies = [x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9]
    
def affichage (x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9) :
    print ("""
       |       |       
   """ + x_1 + """   |   """ + x_2 + """   |   """ + x_3 + """
_______|_______|_______
       |       |
   """ + x_4 + """   |   """ + x_5 + """   |   """ + x_6 + """
_______|_______|_______
       |       |
   """ + x_7 + """   |   """ + x_8 + """   |   """ + x_9 + """
       |       |
""")