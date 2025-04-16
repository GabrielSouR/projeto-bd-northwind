from config.conexao import conectar

def exibir_pedido_detalhado_inseguro(order_id_raw):
    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SET search_path TO northwind;")

        query = f"""
            SELECT o.orderid, o.orderdate, c.companyname AS cliente, 
                   e.firstname || ' ' || e.lastname AS vendedor
            FROM orders o
            JOIN customers c ON o.customerid = c.customerid
            JOIN employees e ON o.employeeid = e.employeeid
            WHERE o.orderid = {order_id_raw}
        """
        cursor.execute(query)
        pedido = cursor.fetchall()

        if not pedido:
            print("Pedido não encontrado.")
            return

        print("\n=== RESULTADO DO RELATÓRIO (INSEGURO) ===")
        for pedido in pedido:
            print(f"\nPedido ID: {pedido[0]}")
            print(f"Data do Pedido: {pedido[1]}")
            print(f"Cliente: {pedido[2]}")
            print(f"Vendedor: {pedido[3]}")


    except Exception as e:
        print("Erro no relatório inseguro:", repr(e))
    finally:
        conn.close()
