from config.conexao import conectar

def exibir_ranking_funcionarios(data_inicio, data_fim):
    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SET search_path TO northwind;")

        cursor.execute("""
            SELECT 
                e.firstname || ' ' || e.lastname AS funcionario,
                COUNT(o.orderid) AS total_pedidos,
                SUM(od.unitprice * od.quantity * (1 - od.discount)) AS total_vendido
            FROM orders o
            JOIN employees e ON o.employeeid = e.employeeid
            JOIN order_details od ON o.orderid = od.orderid
            WHERE o.orderdate BETWEEN %s AND %s
            GROUP BY e.employeeid
            ORDER BY total_vendido DESC
        """, (data_inicio, data_fim))

        ranking = cursor.fetchall()

        print("\n=== Ranking de Funcionários ===")
        for pos, linha in enumerate(ranking, start=1):
            nome, total, vendido = linha
            print(f"{pos}. {nome} | Pedidos: {total} | Total Vendido: R${vendido:.2f}")

    except Exception as e:
        print("Erro ao gerar ranking:", repr(e))
    finally:
        conn.close()
