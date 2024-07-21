def arranger () :

# Les alphabets :
    a = ['a', 'A']
    b = ['b', 'B']
    c = ['c', 'C']
    d = ['d', 'D']
    e = ['e', 'E']
    f = ['f', 'F']
    g = ['g', 'G']
    h = ['h', 'H']
    i = ['i', 'I']
    j = ['j', 'J']
    k = ['k', 'K']
    l = ['l', 'L']
    m = ['m', 'M']
    n = ['n', 'N']
    o = ['o', 'O']
    p = ['p', 'P']
    q = ['q', 'Q']
    r = ['r', 'R']
    s = ['s', 'S']
    t = ['t', 'T']
    u = ['u', 'U']
    v = ['v', 'V']
    w = ['w', 'W']
    x = ['x', 'X']
    y = ['y', "Y"]
    z = ['z', 'Z']

    alphabet = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

    print ("\nEntrer 0 pour arreter de scanner")
    for x in range (500) :
        
        mot = input ("Entrer le mot ou le groupe de mots a arranger : ")
        
        if mot == '0' :
            print ('')
            break

        else :
        
        # Verification que la premiere lettre appartient a l'alphabet :
            num = 0
            
            for y in range (26) :
            
                if mot [0] == (alphabet [num]) [0] or mot [0] == (alphabet [num]) [1] :
                    (alphabet [num]).append (mot)
                num += 1

# Arrange l'affichage en ajoutant " :"
    num = 0

    for x in range (26) :
        (alphabet [num]).pop(0)
        (alphabet [num]) [0] = (alphabet [num]) [0] + ' :'
        num += 1

    num = 0

# Affiche la liste des elements ayant le meme alphabet debutant le mot uniquement*:
    for x in range (len (alphabet)) :
        
        for y in (alphabet [num]) :
            
            # *uniquement* :
            if len (alphabet [num]) == 1 :
                continue

            else :
                print (y)        
        
        num += 1