#by joao gabriel - Neuroimmunogenetics Lab (iLIKA)


import sys
import os

#-----------------------------------------Functions-------------------------------------------#

def remove_molecules(inpt, outpt, mol):
    mol_set = set(mol)
    with open(inpt, "r") as infile, open(outpt, "w") as outfile:
        for line in infile:
            keep_line = True
            splitting = line.split(" ")
            for element in splitting:
                if element not in mol_set:
                    continue
                else:
                    keep_line = False
            if keep_line:
                outfile.write(line)


def get_molecules_list(res_names):
    return res_names.split(",")

#--------------------------------------------Values--------------------------------------------#

if len(sys.argv) < 3:
    print("Error: Insufficient arguments. Usage: python treatment.py pdb_ID filename")
    sys.exit(1)


protein_code = sys.argv[1]
input_file = sys.argv[2]
workspace = os.path.dirname(os.path.abspath(__file__))
output_file = f"{protein_code}_treated.pdb"
residues_removed = False

#---------------------------------------Main Script--------------------------------------------#

while True:
    selection_residue = input("Do you want to remove anything from the file? (y/n): ")
    if selection_residue == "y":
        residues_name = input("Insert molecule or molecules name, separated by a comma: ")
        molecule = get_molecules_list(residues_name)
        remove_molecules(input_file, output_file, molecule)
        residues_removed = True
        print(f"Treated file saved as {output_file}.")
    elif selection_residue == "n":
        break


