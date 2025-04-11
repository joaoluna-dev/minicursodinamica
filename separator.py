#Neuroimmunogenetics lab - iLIKA UFPE
#Separate ligand info from target protein, and write that in a new pdb file.
import sys
from pathlib import Path
import os

ligand = sys.argv[1]
input_file = sys.argv[2] 
output_ligand = sys.argv[3]
output_protein = sys.argv[4]

with open(input_file, "r") as input_file, open(output_ligand, "w") as output_ligand, open(output_protein, "w") as output_protein:
    read = input_file.readlines()
    for i in read:
        if ligand in i:
            output_ligand.write(i)
        else:
            output_protein.write(i)

print("Separação entre ligante e proteína executada.")

