from config import get_supabase
from datetime import date, timedelta

supabase = get_supabase()

def create_subscription(member_id, plan_id):
    # Get member name
    member_resp = supabase.table("members").select("name").eq("member_id", member_id).execute()
    if not member_resp.data:
        print("Member not found!")
        return
    member_name = member_resp.data[0]["name"]

    # Get plan details
    plan_resp = supabase.table("plans").select("*").eq("plan_id", plan_id).execute()
    if not plan_resp.data:
        print("Plan not found!")
        return
    plan_name = plan_resp.data[0]["name"]
    duration = plan_resp.data[0]["duration_days"]

    # Calculate dates
    start = date.today().isoformat()
    end = (date.today() + timedelta(days=duration)).isoformat()

    # Insert subscription
    response = supabase.table("subscriptions").insert({
        "member_id": member_id,
        "member_name": member_name,
        "plan_id": plan_id,
        "plan_name": plan_name,
        "start_date": start,
        "end_date": end,
        "status": "Active"
    }).execute()

    if response.data:
        print(f"Subscription created: {response.data[0]}")
    else:
        print("Error:", response.error)
