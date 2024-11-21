
from sys import *
from os import system, chdir, getcwd

fichier = open( "RNA.pdb" , "r" )
atomes = fichier.readlines()
#print(atomes)
fichier.close()
output = []
for atome in atomes:
    if (atome[-1]=='H' or atome[-4]=='H') and ("U" in atome) and ("H5 " in atome):
        line = atome.split('   ')
        line[1] = line[1][:-2] + 'C7'
        line[-1] = '  C \n'
        atome = '   '.join(line)
    if "U" in atome:
        atome = atome[:19]+'T'+atome[20:]	
    output.append(atome)
fichier = open( "pre-DNA1.pdb", "w" )
fichier.writelines(output)
fichier.close()

# Programme to delete lines matching an atom
atom_to_remove = ["O2'"]

with open('pre-DNA1.pdb','r') as oldfile, open('pre-DNA2.pdb', 'w') as newfile:
    for line in oldfile:
        if not any( atom_to_remove in line for atom_to_remove in atom_to_remove):
            newfile.write(line)
 
# programme to replace 'N' with 'DN'  
from biopandas.pdb import PandasPdb
ppdb = PandasPdb()
ppdb.read_pdb('pre-DNA2.pdb')
data=ppdb.df['ATOM']
data["residue_name"]=data["residue_name"].replace(['A'], 'DA')
data["residue_name"]=data["residue_name"].replace(['T'], 'DT')
data["residue_name"]=data["residue_name"].replace(['G'], 'DG')
data["residue_name"]=data["residue_name"].replace(['C'], 'DC')

ppdb.to_pdb(path='DNA.pdb')

