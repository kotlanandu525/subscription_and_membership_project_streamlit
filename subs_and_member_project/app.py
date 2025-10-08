import streamlit as st
import pandas as pd
from config import get_supabase
from member.member import add_member
from plan.plan import add_plan
from subscription.subscription import create_subscription
from payment.payment import process_payment

supabase = get_supabase()

st.set_page_config(page_title="Subscriptify - Member Reports", layout="wide")
st.title("💳 Subscriptify - Subscription Management System")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Member",
        "Add Plan",
        "Create Subscription",
        "Process Payment",
        "Member Reports"
    ]
)

# ---------- ADD MEMBER ----------
if menu == "Add Member":
    st.header("Add Member")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Add Member"):
        if name and email:
            add_member(name, email)
            st.success(f"Member '{name}' added successfully!")
        else:
            st.warning("Please fill all fields")

# ---------- ADD PLAN ----------
elif menu == "Add Plan":
    st.header("Add Subscription Plan")
    plan_name = st.text_input("Plan Name")
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    duration = st.number_input("Duration (Days)", min_value=1, step=1)
    if st.button("Add Plan"):
        if plan_name:
            add_plan(plan_name, price, duration)
            st.success(f"Plan '{plan_name}' added successfully!")
        else:
            st.warning("Please enter a plan name")

# ---------- CREATE SUBSCRIPTION ----------
elif menu == "Create Subscription":
    st.header("Create Subscription")
    # Fetch members and plans for selection
    members = supabase.table("members").select("member_id, name").execute().data
    plans = supabase.table("plans").select("plan_id, name").execute().data

    member_options = {m["name"]: m["member_id"] for m in members} if members else {}
    plan_options = {p["name"]: p["plan_id"] for p in plans} if plans else {}

    selected_member = st.selectbox("Select Member", options=list(member_options.keys()))
    selected_plan = st.selectbox("Select Plan", options=list(plan_options.keys()))

    if st.button("Create Subscription"):
        member_id = member_options.get(selected_member)
        plan_id = plan_options.get(selected_plan)
        if member_id and plan_id:
            create_subscription(member_id, plan_id)
            st.success(f"Subscription created for {selected_member} with plan {selected_plan}")
        else:
            st.error("Invalid member or plan selected")

# ---------- PROCESS PAYMENT ----------
elif menu == "Process Payment":
    st.header("Process Payment")
    subscription_id = st.text_input("Subscription ID")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    method = st.selectbox("Payment Method", ["Credit Card", "Debit Card", "Paypal", "Bank Transfer"])
    if st.button("Process Payment"):
        if subscription_id and amount > 0 and method:
            process_payment(subscription_id, amount, method)
            st.success(f"Payment of ${amount:.2f} processed for subscription {subscription_id}")
        else:
            st.warning("Please enter all payment details")

# ---------- MEMBER REPORTS ----------
elif menu == "Member Reports":
    st.header("Member Reports")

    # Fetch members for selection
    members = supabase.table("members").select("member_id, name").execute().data
    if not members:
        st.info("No members found.")
    else:
        member_options = {m["name"]: m["member_id"] for m in members}
        selected_member = st.selectbox("Select Member", options=list(member_options.keys()))
        member_id = member_options[selected_member]

        # Subscriptions of selected member
        subs = supabase.table("subscriptions").select("*").eq("member_id", member_id).execute().data
        if subs:
            st.subheader(f"Subscriptions for {selected_member}")
            subs_df = pd.DataFrame(subs)
            subs_df = subs_df[["subscription_id", "plan_name", "start_date", "end_date", "status"]]
            subs_df.columns = ["Subscription ID", "Plan Name", "Start Date", "End Date", "Status"]
            st.dataframe(subs_df)
        else:
            st.info(f"No subscriptions found for {selected_member}")

        # Payments of selected member (join payments with subscriptions)
        # First get all subscription IDs for the member
        sub_ids = [s["subscription_id"] for s in subs] if subs else []

        if sub_ids:
            payments = supabase.table("payments").select("*").in_("subscription_id", sub_ids).execute().data
            if payments:
                st.subheader(f"Payments for {selected_member}")
                payments_df = pd.DataFrame(payments)
                payments_df = payments_df[["payment_id", "subscription_id", "plan_name", "amount", "payment_date", "method", "status"]]
                payments_df.columns = ["Payment ID", "Subscription ID", "Plan Name", "Amount", "Date", "Method", "Status"]
                st.dataframe(payments_df)
            else:
                st.info(f"No payments found for {selected_member}")
        else:
            st.info(f"No subscriptions/payments found for {selected_member}")
