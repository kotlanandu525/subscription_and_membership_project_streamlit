# # config.py
# import os
# from dotenv import load_dotenv # type: ignore
# from supabase import create_client # type: ignore
# import streamlit as st
# def get_supabase():
#     # Load environment variables (for local dev)
#     load_dotenv()

#     url = os.getenv("SUPABASE_URL")
#     key = os.getenv("SUPABASE_KEY")

#     if not url or not key:
#         raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY")

#     return create_client(url, key)

import streamlit as st
from supabase import create_clientaimport streamlit as st
from supabase import create_client # type: ignore

def get_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    
    if not url or not key:
        raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY in Streamlit secrets")

    return create_client(url, key)


# Access Supabase credentials from Streamlit secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)


