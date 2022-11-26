# coding=utf-8

#####################################################################################
# This program compares two thin layer model (TLM) with a little difference in mesh parameters.
# README files explains precisely which equations are studied.
# The goal is to draw a graph of the relative error between both models
# following the thin layer thickness "delta0".
# To work it requires the following programs :
# - Helmh_Comparaison_Precision_Delta.edp
# - Helmh_Delta.edp (PETS-c)
#####################################################################################

import os
import numpy as np
import matplotlib.pyplot as plt

## OPTIONS ##
creation = True # True if you want to calculate the error, False if you just want to manipulate the graph
graph = True	# True if you want to see the graph
savefig = 1 # 1 if you want to save the figure, 0 otherwise
Xticks = [50,100]
avectitre = False

## PATHS ##
PATHTOFIGUREFOLDER = "/home/c31182/Helmh/Figures/"
PATHTOPROGRAMFOLDER = "/home/c31182/Helmh/Programs/"
PATHTOTEMPFOLDER = "/home/c31182/Helmh/TEMP/"
PATHTOSAVEFOLDER = "/home/c31182/Helmh/ErreursSauvees/"

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
## CREATION DES FICHIERS ##
if creation :
	os.system("FreeFem++ "+PATHTOPROGRAMFOLDER+"Helmh_Comparaison_Precision_Delta.edp -wg -typecouche "+ str(typecouche) +" -re "+ str(repsc) +" -ie "+ str(iepsc) +" -rm "+ str(rmuc) +" -im "+ str(imuc) + " -delta "+ str(delta) + " -ecrire " + str(1) + " -debutNptL "+ str(debutNptL)+ " -finNptL "+ str(finNptL) + " -Niter "+ str(Niter)+  " -uinc "+ str(typeuinc) + " -k "+ str(k) +" -rmup "+ str(rmup) +" -imup "+ str(imup) + " -repsp "+ str(repsp)+" -iepsp "+ str(iepsp)+" -rmum "+ str(rmum)+" -imum "+ str(imum)+ " -repsm "+ str(repsm)+" -iepsm "+ str(iepsm) + " -ordre "+str(ordre) + " -PTPF " + PATHTOPROGRAMFOLDER + " -PTTF " + PATHTOTEMPFOLDER)
	os.system("mv "+PATHTOTEMPFOLDER+"Erreur.dat "+PATHTOSAVEFOLDER+"Erreurs_Delta_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_mum_"+str(rmum)+"+i"+str(imum)+"_epsm_"+str(repsm)+"+i"+str(iepsm)+"_mup_"+str(rmup)+"+i"+str(imup)+"_epsp_"+str(repsp)+"+i"+str(iepsp)+"_N_"+str(Niter)+"_debutNptL_"+str(debutNptL)+"_finNptL_"+str(finNptL)+"_delta_"+str(delta)+".txt") ## renome le fichier

# GRAPH #
Listes = [[],[],[],[],[]]
if graph :
	nom = PATHTOSAVEFOLDER+"Erreurs_Asymptotic_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_mum_"+str(rmum)+"+i"+str(imum)+"_epsm_"+str(repsm)+"+i"+str(iepsm)+"_mup_"+str(rmup)+"+i"+str(imup)+"_epsp_"+str(repsp)+"+i"+str(iepsp)+"_N_"+str(Niter)+"_debutNptL_"+str(debutNptL)+"_finNptL_"+str(finNptL)+"_delta_"+str(delta)+".txt"
	Mots = ["NptLa","Erreur Plus","Erreur H1Plus","Erreur H1Plus","Erreur Relative Plus","Erreur Relative H1Plus"]
	with open(nom,"r") as fichier:
		for ligne in fichier:
			if (ligne != "" and ligne != "\n"):
				if ligne == "end\n":
					continue
				l = ligne.split("\n")[0]
				mot,val = l.split(" = ")
				if mot in Mots:
					Listes[Mots.index(mot)].append(val)
	if avectitre :
		plt.title(titre)
	plt.xticks(Xticks,Xticks)
	plt.xlabel("NptLa")
	plt.ylabel("error")
	plt.xticks(Xticks,Xticks)
	plt.plot(Listes[0], Listes[3], "x", label = "L2 Relative Error")
	plt.plot(Listes[0], Listes[4], "x", label = "H1 Relative Error")
	plt.legend()
	if savefig == 1:
		plt.savefig(PATHTOFIGUREFOLDER+savename,format = "eps", dpi = 1200,bbox_inches = "tight")
	plt.show()
