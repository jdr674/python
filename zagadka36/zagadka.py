# ROzwiazanie zagadki "36"

print ("""

    ZAGADKA '36'

    """);


p=1; d=1;t=1;
iloczyn=36;

for p in range (1, 37):
    for d in range (1, 37):
        for t in range (1, 37):
           if p*d*t==iloczyn:
               print (" Udalo sie znalesc:", p, " ", d ," ", t, " Suma:", p+d+t);

print ("Koniec");
