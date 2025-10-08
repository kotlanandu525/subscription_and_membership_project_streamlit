from config import get_supabase
from datetime import date

supabase = get_supabase()

def process_payment(subscription_id, amount, method):
    # Fetch subscription details
    sub_resp = supabase.table("subscriptions").select("member_name, plan_name").eq("subscription_id", subscription_id).execute()
    if not sub_resp.data:
        print("Subscription not found!")
        return

    member_name = sub_resp.data[0]["member_name"]
    plan_name = sub_resp.data[0]["plan_name"]

    # Insert payment with member_name and plan_name
    response = supabase.table("payments").insert({
        "subscription_id": subscription_id,
        "member_name": member_name,
        "plan_name": plan_name,
        "amount": amount,
        "payment_date": date.today().isoformat(),
        "method": method,
        "status": "Completed"
    }).execute()

    if response.data:
        print(f"Payment successful: {response.data[0]}")
    else:
        print("Error:", response.error)
