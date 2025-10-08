import os
from dotenv import load_dotenv # type: ignore
from supabase import create_client # type: ignore

load_dotenv()  # Load .env variables

def get_supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY in .env file")

    return create_client(url, key)

supabase = get_supabase()
