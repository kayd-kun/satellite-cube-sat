from supabase import create_client
import os
from dotenv import load_dotenv
import json

load_dotenv()

supabase_url = os.getenv('supabase_url')
supabase_key = os.getenv('supabase_key')

bucket_name = 'images'
supabase = create_client(supabase_url, supabase_key)
download_destination = './downloaded_images/'
downloaded_images =  []

# retrive_a_bucket = supabase.storage.get_bucket(bucket_name)
files_in_a_bucket = supabase.storage.get_bucket(bucket_name).list()

downloaded_images_local = os.listdir(download_destination)
for image in downloaded_images_local:
    downloaded_images.append(image)

for file in files_in_a_bucket:
    file_name = file['name']
    print(file_name)
  
    if file_name not in downloaded_images:
        # if file_name == '.emptyFolderPlaceholder':
        #     continue
        download_destination += file_name
        with open(download_destination, 'wb+') as f:
            res = supabase.storage.from_(bucket_name).download(file_name)
            print('Downloaded successfully')
            f.write(res)
        downloaded_images.append(file_name)
    else:
        print(f'File {file_name} already exists, not downloading again.')