
import streamlit as st
from supabase import create_client # type: ignore
from config import supabase  # import the supabase connection from config.py
import pandas as pd

st.set_page_config(page_title="Subscriptify", layout="centered")

st.title("💳 Subscriptify - Subscription Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add Member",
        "View Members",
        "Add Plan",
        "View Plans"
    ]
)

# ---------- ADD MEMBER ----------
if menu == "Add Member":
    st.header("Add Member")
    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Add"):
        if name and email:
            data = {"name": name, "email": email}
            supabase.table("members").insert(data).execute()
            st.success(f"✅ Member '{name}' added successfully!")
        else:
            st.warning("⚠️ Please fill all fields")

# ---------- VIEW MEMBERS ----------
elif menu == "View Members":
    st.header("Members List")
    res = supabase.table("members").select("*").execute()
    members = res.data

    if members:
        df = pd.DataFrame(members)
        st.dataframe(df)
    else:
        st.info("No members found.")

# ---------- ADD PLAN ----------
elif menu == "Add Plan":
    st.header("Add Subscription Plan")
    name = st.text_input("Plan Name")
    price = st.number_input("Price", min_value=0.0, format="%.2f")

    if st.button("Save Plan"):
        if name:
            data = {"plan_name": name, "price": price}
            supabase.table("plans").insert(data).execute()
            st.success(f"✅ Plan '{name}' added successfully!")
        else:
            st.warning("⚠️ Please enter a plan name")

# ---------- VIEW PLANS ----------
elif menu == "View Plans":
    st.header("Available Plans")
    res = supabase.table("plans").select("*").execute()
    plans = res.data

    if plans:
        df = pd.DataFrame(plans)
        st.dataframe(df)
    else:
        st.info("No plans found.")
