# MOPAC_Calculation_from_SMILES
Use this code if you want to do a MOPAC calculation with just the SMILES of the structure

This code takes SMILES as input and all the functionals you want to use to run a MOPAC calculation on the structure. 

This code uses openbabel and pybel to convert smiles into xyz, if you dont have openbabel and pybel, please install it before continuing. 

Installing openbabel : http://openbabel.org/wiki/Category:Installation 
Installing pybel : pip install pybel 


This code also assumes that you have mopac on your system(Download MOPAC: http://openmopac.net/downloads.html) and its added in your bashrc/bash_profile like the following: export PATH='$PATH:/opt/mopac/bin'


The code will ask you for the numkber of structures you want to do the calculation on and you then have to name all the structures and give the Smiles as asked.

Then specify all the functionals you want to use for the calculation. 
