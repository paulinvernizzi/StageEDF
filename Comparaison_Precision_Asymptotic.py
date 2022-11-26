# coding=utf-8

#####################################################################################
# This program compares two asymptotic model (AM) with a little difference in mesh parameters.
# README files explains precisely which equations are studied.
# The goal is to draw a graph of the relative error between both models
# following the thin layer thickness "delta0".
# To work it requires the following programs :
# - Helmh_Comparaison_Precision_Asymptotic.edp
# - Helmh_asymptotic.edp (if you want to test the asymptotic model at order 1)
# - Helmh_asymptotic_ordre2.edp (if you want to test the asymptotic model at order 2).
#####################################################################################

import os
import numpy as np
import matplotlib.pyplot as plt

## OPTIONS ##
creation = True # True if you want to calculate the error, False if you just want to manipulate the graph
graph = True	# True if you want to see the graph
savefig = 1 # 1 if you want to save the figure, 0 otherwise
Xticks = [0.03,0.05,0.1,0.2,0.3] # Ticks that will apear on the graph
avectitre = False # True if you want a title on the graph

## PATHS ##
PATHTOFIGUREFOLDER = "/home/c31182/Helmh/Figures/"
PATHTOPROGRAMFOLDER = "/home/c31182/Helmh/Programs/"
PATHTOTEMPFOLDER = "/home/c31182/Helmh/TEMP/"
PATHTOSAVEFOLDER = "/home/c31182/Helmh/ErreursSauvees/"

## PARAMETERS ##
# Program and geometry parameters
typeuinc = 0 # Type of the incident wave (1 : source point, 0 : planar wave)
typecouche = 5 # Type of the thin layer (0 : cos(t - pi), 1 : cos(t - pi/2), 2 : cos(t - 3pi/4), 3 : cos(5t), 4 : cos(-5t), 5 : 1 
debutNptL = 45 # The first measure of the parameter NptL
finNptL = 55 # Final measure of the parameter NptL
Niter = 5 # Number of points in the graph
delta = 0.08 # Thickness of the thin layer
ordre = 1 # Order in delta of the modelisation

# Physical parameter
k = 1
rmup, imup = 0.01,0. # mu in plus domain
repsp, iepsp = 100.,0.1 # epsilon in plus domain
rmum, imum = 0.01,0. # mu in minus domain
repsm, iepsm = 100.,0.1 # epsilon in minus domain
rmuc, imuc = 0.1,0. # mu in the thin layer
repsc, iepsc = 100,0.1 # epsilon in the thin layer

# SAVE AND FIGURE NAME AND PATH#
a = ["1","1","1","5","-5","0"]
b = ["-pi","-pi/2","-3*pi/4","+ pi/2","+ 0","+ 0"]
onde = ["an incident plane","a source point"]
f = "(1 + cos("+a[typecouche]+"t "+b[typecouche]+" )*3/8 + 1/4"
titre = "L2 and H1 relative error between two TLM with different mesh parameters at order "+str(ordre)
savename = "PrecisAsy"+ "delta" + str(delta) + "debutNptL" + str(debutNptL) + "finNptL" + str(finNptL) + "Niter" + str(Niter) + "ordre" + str(ordre) + "typecouche" + str(typecouche)+ "mup"+str(rmup)+"+i"+str(imup)+ "epsp"+str(repsp)+ "+i"+str(iepsp)+"mum"+str(rmum)+"+i"+str(imum)+ "epsm"+str(repsm)+ "+i"+str(iepsm)+"muc"+str(rmuc)+"+i"+str(imuc)+ "epsc"+str(repsc)+ "+i"+str(iepsc)

## CODE ##
## CREATION DES FICHIERS ##
if creation :
	os.system("FreeFem++ "+PATHTOPROGRAMFOLDER+"Helmh_Comparaison_Precision_Asymptotic.edp -wg -typecouche "+ str(typecouche) +" -re "+ str(repsc) +" -ie "+ str(iepsc) +" -rm "+ str(rmuc) +" -im "+ str(imuc) + " -delta "+ str(delta) + " -ecrire " + str(1) + " -debutNptL "+ str(debutNptL)+ " -finNptL "+ str(finNptL) + " -Niter "+ str(Niter)+  " -uinc "+ str(typeuinc) + " -k "+ str(k) +" -rmup "+ str(rmup) +" -imup "+ str(imup) + " -repsp "+ str(repsp)+" -iepsp "+ str(iepsp)+" -rmum "+ str(rmum)+" -imum "+ str(imum)+ " -repsm "+ str(repsm)+" -iepsm "+ str(iepsm) + " -ordre "+str(ordre) + " -PTPF " + PATHTOPROGRAMFOLDER + " -PTTF " + PATHTOTEMPFOLDER)
	os.system("mv "+PATHTOTEMPFOLDER+"Erreur.dat "+PATHTOSAVEFOLDER+"Erreurs_Asymptotic_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_mum_"+str(rmum)+"+i"+str(imum)+"_epsm_"+str(repsm)+"+i"+str(iepsm)+"_mup_"+str(rmup)+"+i"+str(imup)+"_epsp_"+str(repsp)+"+i"+str(iepsp)+"_N_"+str(Niter)+"_debutNptL_"+str(debutNptL)+"_finNptL_"+str(finNptL)+"_delta_"+str(delta)+".txt") ## renome le fichier

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
