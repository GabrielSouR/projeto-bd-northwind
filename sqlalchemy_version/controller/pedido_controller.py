from sqlalchemy_version.config.conexao import SessionLocal
from sqlalchemy_version.model.pedido import Pedido
from sqlalchemy_version.model.item_pedido import ItemPedido
from datetime import datetime, timedelta

def criar_pedido_sqlalchemy():
    session = SessionLocal()

    customer_id = input("Customer ID (ex: MEREP): ")
    employee_id = int(input("Employee ID (ex: 1): "))
    ship_name = input("Nome para entrega: ")

    order_date = datetime.now()
    required_date = order_date + timedelta(days=7)

    pedido = Pedido(
        customerid=customer_id,
        employeeid=employee_id,
        orderdate=order_date,
        requireddate=required_date,
        shipname=ship_name
    )

    print("\nItens do pedido (digite 'fim' para encerrar):")
    while True:
        product_id = input("ID do produto: ")
        if product_id.lower() == 'fim':
            break
        unit_price = float(input("Preço unitário: "))
        quantity = int(input("Quantidade: "))
        discount = float(input("Desconto (0 a 1): "))

        item = ItemPedido(
            productid=int(product_id),
            unitprice=unit_price,
            quantity=quantity,
            discount=discount
        )
        pedido.itens.append(item)

    session.add(pedido)
    session.commit()
    print(f"Pedido {pedido.orderid} inserido com sucesso (SQLAlchemy)!")
    session.close()
