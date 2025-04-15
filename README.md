# 💻🧪 minicursodinamica
BR: Repositório de arquivos para o minicurso de dinâmica molecular, ministrado pelos integrantes do laboratório de Neuroimunogenética, na UFPE. 

EN: File repository for the molecular dynamics mini-course, taught by members of the Neuroimmunogenetics laboratory at UFPE.

## 🌟 Highlights /  Destaques

- Improve analysis, by automating some tasks (get pdbs, treat them..) / Melhora a análise, por meio da automatização de algumas tarefas (obter pbds, trata-los...)
- Ready-to-go mdp files / Arquivos mdp prontos 


## ℹ️ Overview / Visão geral

I'm a biomedical scientist, working in Data science, computational biology, and genomics. This tool is made for scientists who want to learn and apply their knowledge on molecular dynamics, facilitating their understanding. Sou Biomedico, trabalhando em ciência de dados, biologia computacional e genômica. Esta ferramenta é feita para cientistas que desejam aprender e aplicar seu conhecimento em dinâmica molecular, facilitando sua compreensão.

### ✍️ Authors / Autores

João Gabriel: https://github.com/joaoluna-dev
https://www.ufpe.br/ilika

## 🚀 Usage / Uso

### 📄 mdp files 
you can use the pre-configured (mini-course only) or the base files, which have no parameters inserted / você pode usar os arquivos pré-configurados (apenas no mini-curso) ou os arquivos base, que não têm parâmetros inseridos.

### 🐍 Python files
- go to the files folder, and run the following command lines on the terminal / vá para a pasta com os arquivos, e execute as seguintes linhas de comando no terminal
- get_pdb.py
```bash
>>> python get_pdb.py pdb_ID
# obtains a pdb file from the RCSB database / obtém um arquivo pdb do banco de dados do RCSB
```
- treatment.py
```bash
>>> python treatment.py pdb_ID filename
# removes specified molecules from the file / remove moléculas especificadas do arquivo
```
- separator.py
```bash
>>> python separator.py ligand pdb_ID filename
# separates a ligand from a protein in the specified file / separa o ligante da proteína do arquivo especificado
```


## ⬇️ Installation

- You can mannualy download the files from the repository / Você pode baixar os arquivos do repositório manualmente
- Clone the repo by a git command / Clone o repositório por meio do comando git
```bash
gh repo clone joaoluna-dev/minicursodinamica 
```

### 🛠️ Requirements / Requisitos:
- Python 3.x
- requests (for the get_pdb.py script / para o script get_pdb.py)
```bash
pip install requests 
```
