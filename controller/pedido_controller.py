from model.pedido_model import Pedido
from dao.pedido_dao import inserir_pedido
from dao.pedido_dao_inseguro import inserir_pedido_inseguro
    
def criar_pedido_interativo(customer_id, employee_id, order_date, required_date, ship_name, items):
    pedido = Pedido(customer_id, employee_id, order_date, required_date, ship_name, items)
    inserir_pedido(pedido)
    
def criar_pedido_inseguro(customer_id, employee_id, order_date, required_date, ship_name, items):
    pedido = Pedido(customer_id, employee_id, order_date, required_date, ship_name, items)
    inserir_pedido_inseguro(pedido)
