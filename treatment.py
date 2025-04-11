import sys
import subprocess
import os
from main import log_write

if len(sys.argv) < 3:
    print("Erro: Argumentos insuficientes.")
    sys.exit(1)

workspace = sys.argv[1]
protein_code = sys.argv[2]
input_file = sys.argv[3]
output_file = sys.argv[4]

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if "HOH" not in line:
            outfile.write(line)
log_write("Arquivo tratado para a remoção de resíduos de água.", "info")
print(f"Arquivo tratado para remoção de água salvo como {protein_code}_tratado.pdb.")

while True:
    try:
        selection_HETATM = input("Você deseja remover algo a mais? (y/n): ").lower()    
        if selection_HETATM == "y":
            resn = input("Insira o nome do resíduo a ser removido: ")
            input_file_2 = output_file
            output_file_2 = os.path.join(workspace, f"{protein_code}_tratado_{resn}.pdb")
            with open(output_file, "r") as infile, open(output_file_2, "w") as outfile:
                for line in infile:
                    if f"{resn}" not in line:
                        outfile.write(line)
                with open('logs.txt', 'a') as log:
                    log_write("Usuário solicitou remoção de resíduo", "info")
                    log_write(f"Arquivo tratado para a remoção de {resn} e salvo como {output_file_2}.", "info")
                print(f"Arquivo tratado salvo como {protein_code}_tratado_{resn}.pdb.")
            break
        elif selection_HETATM == "n":
            break
        else:
            print("Entrada inválida. Tente novamente.")
            log_write(f"Entrada inserida inválida para a seleção de heteroátomo", "erro")
    except ValueError:
        log_write("Entrada inválida inserida.", "erro")
        print("Entrada inválida. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        log_write(f"{e}", "erro")
        print("Erro adicionado ao log do sistema.")

