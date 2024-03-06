from google.cloud import bigquery
from datetime import datetime

# Crea un cliente de BigQuery
client = bigquery.Client()
query = """
SELECT DATE(TIMESTAMP_SECONDS(CAST(timestamp / 1000 AS INT64))) AS transaction_date, COUNT(*) AS num_transactions
FROM `bigquery-public-data.bitcoin_blockchain.transactions`
GROUP BY transaction_date
ORDER BY transaction_date;
"""

# Ejecuta la consulta
query_job = client.query(query)

# Crea un diccionario para almacenar los resultados agrupados por día
transactions_by_date = {}

# Recorre los resultados y agrupa por día
for row in query_job:
    transaction_date = row['transaction_date']
    num_transactions = row['num_transactions']
    transactions_by_date[transaction_date] = num_transactions

# Imprime los resultados agrupados por día
for date, num_transactions in transactions_by_date.items():
    print(f"Fecha: {date}, Transacciones: {num_transactions}")
