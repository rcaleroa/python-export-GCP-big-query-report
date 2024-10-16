from google.cloud import bigquery
from google.cloud import storage
import logging
import pandas

def generar_reporte(self):
   # Query para sacar reporte de negocio, usa sintaxis propia SQL de Big Query
   self.QUERY = "SELECT visitID  FROM `tableexample`"
   # Instancia un objeto de BigQuery
   self.bq_client = bigquery.Client()
   # Se envía a ejecutar el Query al Objeto de BigQuery
   self.query_job = self.bq_client.query(self.QUERY)
   # Espera a que el query termine
   self.rows_df = self.query_job.result().to_dataframe() 
   # Instancia un objeto de cloud storage
   self.storage_client = storage.Client() 
   # Al objeto de cloud storage GCP le pedimos buscar el contenedor
   self.bucket = self.storage_client.get_bucket('respuestas_ejemplo') 
   # Dentro del contenedor se crea el objeto con este nombre en formato CSV
   self.blob = self.bucket.blob('respuestas_formulario.csv') 
   # Subir el CSV al contenedor
   self.blob.upload_from_string(self.rows_df.to_csv(sep=';',index=False,
encoding='utf-8'),content_type='application/octet-stream') 
   # Dejar el objeto público dentro del contenedor
   self.blob.make_public() 
   return ('200')
