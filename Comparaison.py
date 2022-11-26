# coding=utf-8
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as trs

## OPTIONS ##
creation = True # True if you want to calculate the error, False if you just want to manipulate the graph
graph = True	# True if you want to see the graph
log = 1 #1 if you want a log scale, 0 otherwise
savefig = 1 # 1 if you want to save the figure, 0 otherwise
Xticks = [0.03,0.05,0.1,0.2,0.3]
avectitre = False

## PARAMETERS ##
uinc = 0 # Type of the incident wave (1 : source point, 0 : planar wave)
typecouche = 0 # Type of the thin layer (0 : cos(t - pi), 1 : cos(t - pi/2), 2 : cos(t - 3pi/4), 3 : cos(5t), 4 : cos(-5t), 5 : 1 
debutdelta = 0.5 # The first measure of the parameter delta
findelta = 0.005 # The final measure of the parameter delta
Niter = 20 # The number of points in the graph
Nptlambda = 50 # Mesh parameter
ordre = 1 # Order in delta of the modelisation

#Paramètre physique
k = 1
rmup, imup = 0.01,0.
repsp, iepsp = 100.,0.1
rmum, imum = 0.01,0.
repsm, iepsm = 100.,0.1
rmuc, imuc = 0.1,0.
repsc, iepsc = 100,0.1

## CODE ##

# SAVE AND FIGURE NAME#
if typecouche == 0 :
	a = "1"
	b = "-pi"
if typecouche == 1 :
	a = "1"
	b = "-pi/2"
if typecouche == 2 :
	a = "1"
	b = "-3*pi/4"
if typecouche == 3 :
	a = "5"	
	b = "+ pi/2"
if typecouche == 4 :
	a = "-5"
	b = "+ 0"
if typecouche == 5 :
	a = "0"
	b = "+ 0"
f = "(1 + cos("+a+"t "+b+" )*3/8 + 1/4"
if uinc == 1:
	onde = "un point source"
else:
	onde = "une onde incidente plane"
titre = "Erreurs L2 et H1 du modele asymptotique a l ordre "+str(ordre)+" selon delta"
if avectitre :
	savename = "O"+str(ordre)+"_T"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_d_"+str(debutdelta)+"_"+str(findelta)+"_NptL_"+str(Nptlambda) + "_mup_"+str(rmup)+"+i"+str(imup)+ "_epsp_"+str(repsp)+ "+i"+str(iepsp)+"_mum_"+str(rmum)+"+i"+str(imum)+ "_epsm_"+str(repsm)+ "+i"+str(iepsm)
else :
	savename = "O"+str(ordre)+"_T"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_d_"+str(debutdelta)+"_"+str(findelta)+"_NptL_"+str(Nptlambda) + "_mup_"+str(rmup)+"+i"+str(imup)+ "_epsp_"+str(repsp)+ "+i"+str(iepsp)+"_mum_"+str(rmum)+"+i"+str(imum)+ "_epsm_"+str(repsm)+ "+i"+str(iepsm) + "_sans_titre"

# LISTS #

X = []
Yp = []
Yhp = []
Zp = []
Zhp = []
ZpA = []
ZhpA = []
Droite = []
Droite2 = []

# COMPARISON #
if creation :
	os.system("FreeFem++ /home/c31182/Helmh/Helmh_Comparaison_LA_appel.edp -Niter "+str(Niter)+" -debutdelta "+str(debutdelta)+" -findelta "+str(findelta)+" -typecouche "+str(typecouche)+" -re "+str(repsc)+" -ie "+str(iepsc)+" -rm "+str(rmuc)+" -im "+str(imuc)+" -log "+str(log)+" -NptL "+str(Nptlambda)+ " -ordre "+str(ordre)+" -uinc "+str(uinc) + " -k "+ str(k) + " -rmup "+str(rmup) + " -imup "+str(imup)+ " -repsp "+str(repsp) + " -iepsp "+str(iepsp)+ " -rmum "+str(rmum) + " -imum "+str(imum)+ " -repsm "+str(repsm) + " -iepsm "+str(iepsm))
	os.system("mv Erreurs2/Erreur.dat ErreursSauvees/Erreurs_log"+str(log)+"_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_N_"+str(Niter)+"_delta0_"+str(debutdelta)+"_deltan_"+str(findelta)+"_NptL_"+str(Nptlambda)+"_ordre_"+str(ordre)+"_uinc_"+str(uinc)+ "_k_"+ str(k) + "_mup_"+str(rmup)+"+i"+str(imup)+ "_epsp_"+str(repsp)+ "+i"+str(iepsp)+"_mum_"+str(rmum)+"+i"+str(imum)+ "_epsm_"+str(repsm)+ "+i"+str(iepsm)+".txt") ## renome le fichier

# GRAPH #
if graph :
	nom = "ErreursSauvees/Erreurs_log"+str(log)+"_typecouche_"+str(typecouche)+"_muc_"+str(rmuc)+"+i"+str(imuc)+"_epsc_"+str(repsc)+"+i"+str(iepsc)+"_N_"+str(Niter)+"_delta0_"+str(debutdelta)+"_deltan_"+str(findelta)+"_NptL_"+str(Nptlambda)+"_ordre_"+str(ordre)+"_uinc_"+str(uinc)+ "_k_"+ str(k)  + "_mup_"+str(rmup)+"+i"+str(imup)+ "_epsp_"+str(repsp)+ "+i"+str(iepsp)+"_mum_"+str(rmum)+"+i"+str(imum)+ "_epsm_"+str(repsm)+ "+i"+str(iepsm)+".txt"
	#nom = "Erreurs2/Erreur.dat"
	with open(nom,"r") as fichier:
		for ligne in fichier:
			if (ligne != "" and ligne != "\n"):
				if ligne == "end\n":
					continue
				print(ligne)
				l = ligne.split("\n")[0]
				mot,val = l.split(" = ")
				if mot == "Delta" :
					X.append(float(val))
				if mot == "Erreur Plus" :
					Yp.append(float(val))
				if mot == "Erreur H1Plus" :
					Yhp.append(float(val))
				if mot == "Erreur Relative Plus" :
					Zp.append(float(val))
				if mot == "Erreur Relative H1Plus" :
					Zhp.append(float(val))
	Droite = [  Zp[ int(len(X)/2)]*( X[n]/X[int(len(X)/2)])**(ordre+1) for n in range(len(X))]
	if avectitre :	
		plt.title(titre)
	plt.xscale("log")
	plt.yscale('log')
	plt.xticks(Xticks,Xticks)
	plt.xlabel("delta")
	plt.ylabel("error")
	plt.plot(X, Zp, "x", label = "Erreur Relative L2")
	plt.plot(X, Zhp, "x", label = "Erreur Relative H1")
	plt.plot(X, Droite, label = "y = A*x**"+str(ordre + 1 ))
	plt.legend()
	if savefig == 1:
		plt.savefig("/home/c31182/Helmh/Figures/"+savename,format = "eps", dpi = 1200,bbox_inches = "tight")
	plt.show()
