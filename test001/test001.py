import numpy as np


def cryptoMonoAlpha():
    #crypto mono alphabetique
    char =input("entrer le texte a crypte : ").upper();
    cle = int(input("entrer la cle : "));
    s = str();
    char1 =str();
    #encryptage
    print("cryptage");
    for i in char:
        if i != (" "):
            tmp = ord(i) + cle;
            if tmp >= ord('Z'):
                tmp -= 26;
            s += chr(tmp);    
    print(s);
    #decryptage
    print("decryptage");
    for i in s:
        tmp = ord(i) - cle;
        if tmp < ord('A'):
            tmp += 26;
        char1 += chr(tmp);
    print(char1);
    #ok
def cryptoDeVigen():
    
    txt = str(input("entrer le texte a crypte(sans espace) : ")).upper();
    cle = str(input("entrer la cle : ")).upper();
    
    k = 0;
    mat = np.empty([26,26], dtype= str)

    #creation matice
    for i in range(26):
        k = i + 65;
        for j in range(26):
            if k >= 91:
                k -= 26
            mat[i,j] = chr(k)
            k += 1;

    #check txt cle
    k = 0;
    cle1 = ""
    res = ""
    for i in range(len(txt)):
        if k == len(cle):
            k -= len(cle)
        cle1 += cle[k]
        k += 1

    #encrypte
    print("encrypte")
    k = 0
    for i in txt:
        res += mat[ord(i) - 65, ord(cle1[k]) - 65];
        k += 1
    print("resultat :")
    print(res,end="\n");

    #decrypte
    print("decrypte")
    res1 = ""
    k = 0
    for i in cle1:
        for j in range(26):
            if res[k] == mat[ord(i) - 65, j]:
                res1 += mat[0, j]
                k += 1
                break

    print("resultat :")
    print(res1,end="\n");
    #ok

cryptoDeVigen()
