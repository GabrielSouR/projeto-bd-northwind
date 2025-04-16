from controller.pedido_controller import criar_pedido_interativo, criar_pedido_inseguro
from relatorios.pedido_detalhado import exibir_pedido_detalhado
from relatorios.ranking_funcionarios import exibir_ranking_funcionarios
from relatorios.pedido_detalhado_inseguro import exibir_pedido_detalhado_inseguro
from model.pedido_model import Pedido
from datetime import datetime, timedelta

def menu_interativo():
     while True:
        print("\n=== Sistema de Pedidos Northwind ===")
        print("1 - Inserir pedido (modo seguro)")
        print("2 - Inserir pedido (modo vulnerável)")
        print("3 - Relatórios")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            coletar_dados_do_pedido(seguro=True)
        elif escolha == '2':
            coletar_dados_do_pedido(seguro=False)
        elif escolha == '3':
            menu_relatorios()
        elif escolha == '0':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

def coletar_dados_do_pedido(seguro=True):
    print("\n=== Cadastro de Pedido ===")
    modo = "SEGURO" if seguro else "INSEGURO"
    print(f"Modo selecionado: {modo}\n")

    customer_id = input("Customer ID (ex: ALFKI): ").strip()
    employee_id = int(input("Employee ID (ex: 1): "))
    ship_name = input("Nome para entrega (ship name): ").strip()

    order_date = datetime.now()
    required_date = order_date + timedelta(days=7)

    print("\nInforme os itens do pedido (digite 'fim' para encerrar)")
    items = []
    while True:
        product_id = input("ID do produto: ")
        if product_id.lower() == 'fim':
            break
        unit_price = float(input("Preço unitário: "))
        quantity = int(input("Quantidade: "))
        discount = float(input("Desconto (0 a 1): "))
        items.append((int(product_id), unit_price, quantity, discount))

    pedido = Pedido(customer_id, employee_id, order_date, required_date, ship_name, items)

    if seguro:
        criar_pedido_interativo(customer_id, employee_id, order_date, required_date, ship_name, items)
    else:
        criar_pedido_inseguro(customer_id, employee_id, order_date, required_date, ship_name, items)
        
def menu_relatorios():
    print("\n=== Relatórios ===")
    print("1 - Detalhes de um pedido (seguro)")
    print("2 - Ranking de funcionários por período")
    print("3 - Detalhes de um pedido (INSEGURO - simulação de SQL Injection)")
    print("0 - Voltar ao menu principal")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        order_id = int(input("Digite o número do pedido: "))
        exibir_pedido_detalhado(order_id)

    elif escolha == '2':
        data_inicio = input("Data de início (YYYY-MM-DD): ")
        data_fim = input("Data de fim (YYYY-MM-DD): ")
        try:
            data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
            data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()
            exibir_ranking_funcionarios(data_inicio, data_fim)
        except ValueError:
            print("Datas em formato inválido. Use YYYY-MM-DD.")

    elif escolha == '3':
        entrada = input("Digite o número do pedido (ou tente uma injeção): ")
        exibir_pedido_detalhado_inseguro(entrada)

    elif escolha == '0':
        return
    else:
        print("Opção inválida.")

