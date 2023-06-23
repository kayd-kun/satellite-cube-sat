from supabase import create_client

supabase_url = 'https://pduxeaspjpknwnrutgxj.supabase.co'
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBkdXhlYXNwanBrbnducnV0Z3hqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4Njk1MzUyOSwiZXhwIjoyMDAyNTI5NTI5fQ.2DNbHc-_PWF4cQ_aqiwfm4Lr2Wk0_IFIP5Fzr11wsaA"

supabase = create_client(supabase_url, supabase_key)

bucket_name = 'images'
image_path = './test_image.png'

with open(image_path, "rb") as file:
       file_data = file.read()

response = supabase.storage.get_bucket(bucket_name).upload("image.png", file_data)

if response.status_code == 200:
   image_url = response.content.decode("utf-8")
   print("Image uploaded successfully:", image_url)
else:
   print("Image upload failed:", response.status_code)

