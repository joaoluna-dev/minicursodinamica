# by joao gabriel = Neuroimmunogenetics lab (iLIKA)
#Separate ligand info from target protein, and write that in a new PDB file.
import sys
#----------------------------------------------------------Values--------------------------------------------------------------#

if len(sys.argv) < 3:
    print("Insufficient arguments. Usage: python separator.py ligand pdb_ID filename")
    sys.exit(1)

ligand = sys.argv[1]
protein_code = sys.argv[2]
input_file = sys.argv[3] 
output_ligand = f"{ligand}.pdb"
output_protein = f"{protein_code}_without_{ligand}.pdb"

#-------------------------------------------------------Main Script------------------------------------------------------------#

with open(input_file, "r") as input_file, open(output_ligand, "w") as output_ligand, open(output_protein, "w") as output_protein:
    read = input_file.readlines()
    for i in read:
        if ligand in i:
            output_ligand.write(i)
        else:
            output_protein.write(i)

print("Protein and ligand were successfully separated.")

