from openbabel import pybel
import subprocess, os
print("Read the following carefully")
print("This code takes SMILES as input and all the functionals you want to use to run a MOPAC calculation on the structure")
print("This code uses openbabel and pybel to convert smiles into xyz, if you dont have openbabel and pybel, please install it before continuing")
print("This code also assumes that you have mopac on your system and its added in your bashrc like the following: export PATH='$PATH:/opt/mopac/bin'")
print("The code will ask you for the numkber of structures you want to do the calculation on and you then have to name all the structures and give the Smiles as asked.")
print("Then specify all the functionals you want to use for the calculation")
​
​
User_input = int(input('How many structures are you doing the calculation on?'))
dict_of_structure = {}
for i in range(0,User_input):
    structure_name = input('Input the name for the structure: ' )
    print("\n")
    structure = str(input('SMILES for the Structure: '))
    print("\n")
    dict_of_structure[structure_name] = structure
​
print('Structure dictionary:\n' , dict_of_structure)
functional_you_want_to_use = int(input('How many functionals you want to use for the optimization?'))
lst = []
for j in range(0,functional_you_want_to_use):
	ele = input(str(j) + ' Functional?:')
	lst.append(ele)
​
print('Functional list:', lst)
​
	    
​
def get_key(val, my_dict):
    for key, value in my_dict.items():
        # print(val,value)
        if val == value:
            # print(val)
            return key
        else:
            continue

            
##############Changing the structures into MOP files for MOPAC input generation###########
def SMILES_to_XYZ(smile_structure):
    struc = smile_structure
    mymol = pybel.readstring("smi", struc) ## Takes in the Smile structure and converts it into a 3D structure
    mymol.make3D()
    mymol.write("mop",  "a.mop",overwrite=True) ## this generates a MOPAC compatible intpu file, this file is not yet ready for submitting a MOPAC job
##############Changing the MOPAC file to accomodate the functional we want to use?###########
def generate_MOPAC_input_with_functional(abc, functional):
   my_file = open("a.mop", "r")
   string_list = my_file.readlines()
   print(string_list[0])
   string_list[0] = "AUX LARGE CHARGE=0 SINGLET  "+ functional+ "\n"
   my_file.close()
   subprocess.call(['rm', '-rf', 'a.out'])
   readable_file = open(abc+".mop", "x")
   new_file_contents = "".join(string_list)
   readable_file.write(new_file_contents)
   readable_file.close()

  
####MAIN#######
tmp_cwd = os.getcwd()
for k in dict_of_structure.values():
	os.chdir(tmp_cwd)
	os.mkdir(get_key(k,dict_of_structure))
	os.chdir(tmp_cwd+'/'+get_key(k,dict_of_structure))
	for p in lst:
		os.chdir(tmp_cwd+'/'+get_key(k,dict_of_structure))
		os.mkdir(p)
		os.chdir(tmp_cwd+'/'+get_key(k,dict_of_structure)+'/'+p)
		SMILES_to_XYZ(k)
		generate_MOPAC_input_with_functional(get_key(k,dict_of_structure),p)
		subprocess.call(['mopac', get_key(k,dict_of_structure)+'.mop'])
