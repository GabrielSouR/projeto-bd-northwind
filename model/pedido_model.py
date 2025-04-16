class Pedido:
    def __init__(self, customer_id, employee_id, order_date, required_date, ship_name, items):
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_date = order_date
        self.required_date = required_date
        self.ship_name = ship_name
        self.items = items
