import os

restaurantes = [{"nome":"Praça", "categoria": "Japonesa", "ativo":False }, 
                {"nome":"Pizza Suprema", "categoria": "Pizza",
                 "ativo": True},
                 {"nome":"Cantina","categoria":"Italiano", "ativo":False}]

def exibir_nome_do_programa():
    print("""
 ██████╗ █████╗ ██████╗  █████╗ ██████╗   ███████╗██╗  ██╗██████╗ ██████╗ ███████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗ ███████║██████╦╝██║  ██║██████╔╝  █████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ╚█████╗ ╚█████╗ 
 ╚═══██╗██╔══██║██╔══██╗██║  ██║██╔══██╗  ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝   ╚═══██╗ ╚═══██╗
██████╔╝██║  ██║██████╦╝╚█████╔╝██║  ██║  ███████╗██╔╝╚██╗██║     ██║  ██║███████╗██████╔╝██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝  ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ """)

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Alternar estado do Restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizar App")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu ")
    main()


def opcao_invalida():
    print("Opção Inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system("clear")
    linha = "*" * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


 # Função Responsavel por cadastrar novos Restaurantes e suas categorias 

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos Restaurantes")
    nome_do_restaurante = input("Digite o nome do Restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do Restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome" :nome_do_restaurante, "categoria" :categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
     
    
    voltar_ao_menu_principal()

# Função que lista os Restaurantes cadastrados 

def listar_restaurantes():
    exibir_subtitulo("listando Restaurantes")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    
    voltar_ao_menu_principal()


# Função para Alterar o estado do Restaurante, se está ativo ou desativado 

def alernar_estado_restaurante():
    exibir_subtitulo("Alterando estado do Restaurante")
    nome_restaurante = input("Digite o nome do Restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O Restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"]else f"O Restaurante foi desativado com sucesso!"
            print(mensagem)
    
    if not restaurante_encontrado:
        print("O Restaurante não foi encontrado")

    voltar_ao_menu_principal()       


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alernar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("clear")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
