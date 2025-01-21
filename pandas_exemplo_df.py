import pandas as pd

class exemplo:
    data = {
        'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Idade': [25,30,35,40,27],
        'Cargo': ['Analista', 'Gerente', 'CEO', 'Coordenador', 'Analista'],
        'Salario': [5000, 8000, 15000, 7000, 4800]
    }
    dataframe = pd.DataFrame(data)

    def lineBreak():
        print('\nx ------ x ------ x ------ x ------ x\n')