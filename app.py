import pyodbc


server = 'DESKTOP-HNL7NA6'  
database = 'NomeDoSeuBancoDeDados'  
username = 'Rodolfo Arnaut'  
password = 'Aulabil@2023'

# Estabelecer conexão com o banco de dados
try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

    print("Conexão estabelecida com sucesso.")

except pyodbc.Error as e:
    print("Erro na conexão com o banco de dados:", e)


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def inserir_dados(nome, endereco, altura, peso):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Pacientes (Nome, Endereco, Altura, Peso) VALUES (?, ?, ?, ?)", nome, endereco, altura, peso)
        conn.commit()
        print("Dados inseridos com sucesso.")
    except pyodbc.Error as e:
        print("Erro ao inserir dados no banco de dados:", e)
        conn.rollback()
    finally:
        cursor.close()

def calcular_e_armazenar_imc():
    nome = input("Digite o nome do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    altura = float(input("Digite a altura do paciente em metros: "))
    peso = float(input("Digite o peso do paciente em kg: "))
    
    imc = calcular_imc(peso, altura)
    print(f"O IMC do paciente é: {imc:.2f}")

    inserir_dados(nome, endereco, altura, peso)


calcular_e_armazenar_imc()


conn.close()
