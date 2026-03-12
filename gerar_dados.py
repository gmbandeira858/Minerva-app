import pandas as pd
import random
from datetime import datetime, timedelta

# nomes masculinos
nomes = [
    "Carlos","João","Pedro","Lucas","Marcos","Felipe",
    "André","Rafael","Daniel","Gustavo","Henrique","Eduardo"
]

# nomes femininos
nomes_femininos = [
    "Ana","Maria","Juliana","Fernanda","Carla","Patricia",
    "Camila","Larissa","Beatriz","Gabriela"
]

# sobrenomes para compor
sobrenomes = [
    "Silva","Souza","Oliveira","Santos","Ferreira","Costa",
    "Rodrigues","Almeida","Barbosa","Gonçalves","Cardoso",
    "Teixeira","Mendes","Araújo"
]

enderecos = [
    "Rua das Flores","Av. Brasil","Rua Goiás","Rua Central",
    "Av. Independência","Rua 7","Rua 10","Av. Tocantins"
]

estados_civis = ["Solteiro","Casado","Divorciado"]

def nome_completo():
    return f"{random.choice(nomes)} {random.choice(sobrenomes)} {random.choice(sobrenomes)}"

def nome_feminino():
    return f"{random.choice(nomes_femininos)} {random.choice(sobrenomes)} {random.choice(sobrenomes)}"

def data_aleatoria(inicio, fim):
    delta = fim - inicio
    dias = random.randint(0, delta.days)
    return inicio + timedelta(days=dias)

dados = []

for i in range(25):

    estado = random.choice(estados_civis)

    nome = nome_completo()
    nascimento = data_aleatoria(datetime(1960,1,1), datetime(2000,12,31)).date()

    cim = random.randint(100000,999999)
    endereco = random.choice(enderecos) + ", " + str(random.randint(1,999))
    telefone = "(62) 9" + str(random.randint(1000,9999)) + "-" + str(random.randint(1000,9999))

    esposa = ""
    cunhada = ""

    if estado == "Casado":
        esposa = nome_feminino()
        cunhada = data_aleatoria(datetime(1965,1,1), datetime(2005,12,31)).date()

    filhos = random.randint(0,5)

    filhos_nomes = []
    filhos_datas = []

    for f in range(filhos):
        filhos_nomes.append(nome_completo())
        filhos_datas.append(data_aleatoria(datetime(2005,1,1), datetime(2023,12,31)).date())

    while len(filhos_nomes) < 5:
        filhos_nomes.append("")
        filhos_datas.append("")

    linha = {
        "CIM": cim,
        "Nome Completo": nome,
        "Data de Nascimento": nascimento,
        "Endereço": endereco,
        "Telefone": telefone,
        "Estado Civil": estado,
        "Nome da Esposa": esposa,
        "Data Nascimento Cunhada": cunhada,
        "Quantidade de Filhos": filhos,
        "Filho 1": filhos_nomes[0],
        "Nascimento Filho 1": filhos_datas[0],
        "Filho 2": filhos_nomes[1],
        "Nascimento Filho 2": filhos_datas[1],
        "Filho 3": filhos_nomes[2],
        "Nascimento Filho 3": filhos_datas[2],
        "Filho 4": filhos_nomes[3],
        "Nascimento Filho 4": filhos_datas[3],
        "Filho 5": filhos_nomes[4],
        "Nascimento Filho 5": filhos_datas[4]
    }

    dados.append(linha)

df = pd.DataFrame(dados)

df.to_csv("cadastro_homens.csv", index=False)

print("CSV gerado com sucesso: cadastro_homens.csv")

print("Planilha gerada com sucesso: cadastro_homens.xlsx")
