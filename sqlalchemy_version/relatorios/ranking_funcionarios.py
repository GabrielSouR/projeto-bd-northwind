from sqlalchemy_version.config.conexao import SessionLocal
from sqlalchemy_version.model.employee import Employee
from sqlalchemy_version.model.pedido import Pedido
from sqlalchemy_version.model.item_pedido import ItemPedido
from sqlalchemy import func
from datetime import date

def exibir_ranking_funcionarios_orm(data_inicio: date, data_fim: date):
    session = SessionLocal()

    resultados = (
        session.query(
            Employee.firstname,
            Employee.lastname,
            func.count(Pedido.orderid).label("total_pedidos"),
            func.sum(ItemPedido.unitprice * ItemPedido.quantity * (1 - ItemPedido.discount)).label("total_vendido")
        )
        .join(Pedido, Pedido.employeeid == Employee.employeeid)
        .join(ItemPedido, ItemPedido.orderid == Pedido.orderid)
        .filter(Pedido.orderdate.between(data_inicio, data_fim))
        .group_by(Employee.employeeid)
        .order_by(func.sum(ItemPedido.unitprice * ItemPedido.quantity * (1 - ItemPedido.discount)).desc())
        .all()
    )

    print("\n=== Ranking de Funcionários (SQLAlchemy ORM) ===")
    for i, (first, last, pedidos, total) in enumerate(resultados, start=1):
        print(f"{i}. {first} {last} | Pedidos: {pedidos} | Total Vendido: R${float(total):.2f}")

    session.close()
