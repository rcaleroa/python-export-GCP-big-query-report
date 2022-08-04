from google.cloud import bigquery
from google.cloud import storage
import logging
import pandas

def generar_reporte(self):
   # Query para sacar reporte de negocio, usa sintaxis propia SQL de Big Query
   self.QUERY = """SELECT visitID as SbjNum, concat(initDate,' ', initHour) as Date,concat(CAST(CAST((CAST((timestamp_diff(timestamp(concat(endDate,' ', endHour), "America/Bogota"), timestamp(concat(initDate ,' ', initHour), "America/Bogota"), MINUTE))AS INT64) /60) AS INT64)AS STRING),':',CAST(MOD(CAST((timestamp_diff(timestamp(concat(endDate,' ', endHour), "America/Bogota"), timestamp(concat(initDate ,' ', initHour), "America/Bogota"), MINUTE))AS INT64),60)AS STRING),':','00') as Duration_Min,concat(endDate,' ', endHour) as Upload, status as Complete,null as ID_Matrix,if(p135_8a89ce0adf8e498fbbd945577a5f8d10 <> 'n/a',split(p135_8a89ce0adf8e498fbbd945577a5f8d10,' Y:')[ORDINAL(2)], 'n/a') as GPS_LA,if(p135_8a89ce0adf8e498fbbd945577a5f8d10 <> 'n/a',split(split(p135_8a89ce0adf8e498fbbd945577a5f8d10,' Y')[ORDINAL(1)],'X:')[ORDINAL(2)],'n/a') as GPS_LO,userName as Encuestador FROM `tableexample` f left join `tableexample2` a on if(f.p5_8a89ce0adf8e498fbbd945577a5f8d10 <> 'n/a',CAST((REGEXP_REPLACE(f.p5_8a89ce0adf8e498fbbd945577a5f8d10, r'[^\d]+', '')) AS INT64),0)= a.codigo_ciiu left join `tableexample3` aa on if(f.p185_8a89ce0adf8e498fbbd945577a5f8d10 <> 'n/a',CAST((REGEXP_REPLACE(f.p185_8a89ce0adf8e498fbbd945577a5f8d10, r'[^\d]+', '')) AS INT64),0)= aa.codigo_ciiu left join `tableexample` ca on if(f.p5_8a89ce0adf8e498fbbd945577a5f8d10 <> 'n/a',CAST((REGEXP_REPLACE(f.p5_8a89ce0adf8e498fbbd945577a5f8d10, r'[^\d]+', '')) AS INT64),0)= ca.CIIU where split(initDate,'-')[ORDINAL(1)] ='2022'"""
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