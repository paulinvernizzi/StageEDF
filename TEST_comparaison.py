# coding=utf-8
import os
import numpy as np
import matplotlib.pyplot as plt

DNptL = 100
ENptL = 500
Niter = 50
NmNev = 30

X = []
Y = []
Yh = []
Z = []
Zh = []
Xt = []
Yt = []
Zt = []

os.system("FreeFem++ /home/c31182/Helmh/TEST_comparaison.edp -DNptL "+str(DNptL)+" -ENptL "+str(ENptL)+" -Niter "+str(Niter)+" -NmNev "+str(NmNev))
os.system("mv Resultats3/Erreurs.dat Resultats3/Erreurs.txt") ## renome le fichier

nom = "Resultats3/Erreurs.txt"
with open(nom,"r") as fichier:
		for ligne in fichier:
			if (ligne != "" and ligne != "\n"):
				if ligne == "end\n":
					continue
				print(ligne)
				l = ligne.split("\n")[0]
				mot,val = l.split(" = ")
				if mot == "NptL" :
					X.append(float(val))
				if mot == "erreurL2SLEPC" :
					Y.append(float(val))
				if mot == "erreurH1SLEPC" :
					Yh.append(float(val))
				if mot == "erreurL2EIGEN" :
					Z.append(float(val))
				if mot == "erreurH1EIGEN" :
					Zh.append(float(val))
nom = "Resultats3/Time.txt"
with open(nom,"r") as fichier:
		for ligne in fichier:
			if (ligne != "" and ligne != "\n"):
				if ligne == "end\n":
					continue
				print(ligne)
				l = ligne.split("\n")[0]
				mot,val = l.split(" = ")
				if mot == "NptL" :
					if float(val) not in Xt:
						Xt.append(float(val))
				if mot == "TimeEIGEN" :
					Yt.append(float(val))
				if mot == "TimeSLEPC" :
					Zt.append(float(val))

plt.plot(X, Z, "o", label = "Erreur EIGEN L2")
plt.plot(X, Zh, "o", label = "Erreur EIGEN H1")
plt.plot(X, Y, "o", label = "Erreur SLEPC L2")
plt.plot(X, Yh, "o", label = "Erreur SLEPC H1")
plt.legend()
plt.show()

plt.plot(Xt, Zt, "o", label = "Time SLEPC")
plt.plot(Xt, Yt, "o", label = "Time EIGEN")
plt.legend()
plt.show()
