# pythonBigQueryReport
This python code extracts data from BigQuery and creates a CSV file in a Cloud Storage container


# Requeriments

1. Create a service account in your GCP Project with permissions on BigQuery and CloudStorage services
2. Create a new cloud function in GCP 
    2.1 Trigger type HTTP
    2.2 In runtime service account assign the service account created in step 1
    2.3 In runtime environment select Python > 3.7
    2.4 Create the requeriments and copy the content of the file located in this repository
    2.5 Create the main.py file and copy the content of the file located in this repository
    2.6 Deploy function and test
    
