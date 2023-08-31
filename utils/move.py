import subprocess

# O comando que você deseja executar
comando = "ls -l"

# Executa o comando e captura a saída
saida = subprocess.check_output(comando, shell=True, text=True)

# Imprime a saída
print(saida)
