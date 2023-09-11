import create_script.execute
import create_script.words
import create_script.translate_file
import utils.clear
import automate

index=1
modulo="01"
directory = "C:/Users/shust/OneDrive/Inglês Conversação/" 
export = f"{directory}Modulo {modulo}/"
roteiro = f"{export}roteiro/"
bkp = f"{export}bkp/"
path = f"{roteiro}aula{index}modulo{modulo}.txt"
gerados = export+"gerados/"
phrases = f"{directory}/phrases.txt"

print(f"{directory}\n{roteiro}\n{path}\n{export}")

#utils.clear.clear_folder(roteiro,bkp)
#create_script.execute.process(path=phrases,bkp=roteiro,increment=True,module=modulo,index=index)
#create_script.translate_file.translate_lines(roteiro)
automate.automate_roteiros(export,gerados)