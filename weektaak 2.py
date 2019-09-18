#dit deel vraagt om de sequentie en maakt een variabele van de letters in de sequentie.
sequentie = input("sequentie: ")
nucleotide_A = "A"
nucleotide_C = "C"
nucleotide_G = "G"
nucleotide_T = "T"

#dit deel telt de letters in de sequentie.
aantal_A = sequentie.count(nucleotide_A)
print ("aantal_A: ",aantal_A)
aantal_C = sequentie.count(nucleotide_C)
print ("aantal_C: ",aantal_C)
aantal_G = sequentie.count(nucleotide_G)
print ("aantal_G: ",aantal_G)
aantal_T = sequentie.count(nucleotide_T)
print ("aantal_T: ",aantal_T)

#dit deel rekent de resultaten uit en print die.
ACGT = (aantal_A + aantal_C) + aantal_G + aantal_T
percentage_GC = aantal_G + aantal_C / ACGT *100
print ("percentage_GC", percentage_GC)
print ("aantal nucleotide: ", ACGT)

