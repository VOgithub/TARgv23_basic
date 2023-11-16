print ("Hello,world!")
kool = input ("Mis koolis sa õpid?: ")      #str kool
kursus = int (input ("Mis kursusel?: "))   #int kursus
print("Tere tulemast kooli "+kool+"\n Ole hea "+ str (kursus)+ ".kursuse õpilaseks!")
print ("Tere tulemast kooli",kool,"!\nOle hea",kursus,".kursuse õpilaseks!")
print ("Tere tulemast kooli {0}! \nOle hea {1}.kursuse õpetajaks!",format (kool,kursus))