from config.conexao import conectar

def inserir_pedido_inseguro(pedido):
    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SET search_path TO northwind;")

        sql = f"""
            INSERT INTO orders (customerid, employeeid, orderdate, requireddate, shipname)
            VALUES ('{pedido.customer_id}', {pedido.employee_id}, '{pedido.order_date}', '{pedido.required_date}', '{pedido.ship_name}')
            RETURNING orderid
        """
        cursor.execute(sql)
        order_id = cursor.fetchone()[0]

        for item in pedido.items:
            product_id, unit_price, quantity, discount = item
            cursor.execute(f"""
                INSERT INTO order_details (orderid, productid, unitprice, quantity, discount)
                VALUES ({order_id}, {product_id}, {unit_price}, {quantity}, {discount})
            """)

        conn.commit()
        print(f"Pedido {order_id} inserido com sucesso (inseguro).")

    except Exception as e:
        print("Erro ao inserir pedido (inseguro):", repr(e))
        conn.rollback()
    finally:
        conn.close()
