# coding=utf-8

#####################################################################################
# This program compares the asymptotic model (AM) and the thin layer model (TLM).
# README files explains precisely which equations are studied.
# The goal is to draw a graph of the relative error between both models
# following the thin layer thickness "delta0".
# To work it requires the following programs :
# - Helmh_Comparaison_appel.edp
# - Helmh_Comparaison_comparaison.edp (PETS-c code)
# - Helmh_delta.edp (PETS-c code)
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
uinc = 0 # Type of the incident wave (1 : source point, 0 : planar wave)
typecouche = 0 # Type of the thin layer (0 : cos(t - pi), 1 : cos(t - pi/2), 2 : cos(t - 3pi/4), 3 : cos(5t), 4 : cos(-5t), 5 : 1
debutdelta = 0.5 # First measure of the parameter delta (thickness of the thin layer)
findelta = 0.005 # Final measure of the parameter delta
Niter = 20 # Number of points in the graph
Nptlambda = 50 # Mesh parameter
ordre = 1 # Asymptotical order in delta of the modelisation

# Physical parameter
k = 1
rmup, imup = 1.,0. # mu in plus domain
repsp, iepsp = 1.,0.1 # epsilon in plus domain
rmum, imum = 1.,0. # mu in minus domain
repsm, iepsm = 1.,0.1 # epsilon in minus domain
rmuc, imuc = 10.,0. # mu in the thin layer
repsc, iepsc = 3.,0.1 # epsilon in the thin layer

# SAVE AND FIGURE NAME AND PATH
# (Only for the saving name, it does not change anything on the result)
a = ["1","1","1","5","-5","0"]
b = ["-pi","-pi/2","-3*pi/4","+ pi/2","+ 0","+ 0"]
onde = ["an incident plane","a source point"]
f = "(1 + cos("+a[typecouche]+"t "+b[typecouche]+" )*3/8 + 1/4"
titre = "L2 and H1 relative error between TLM and AM at order "+str(ordre)+" following delta"
savename = "O"+str(ordre)+"_T"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_d_"+str(debutdelta)+"_"+str(findelta)+"_NptL_"+str(Nptlambda) + "_mup_"+str(rmup)+"+i"+str(imup)+ "_epsp_"+str(repsp)+ "+i"+str(iepsp)+"_mum_"+str(rmum)+"+i"+str(imum)+ "_epsm_"+str(repsm)+ "+i"+str(iepsm)


## COMPARISON ##
# Execution of the sub-program
if creation :
	os.system("FreeFem++ "+PATHTOPROGRAMFOLDER+"Helmh_Comparaison_appel.edp -Niter "+str(Niter)+" -debutdelta "+str(debutdelta)+" -findelta "+str(findelta)+" -typecouche "+str(typecouche)+" -re "+str(repsc)+" -ie "+str(iepsc)+" -rm "+str(rmuc)+" -im "+str(imuc)+" -NptL "+str(Nptlambda)+ " -ordre "+str(ordre)+" -uinc "+str(uinc) + " -k "+ str(k) + " -rmup "+str(rmup) + " -imup "+str(imup)+ " -repsp "+str(repsp) + " -iepsp "+str(iepsp)+ " -rmum "+str(rmum) + " -imum "+str(imum)+ " -repsm "+str(repsm) + " -iepsm "+str(iepsm) + " -PTPF " + str(PATHTOPROGRAMFOLDER) + " -PTTF " + str(PATHTOTEMPFOLDER))
	os.system("mv "+PATHTOTEMPFOLDER+"Erreur.dat "+PATHTOSAVEFOLDER+"Erreurs_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_N_"+str(Niter)+"_delta0_"+str(debutdelta)+"_deltan_"+str(findelta)+"_NptL_"+str(Nptlambda)+"_ordre_"+str(ordre)+"_uinc_"+str(uinc)+ "_k_"+ str(k) + "_mup_"+str(rmup)+"+i"+str(imup)+ "_epsp_"+str(repsp)+ "+i"+str(iepsp)+"_mum_"+str(rmum)+"+i"+str(imum)+ "_epsm_"+str(repsm)+ "+i"+str(iepsm)+".txt") ## renome le fichier

## GRAPH ##
# Creation of the graph
Listes = [[],[],[],[],[]]
if graph :
	nom = PATHTOSAVEFOLDER+"Erreurs_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_N_"+str(Niter)+"_delta0_"+str(debutdelta)+"_deltan_"+str(findelta)+"_NptL_"+str(Nptlambda)+"_ordre_"+str(ordre)+"_uinc_"+str(uinc)+ "_k_"+ str(k)  + "_mup_"+str(rmup)+"+i"+str(imup)+ "_epsp_"+str(repsp)+ "+i"+str(iepsp)+"_mum_"+str(rmum)+"+i"+str(imum)+ "_epsm_"+str(repsm)+ "+i"+str(iepsm)+".txt"
	Mots = ["Delta","Erreur Plus","Erreur H1Plus","Erreur H1Plus","Erreur Relative Plus","Erreur Relative H1Plus"]
	with open(nom,"r") as fichier:
		for ligne in fichier:
			if (ligne != "" and ligne != "\n"):
				if ligne == "end\n":
					continue
				l = ligne.split("\n")[0]
				mot,val = l.split(" = ")
				if mot in Mots:
					Listes[Mots.index(mot)].append(val)
	Droite = [  Listes[3][ int(len(Listes[0])/2)]*( Listes[0][n]/Listes[0][int(len(Listes[0])/2)])**(ordre+1) for n in range(len(Listes[0]))]
	if avectitre : plt.title(titre)
	plt.xscale("log")
	plt.yscale('log')
	plt.xticks(Xticks,Xticks)
	plt.xlabel("delta")
	plt.ylabel("error")
	plt.plot(Listes[0], Listes[3], "x", label = "L2 Relative Error")
	plt.plot(Listes[0], Listes[4], "x", label = "H1 Relative Error")
	plt.plot(Listes[0], Droite, label = "y = A*x**"+str(ordre + 1 ))
	plt.legend()
	if savefig == 1: plt.savefig(PATHTOFIGUREFOLDER+savename,format = "eps", dpi = 1200,bbox_inches = "tight")
	plt.show()
