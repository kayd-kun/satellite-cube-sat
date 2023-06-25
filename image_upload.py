from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv('supabase_url')
supabase_key = os.getenv('supabase_key')

supabase = create_client(supabase_url, supabase_key)

bucket_name = 'images' # Name of the bucket to upload to
upload_path_local = './to_upload_images/' # Path to local directory containing images to upload
# upload_paths_local = [] # List of paths to images to upload
image_names_to_upload = [] # List of image names to upload

# Get images in local directory
# Collect image names and paths
for image in os.listdir(upload_path_local):
   image_names_to_upload.append(image)
   # upload_paths_local.append(upload_path_local + image)   

# Retrieve images in bucket 
images_in_bucket_list = supabase.storage.get_bucket(bucket_name).list()
images_in_bucket = []

for image in images_in_bucket_list:
   images_in_bucket.append(image['name'])

# Compare images in local directory to images in bucket
# Upload to bucket if not already in bucket
for image in image_names_to_upload:
   if image in images_in_bucket:
      print(f'Image {image} already exists, not uploading again.')
      continue

   image_path = upload_path_local + image
   with open(image_path, "rb") as file:
      file_data = file.read()

   response = supabase.storage.get_bucket(bucket_name).upload(image, file_data)

   if response.status_code == 200:
      image_url = response.content.decode("utf-8")
      print("Image uploaded successfully:", image)
   else:
      print("Image upload failed:", response.status_code)