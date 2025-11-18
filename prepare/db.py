import os
import gdown

DB_PATH = "olist.db"

def download_database():
    if not os.path.exists(DB_PATH):
        url = "https://drive.google.com/uc?id=14gUFHV5wElzgkdfbvMWOknhdtv-lOFw2dans accueil , "  
        gdown.download(url, DB_PATH, quiet=False)

if __name__ == "__main__":
    download_database()
