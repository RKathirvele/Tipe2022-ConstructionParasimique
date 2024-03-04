#1 Lire les valeurs de l'arduino

import serial
port =serial.Serial ('COM5', baudrate=9600)

fichier = open('valeur.txt', 'w')

port.readline()
for i in range (1000):
    donnee= port.readline().decode()
    print(donnee)
    fichier.write(donnee)

fichier.close()


#2 Traitement des valeurs

import matplotlib.pyplot as plt

time=[]
accelerometre=[]
potentiometre=[]
with open('potentiometre.txt', 'r') as fichier:
    for ligne in fichier:
        valeur=ligne.split(":")
        print(valeur)
        time.append(float(valeur[0]))
        accelerometre.append(int(valeur[1]))
        potentiometre.append(float(valeur[2]))
        

plt.plot(time,potentiometre)
plt.plot(time,accelerometre)
plt.show

        
        
        
