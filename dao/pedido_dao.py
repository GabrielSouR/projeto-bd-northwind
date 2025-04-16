from config.conexao import conectar

def inserir_pedido(pedido):
    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SET search_path TO northwind;")

        cursor.execute("""
            INSERT INTO orders (customerid, employeeid, orderdate, requireddate, shipname)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING orderid
        """, (pedido.customer_id, pedido.employee_id, pedido.order_date, pedido.required_date, pedido.ship_name))
        
        order_id = cursor.fetchone()[0]

        for item in pedido.items:
            product_id, unit_price, quantity, discount = item
            cursor.execute("""
                INSERT INTO order_details (orderid, productid, unitprice, quantity, discount)
                VALUES (%s, %s, %s, %s, %s)
            """, (order_id, product_id, unit_price, quantity, discount))

        conn.commit()
        print(f"Pedido {order_id} inserido com sucesso!")

    except Exception as e:
        print("Erro ao inserir pedido:", repr(e))
        conn.rollback()
    finally:
        conn.close()
