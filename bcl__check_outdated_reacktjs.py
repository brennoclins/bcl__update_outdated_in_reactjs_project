import os
import subprocess

# Verifica se o arquivo package.json existe
if not os.path.isfile("package.json"):
    print("Arquivo package.json não encontrado. Certifique-se de estar no diretório do projeto.")
    exit(1)

# Verifica se o diretório node_modules existe
if not os.path.isdir("node_modules"):
    print("Diretório node_modules não encontrado. Instalando as dependências...")
    subprocess.run(["npm", "install"])

print("Verificando dependências desatualizadas")
subprocess.run(["npm", "outdated"])
