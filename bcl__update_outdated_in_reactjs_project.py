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

print("Atualizando as dependências")
subprocess.run(["npm", "update"])

print("Verificando se houve atualizações")
subprocess.run(["npm", "outdated", "--json"])

# Se houver atualizações, realiza o commit
if outdated != updated:
    print("Realizando commit das atualizações")
    subprocess.run(["git", "add", "package.json", "package-lock.json"])
    subprocess.run(["git", "commit", "-m", "update: Atualização de dependências [Updating dependencies]"])

print("Dependências atualizadas:")
print(updated)
