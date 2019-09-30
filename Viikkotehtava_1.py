print("Tervetuloa Presidentti Martti Ahtisaari tietokilpailupeliin")
oikeat_vastaukset_lkm = 0
nimi = input("Mikä on nimesi?\n")
print("Hei",nimi, "onnea kilpailuun")
print("valitse oikea vastaus vaihtoehdoista 1-5:")
vastaus = input("Minä vuonna Martti Ahtisaari on syntynyt?\n 1. 1932\n 2. 1935\n 3. 1937\n 4. 1939\n 5. 1942\n")
if (vastaus == "3"):
    print("Oikein!\n")
    oikeat_vastaukset_lkm += 1
else :
    print("Väärin!\n")

vastaus = input("Missä kaupungissa Martti Ahtisaari on syntynyt?\n 1. Helsinki\n 2. Turku\n 3. Tampere\n 4. Viipuri\n 5. Kotka\n")
if (vastaus == "4"):
    print("Oikein!\n")
    oikeat_vastaukset_lkm += 1
else :
    print("Väärin!\n")

vastaus = input("Minä vuonna Martti Ahtisaari valittiin presidentiksi?\n 1. 1990\n 2. 1992\n 3. 1994\n 4. 1996\n 5. 1998\n")
if (vastaus == "3"):
    print("Oikein!\n")
    oikeat_vastaukset_lkm += 1
else :
    print("Väärin!\n")

vastaus = input("Monesko Suomen presidentti Martti Ahtisaari oli?\n 1. 9\n 2. 10\n 3. 11\n 4. 12\n 5. 13\n")
if (vastaus == "2"):
    print("Oikein!\n")
    oikeat_vastaukset_lkm += 1
else :
    print("Väärin!\n")

vastaus = input("Minä vuonna Martti Ahtisaari sai Nobelin rauhanpalkinnon?\n 1. 2005\n 2. 2006\n 3. 2007\n 4. 2008\n 5. 2009\n")
if (vastaus == "4"):
    print("Oikein!\n")
    oikeat_vastaukset_lkm += 1
else :
    print("Väärin!\n")
    
vastaus = input("Mikä on Martti Ahtisaaren reservin arvo?\n 1. Yliluutnantti\n 2. Kapteeni\n 3. Komentaja\n 4. Majuri\n 5. Eversti\n")
if (vastaus == "2"):
    print("Oikein!\n")
    oikeat_vastaukset_lkm += 1
else :
    print("Väärin!\n")

vastaus = input("Minä vuonna Martti Ahtisaaren teos Tehtävä Belgradissa ilmestyi?\n 1. 1999\n 2. 2000\n 3. 2001\n 4. 2002\n 5. 2003\n")
if (vastaus == "2"):
    print("Oikein!\n")
    oikeat_vastaukset_lkm += 1
else :
    print("Väärin!\n")

kysymykset_lkm = 7
oikein_prosentti = int(oikeat_vastaukset_lkm / kysymykset_lkm * 100)
print("Oikeiden vastauksien määrä prosentteina",oikein_prosentti,"%")
