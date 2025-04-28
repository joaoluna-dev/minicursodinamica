#by joao gabriel - Neuroimmunogenetics Lab (iLIKA)
#gets a PDB file from the RCSB PDB database
#Requirements: requests module (pip install requests)

import requests
import os
import sys

#--------------------------------------------Function-----------------------------------------------#

def get_pdb(file, code):
    # download of the pdb file
    url = f"https://files.rcsb.org/download/{code}.pdb"
    r = requests.get(url)
    with open(file, "w") as pdb:
        pdb.write(r.text)

#--------------------------------------------Values----------------------------------------------#

if len(sys.argv) < 1:
    print("Error: Insufficient arguments. Usage: python get_pdb.py pdb_ID")
    sys.exit(1)

protein_code = sys.argv[1]

#-----------------------------------------Main Script----------------------------------------------#
try:
    pdb_file = f"{protein_code}.pdb"
    get_pdb(pdb_file, protein_code)
    print(f"{protein_code}.pdb file downloaded")
except Exception as e:
    print(f"An unexpected error has ocurred: {e} \n ")
