import os
import dropbox
from dotenv import load_dotenv

load_dotenv()  # Carrega o .env automaticamente

ACCESS_TOKEN = os.getenv("DROPBOX_TOKEN")
print("Token carregado:", ACCESS_TOKEN)

def upload_to_dropbox(file_path, dropbox_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    with open(file_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

    link = dbx.sharing_create_shared_link_with_settings(dropbox_path)
    return link.url.replace('?dl=0', '?raw=1')  # Link direto para visualização/download
