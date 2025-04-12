import sys
from main import log_write, json_write

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

#----------------------------------------------------------------------------------------------#

def get_molecules_list(res_names):
    return res_names.split(",")

#-----------------------------------------------------------------------------------------------#

if len(sys.argv) < 3:
    print("Error: Insufficient arguments.")
    sys.exit(1)

workspace = sys.argv[1]
protein_code = sys.argv[2]
input_file = sys.argv[3]
output_file = sys.argv[4]

residues_removed = False

while True:
    selection_residue = input("Do you want to remove anything from the file? (y/n): ")
    if selection_residue == "y":
        residues_name = input("Insert molecule or molecules name, separated by a comma: ")
        molecule = get_molecules_list(residues_name)
        remove_molecules(input_file, output_file, molecule)
        residues_removed = True
        log_write("Residues removed", "info")
        print(f"Treated file saved as {output_file}.")
        log_write(f"Treated file saved as {output_file}", "info")
    elif selection_residue == "n":
        break

json_write({"Molecules were removed:": residues_removed})
json_write({"Molecules removed": molecule})
