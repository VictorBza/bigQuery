from google.cloud import bigquery

# Crea un cliente de BigQuery
client = bigquery.Client()
query = """
SELECT TIMESTAMP_SECONDS(CAST(timestamp / 1000 AS INT64)) AS transaction_timestamp,
       COUNT(*) AS num_transactions
FROM `bigquery-public-data.bitcoin_blockchain.transactions`
GROUP BY transaction_timestamp
ORDER BY transaction_timestamp;
"""

# Ejecuta la consulta
query_job = client.query(query)

# Recorre los resultados
for row in query_job:
    print(row)




    