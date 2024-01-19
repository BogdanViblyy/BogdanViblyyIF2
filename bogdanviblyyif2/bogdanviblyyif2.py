from datetime import *
import math 
import random


#ülesanne 1: Juku




# nimi=input(str("Mis on sinu nimi?")).capitalize()
# print("Tere,", nimi)    #Tere, Anna"
# if nimi=="Juku":
#     print=("Lähme kinno")
#     vanus=int(input("Kui vana sa oled?"))
#     if 0<vanus<6:
#         pilet="tasuta pilet"
#     elif vanus<=14: #<15
#         pilet="lastepilet"
#     elif vanus<=65: 
#         pilet="täispilet"<
#     elif vanus<=100:
#         pilet="sooduspilet"
#     else:
#         pilet="vale vanus"
#     print(pilet)    
    
# else:
#     print=("Kinnose ei lähe :(")



# ülesanne 2
# print("Sisestage oma nimed")
# nimi1=input("1: ")
# nimi2=input("2: ")

# print(nimi1," ja ",nimi2," olete pinginabrid")



 # ülesanne 3
# a=float(input("milline on esimese seinapikkus?"))
# b=float(input("milline on teise seinapikkus?"))
# pindala=a*b
# print("ruumi pindala on", pindala)
# vastus=input("Kas tahate remondi teha? jah/ei: ")
# if vastus=="jah":
#     hind=float(input("Sisestage 1 meetri hind: "))
#     remondiHind=pindala*hind
#     print("Remondi hind on ",remondiHind)



# ülesanne 4
# hind=int(input("milline on hind?"))

# if hind > 700:
#     soodus=hind*0.3
#     hindSoodustega=hind-soodus

#     print("Hind soodustega on: ",hindSoodustega)


# ülesanne 5
# temp=int(input("Sisestage temperatuur: "))

# if temp > 18:
#     print("Temperatuur üle 18 kraadi")
# else:
#     print("Temperatuur vähem kui 18 kraadi")


# ulesanne 6
# pikkus=int(input("Sisestage oma pikkus sm: "))

# if pikkus <=160:
#     print("Te olete lühike")

# elif pikkus >160 and pikkus <= 175:
#     print("Te olete keskmine")

# elif pikkus > 175:
#     print("Te olete suur")


# ülesanne 7

# pikkus=int(input("Sisestage oma pikkus sm: "))
# sugu=input("Sisestage oma sugu, mees või naine: ")

# if sugu=="naine":
        
#     if pikkus <=160:
#         print("Te olete väike")

#     elif pikkus >160 and pikkus <= 175:
#         print("Te olete keskmine", sugu)

#     elif pikkus > 175:
#         print("Te olete suur ",sugu)
# elif sugu=="mees":
#     if pikkus <=170:
#         print("Te olete väike")

#     elif pikkus >170 and pikkus <= 185:
#         print("Te olete keskmine ",sugu)

#     elif pikkus > 185:
#         print("Te olete suur ",sugu)


#ülesanne 8(1)
#from datetime import *
#from random import *
#arve_nr= date.today()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"/nToode Hind Kogus Summa/n"
#summa=0
#for toode in ["Piim","Leib","Komm"]:
#    hind=randint(50,150)/100
#    v=input("Toode:"+toode+"Hind:"+str(hind)+"/Kas tahad osta?").lower()
#    if v=="jah":
#        mitu=int(input("Mitu? "))
#        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"/n"
#    summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#while True:
#    raha=float(input("Maksa "+str(summa)))
#    if raha==summa:
#        print("Tänan ostu eest!")
#        break
#    elif raha>summa:
#        print("Tänan ostu eest! Tagasi "+str(raha-summa))
#        break
#    else:
#        summa-=raha
#        print("Maksa veel"+str(summa))

#toode="Piim"
#hind=randint(50,150)/100
#v=input("Toode:"+toode+"Hind:"+str(hind)+"/Kas tahad osta?").lower()
#if v=="jah":
#    mitu=int(input("Mitu? "))

#raha=float(input("Maksa "+str(summa))
#if raha==summa:
#    print("Tänan ostu eest!")
#elif raha>summa:
#    print("Tänan ostu eest! Tagasi "+str(raha-summa))
#else:
#    print("Maksa veel"+str(summa-raha))











# ülesanne 8(v2)


# tahabOstaPiim=input("Kas tahate osta piima? jah/ei: ")
# if tahabOstaPiim=="jah":
#     piimaKogus=int(input("Mittu?: "))
#     piimaHind=random.randint(1,20)
#     piimaArve=piimaKogus*piimaHind
    

# tahabOstaLeib=input("Kas tahate osta leib? jah/ei: ")
# if tahabOstaLeib=="jah":
#     leibaKogus=int(input("Mittu?: "))
#     leibaHind=random.randint(1,20)
#     leibaArve=leibaKogus*leibaHind
    


# tahabOstaHappukoor=input("Kas tahate osta happukoor? jah/ei: ")
# if tahabOstaHappukoor=="jah":
#     happukooreKogus=int(input("Mittu?: "))
#     happukooreHind=random.randint(1,20)
#     happukooreArve=happukooreKogus*happukooreHind
# koguArve=piimaArve+leibaArve+happukooreArve    


# print("Piim: ",piimaKogus,"tükki")
# print("Leib: ",leibaKogus,"tükki")
# print("Happukoor: ",happukooreKogus,"tükki")
# print("Peate maksma: ",koguArve,'$')


# ülesanne 9

# a=int(input("Sisestage a külg: "))
# b=int(input("Sisestage b külg: "))

# if a==b:
#     print("See on ruut")

# else:
#     print("See ei ole ruut")
    

# ülesanne 10

# num1=int(input("Number 1: "))
# num2=int(input("Number 2: "))

# tegevus=input("Sisestage tegevus, + - * või /: ")

# if tegevus == '+':
#     vastus=num1+num2
# elif tegevus == '-':
#     vastus=num1-num2
# elif tegevus == '*':
#     vastus=num1*num2
# elif tegevus == '/':
#     vastus=num1/num2

# print("Vastus: ",vastus)

# ülesanne 11

#ta=date.today().year
#sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: ")))
#if (ta-sp)%5==0:
#    print("Juubel")
#else:
#    print("Tavaline sünnipäev")


# ülesanne 12

# hind=float(input("Sisestage hind: "))
# if hind <=10.00:
#     soodus=hind*0.1
#     print("Soodus on 10%")

# elif hind > 10.00:
#     soodus=hind*0.2
#     print("Soodus on 20%")


# hindSoodustega=hind-soodus
# print("Hind soodustega: ",hindSoodustega)


# ülesanne 13

# sugu=input("Sisestage oma sugu, mees või naine: ")
# if sugu == "mees":
#     vanus=int(input("Sisestage oma vanus"))

#     if 16<=vanus<=18:
#         print("Te sobite")
# else:
#     print("Te ei sobi")
    
     
#ülesNNE 14

maht=int(input("Bussi maht: "))
i=int(input("Inimeste arv: "))
ba=round(i/maht) #2,3->2
if i%maht !=0:
    ba+=1
    vb=i%maht
    print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))
#ülesanne 14(2)

# bussiMahtuvus=int(input("Sisestage ühe bussi mahutavus: "))
# inimesteArv=int(input("Sisestage inimeste arv: "))

# bussideArv = math.ceil(inimesteArv / bussiMahtuvus)
# inimesedViimaselBussil= inimesteArv-bussideArv*bussiMahtuvus+bussiMahtuvus

# print("Bussi kogus: ",bussideArv)
# print("Inimeste arv viimasel bussil: ",inimesedViimaselBussil)
