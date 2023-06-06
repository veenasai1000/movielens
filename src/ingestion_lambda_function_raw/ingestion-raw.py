import json
import boto3
import datetime
import os

def lambda_handler(event, context):
    key_path=event.get("key1")
    # TODO: Implement the logic
    Code_Bucket = os.environ['CodeBucket']
    

    current_date = datetime.datetime.now().date()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    
    def read_json_file(Code_Bucket, file_key, s3_client):
        response = s3_client.get_object(Bucket=Code_Bucket, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        data = json.loads(content)
        return data

    Code_Bucket = 'indl-data-ingestion-code'
    file_key = f"{key_path}/config_file.json"
    json_data = read_json_file(Code_Bucket, file_key, s3_client)
    
    ind_edl_source_bucket1 = json_data['ind-edl-source-bucket1']
    ind_edl_raw_bucket1 = json_data['ind-edl-raw-bucket1']
    
    source_bucket = s3.Bucket(ind_edl_source_bucket1)
    target_bucket = s3.Bucket(ind_edl_raw_bucket1)
    print(source_bucket)
    print(target_bucket)
   

        # TODO: Implement the logic to copy the object to the target bucket
        # target_bucket.copy(copy_source, folder_name)
    source_file_list = []
    target_file_list = []
    
    response = s3_client.list_objects_v2(Bucket=ind_edl_source_bucket1)
    for obj in response['Contents']:
         source_file_list.append(obj['Key'])
    
    #response = s3_client.list_objects_v2(Bucket=ind_edl_raw_bucket1)
    #for obj in response['Contents']:
     #    target_file_list.append(obj['Key'])
    
    for file in source_file_list:
         print(f"Source Bucket File: {file}")
    
   # for file in target_file_list:
    #     print(f"Target Bucket File: {file}")
    
    for file in source_file_list:
        folder_name = file.split(".")[0]
        #file_extension=file.split('.')[1]
        #print(file_extension)
        print(f"Copying file {file} to {folder_name} in the target bucket.")
        #bucket.copy(copy_source,f"movie_lens/file_name/year={}/month={}/day={}/file_name.csv")
    
        copy_source = {
            'Bucket': ind_edl_source_bucket1,
           'Key': file
         }
        target_key = f"{folder_name}/{file.split('/')[-1]}/year={year}/month={month}/day={day}/{file.split('/')[-1]}"
        #target_key=f"{folder_name}/{file}/year={year}/month={month}/day={day}/{file}_{current_date}.{file_extension}"
        target_bucket.copy(copy_source, target_key)
        print(f"Copying file {file} to {target_key} in the target bucket.")
        
        return{
            'statusCode':200,
            'body':json.dumps('Hello from Lambda!')
        }