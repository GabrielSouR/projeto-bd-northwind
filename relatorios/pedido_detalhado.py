from config.conexao import conectar

def exibir_pedido_detalhado(order_id):
    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SET search_path TO northwind;")

        cursor.execute("""
            SELECT o.orderid, o.orderdate, c.companyname AS cliente, 
                   e.firstname || ' ' || e.lastname AS vendedor
            FROM orders o
            JOIN customers c ON o.customerid = c.customerid
            JOIN employees e ON o.employeeid = e.employeeid
            WHERE o.orderid = %s
        """, (order_id,))
        
        pedido = cursor.fetchone()
        if not pedido:
            print("Pedido não encontrado.")
            return

        print("\n=== Detalhes do Pedido ===")
        print(f"Pedido ID: {pedido[0]}")
        print(f"Data do Pedido: {pedido[1]}")
        print(f"Cliente: {pedido[2]}")
        print(f"Vendedor: {pedido[3]}")

        cursor.execute("""
            SELECT p.productname, od.quantity, od.unitprice
            FROM order_details od
            JOIN products p ON od.productid = p.productid
            WHERE od.orderid = %s
        """, (order_id,))
        
        itens = cursor.fetchall()
        print("\nItens do Pedido:")
        for item in itens:
            print(f"Produto: {item[0]} | Quantidade: {item[1]} | Preço: {item[2]}")

    except Exception as e:
        print("Erro ao buscar detalhes do pedido:", repr(e))
    finally:
        conn.close()
