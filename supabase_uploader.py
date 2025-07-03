import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")  # ex: https://xxxxx.supabase.co
SUPABASE_KEY = os.getenv("SUPABASE_KEY")  # sua chave anon pública
BUCKET = "primecloud"  # Nome do bucket criado no Supabase

def upload_to_supabase(file_path):
    file_name = os.path.basename(file_path)
    
    with open(file_path, "rb") as f:
        file_data = f.read()

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/pdf"
    }

    url = f"{SUPABASE_URL}/storage/v1/object/{BUCKET}/{file_name}"

    response = requests.post(url, headers=headers, data=file_data)

    if response.status_code in [200, 201]:
        print("✅ Upload no Supabase realizado com sucesso.")
        public_url = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET}/{file_name}"
        return public_url
    else:
        print("❌ Falha no upload:", response.text)
        return None
