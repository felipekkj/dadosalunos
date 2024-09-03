import pickle

def load_data():
    try:
        with open('alunos.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('alunos.pkl', 'wb') as f:
        pickle.dump(data, f)

def add_aluno(alunos):
    nome = input("Nome: ")
    data_nasc = input("Data de Nascimento (dd/mm/aaaa): ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    
    if email in alunos:
        print("Aluno já cadastrado!")
        return
    
    alunos[email] = {
        'nome': nome,
        'data_nasc': data_nasc,
        'telefone': telefone,
        'endereco': endereco
    }
    print("Aluno adicionado com sucesso!")
def listar_aluno(alunos):
    email = input("Digite o e-mail do aluno: ")
    if email in alunos:
        aluno = alunos[email]
        print(f"Nome: {aluno['nome']}")
        print(f"Data de Nascimento: {aluno['data_nasc']}")
        print(f"Telefone: {aluno['telefone']}")
        print(f"Endereço: {aluno['endereco']}")
    else:
        print("Aluno não encontrado!")

def listar_todos_alunos(alunos):
    if alunos:
        for email, info in alunos.items():
            print(f"\nE-mail: {email}")
            print(f"Nome: {info['nome']}")
            print(f"Data de Nascimento: {info['data_nasc']}")
            print(f"Telefone: {info['telefone']}")
            print(f"Endereço: {info['endereco']}")
    else:
        print("Nenhum aluno cadastrado!")

def atualizar_endereco(alunos):
    email = input("Digite o e-mail do aluno: ")
    if email in alunos:
        novo_endereco = input("Digite o novo endereço: ")
        alunos[email]['endereco'] = novo_endereco
        print("Endereço atualizado com sucesso!")
    else:
        print("Aluno não encontrado!")

def main():
    alunos = load_data()
    
    while True:
        print("\n1 - Adicionar aluno")
        print("2 - Listar aluno")
        print("3 - Listar todos os alunos")
        print("4 - Atualizar endereço do aluno")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            add_aluno(alunos)
        elif opcao == '2':
            listar_aluno(alunos)
        elif opcao == '3':
            listar_todos_alunos(alunos)
        elif opcao == '4':
            atualizar_endereco(alunos)
        elif opcao == '5':
            save_data(alunos)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
