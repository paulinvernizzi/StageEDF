# coding=utf-8
import os
import numpy as np
import matplotlib.pyplot as plt

## OPTIONS ##
creation = True # True if you want to calculate the error, False if you just want to manipulate the graph
graph = True	# True if you want to see the graph
savefig = 1 # 1 if you want to save the figure, 0 otherwise
Xticks = [50,100]
avectitre = False

## PARAMETERS ##
typeuinc = 0 # Type of the incident wave (1 : source point, 0 : planar wave)
typecouche = 5 # Type of the thin layer (0 : cos(t - pi), 1 : cos(t - pi/2), 2 : cos(t - 3pi/4), 3 : cos(5t), 4 : cos(-5t), 5 : 1 
debutNptL = 45 # The first measure of the parameter NptL
finNptL = 55 # The final measure of the parameter NptL
Niter = 5 # The number of points in the graph
delta = 0.08
ordre = 1 # Order in delta of the modelisation

#Paramètre physique
k = 1
rmup, imup = 0.01,0.0
repsp, iepsp = 100.,0.1
rmum, imum = 0.01,0.
repsm, iepsm = 100.,0.1
rmuc, imuc = 0.1,0.
repsc, iepsc = 30.,0.1

savename = "PrecisDelta"+ "delta" + str(delta) + "debutNptL" + str(debutNptL) + "finNptL" + str(finNptL) + "Niter" + str(Niter) + "ordre" + str(ordre) + "typecouche" + str(typecouche)+ "mup"+str(rmup)+"+i"+str(imup)+ "epsp"+str(repsp)+ "+i"+str(iepsp)+"mum"+str(rmum)+"+i"+str(imum)+ "epsm"+str(repsm)+ "+i"+str(iepsm)+"muc"+str(rmuc)+"+i"+str(imuc)+ "epsc"+str(repsc)+ "+i"+str(iepsc)
## CODE ##
X = []
Yp = []
Yhp = []
Zp = []
Zhp = []

## CREATION DES FICHIERS ##
if creation :
	os.system("FreeFem++ /home/c31182/Helmh/Helmh_Comparaison_Precision_Delta.edp -wg -typecouche "+ str(typecouche) +" -re "+ str(repsc) +" -ie "+ str(iepsc) +" -rm "+ str(rmuc) +" -im "+ str(imuc) + " -delta "+ str(delta) + " -ecrire " + str(1) + " -debutNptL "+ str(debutNptL)+ " -finNptL "+ str(finNptL) + " -Niter "+ str(Niter)+  " -uinc "+ str(typeuinc) + " -k "+ str(k) +" -rmup "+ str(rmup) +" -imup "+ str(imup) + " -repsp "+ str(repsp)+" -iepsp "+ str(iepsp)+" -rmum "+ str(rmum)+" -imum "+ str(imum)+ " -repsm "+ str(repsm)+" -iepsm "+ str(iepsm) + " -ordre "+str(ordre))
	os.system("mv Erreurs/Erreur.dat ErreursSauvees/Erreurs_Delta_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_mum_"+str(rmum)+"+i"+str(imum)+"_epsm_"+str(repsm)+"+i"+str(iepsm)+"_mup_"+str(rmup)+"+i"+str(imup)+"_epsp_"+str(repsp)+"+i"+str(iepsp)+"_N_"+str(Niter)+"_debutNptL_"+str(debutNptL)+"_finNptL_"+str(finNptL)+"_delta_"+str(delta)+".txt") ## renome le fichier

# GRAPH #
if graph :
	nom = "ErreursSauvees/Erreurs_Delta_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_mum_"+str(rmum)+"+i"+str(imum)+"_epsm_"+str(repsm)+"+i"+str(iepsm)+"_mup_"+str(rmup)+"+i"+str(imup)+"_epsp_"+str(repsp)+"+i"+str(iepsp)+"_N_"+str(Niter)+"_debutNptL_"+str(debutNptL)+"_finNptL_"+str(finNptL)+"_delta_"+str(delta)+".txt"
	with open(nom,"r") as fichier:
		for ligne in fichier:
			if (ligne != "" and ligne != "\n"):
				if ligne == "end\n":
					continue
				print(ligne)
				l = ligne.split("\n")[0]
				mot,val = l.split(" = ")
				if mot == "NptLa" :
					X.append(float(val))
				if mot == "Erreur Plus" :
					Yp.append(float(val))
				if mot == "Erreur H1Plus" :
					Yhp.append(float(val))
				if mot == "Erreur Relative Plus" :
					Zp.append(float(val))
				if mot == "Erreur Relative H1Plus" :
					Zhp.append(float(val))
	if avectitre :
		plt.title(titre)
	plt.xticks(Xticks,Xticks)
	plt.xlabel("NptLa")
	plt.ylabel("error")
	plt.plot(X, Zp, "o", label = "Erreur Relative L2")
	plt.plot(X, Zhp, "o", label = "Erreur Relative H1")
	plt.legend()
	if savefig == 1:
		plt.savefig("/home/c31182/Helmh/Figures/"+savename,format = "eps", dpi = 1200,bbox_inches = "tight")
	plt.show()
