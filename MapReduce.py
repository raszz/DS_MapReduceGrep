import re
from threading import Thread
from collections import defaultdict

class MapReduceController:
    def __init__(self, mapper, reducer, pattern=None, use_regex=False):
        self.mapper = mapper
        self.reducer = reducer
        self.pattern = pattern
        self.use_regex = use_regex
        self.intermediate_results = defaultdict(list)

    def map_reduce(self, files):
        # Inicia uma thread para cada arquivo
        threads = []
        for file_name in files:
            t = Thread(target=self.map_file, args=(file_name,))
            threads.append(t)
            t.start()

        # Espera todas as threads terminarem
        for t in threads:
            t.join()

        # Escreve os resultados intermediários apenas uma vez, após o mapeamento completo
        self.write_intermediate_results_to_file()

        # Inicia uma thread para cada chave e valores intermediários
        reduce_threads = []
        for word, lines in self.intermediate_results.items():
            t = Thread(target=self.reduce_wrapper, args=(word, lines))
            reduce_threads.append(t)
            t.start()

        # Espera todas as threads de redução terminarem
        for t in reduce_threads:
            t.join()

        # Salva o resultado em um arquivo
        self.save_result()

    def map_file(self, file_name):
        # Realiza a função map no arquivo
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if self.use_regex:
                    if re.search(self.pattern, line):
                        self.intermediate_results[file_name].append((i+1, line))
                else:
                    if self.pattern in line:
                        self.intermediate_results[file_name].append((i+1, line))

    def reduce_wrapper(self, file_name, lines):
        # Chama a função de redução
        reduced_result = self.reducer(file_name, lines)
        self.intermediate_results[file_name] = reduced_result

    def write_intermediate_results_to_file(self):
        # Grava os resultados intermediários em um único arquivo de texto
        with open("intermediate_results.txt", 'w') as f:
            for file_name, lines in self.intermediate_results.items():
                for line_num, line in lines:
                    f.write(f"{file_name} - Line {line_num}: {line}\n")

    def save_result(self):
        # Salva o resultado em um arquivo de texto
        with open("grep_result.txt", 'w') as f:
            for file_name, lines in self.intermediate_results.items():
                for line_num, line in lines:
                    f.write(f"{file_name} - Line {line_num}: {line}\n")


# Função de redução
def grep_reducer(file_name, lines):
    return lines

# Exemplo de uso
files = ["input0.txt", "input1.txt", "input2.txt", "input3.txt"]
 # Padrão a ser Buscado  
pattern = "cbb$"

# Define o uso das expressões regulares: 
use_regex = True 
# True para usar regex
# False Para busca simples, sem regex

controller = MapReduceController(None, grep_reducer, pattern=pattern, use_regex=use_regex)
controller.map_reduce(files)