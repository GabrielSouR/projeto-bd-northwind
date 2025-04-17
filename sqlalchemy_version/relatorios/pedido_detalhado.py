from sqlalchemy_version.config.conexao import SessionLocal
from sqlalchemy import select
from sqlalchemy_version.model.pedido import Pedido
from sqlalchemy_version.model.item_pedido import ItemPedido
from sqlalchemy_version.model import pedido, item_pedido

def exibir_pedido_detalhado_orm(order_id):
    session = SessionLocal()

    pedido_resultado = session.query(Pedido).filter(Pedido.orderid == order_id).first()

    if not pedido_resultado:
        print("Pedido não encontrado.")
        return

    print("\n=== Detalhes do Pedido (ORM) ===")
    print(f"Pedido ID: {pedido_resultado.orderid}")
    print(f"Data do Pedido: {pedido_resultado.orderdate}")
    print(f"Cliente ID: {pedido_resultado.customerid}")
    print(f"Funcionário ID: {pedido_resultado.employeeid}")
    print(f"Nome de Entrega: {pedido_resultado.shipname}")

    print("\nItens:")
    for item in pedido_resultado.itens:
        print(f"- Produto ID: {item.productid}, Quantidade: {item.quantity}, Preço: {item.unitprice}, Desconto: {item.discount}")

    session.close()
