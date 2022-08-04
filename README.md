# pythonBigQueryReport
This python code extracts data from BigQuery and creates a CSV file in a Cloud Storage container


# Requeriments

1. Create a service account in your GCP Project with permissions on BigQuery and CloudStorage services
2. Create a new cloud function in GCP
3. Select Trigger type HTTP in the Cloud Functions section
4. In runtime service account section assign the service account created in step 1
5. In runtime environment section select Python > 3.7
6. Create the requeriments and copy the content of the file located in this repository
7. Create the main.py file and copy the content of the file located in this repository
8. Deploy function and test
    
