from config import get_supabase
from prettytable import PrettyTable # type: ignore

supabase = get_supabase()


def members_report():
    members = supabase.table("members").select("*").execute().data
    table = PrettyTable(["ID", "Name", "Email", "Join Date"])
    for m in members:
        table.add_row([m["member_id"], m["name"], m["email"], m["join_date"]])
    print(table)


def plans_report():
    plans = supabase.table("plans").select("*").execute().data
    table = PrettyTable(["ID", "Name", "Price", "Duration(Days)"])
    for p in plans:
        table.add_row([p["plan_id"], p["name"], p["price"], p["duration_days"]])
    print(table)


def subscriptions_report():
    subs = supabase.table("subscriptions").select("*").execute().data
    table = PrettyTable(["Sub ID", "Member Name", "Plan Name", "Start Date", "End Date", "Status"])
    for s in subs:
        table.add_row([
            s["subscription_id"],
            s.get("member_name", "N/A"),   
            s.get("plan_name", "N/A"),     
            s["start_date"],
            s["end_date"],
            s["status"]
        ])
    print(table)


def payments_report():
    payments = supabase.table("payments").select("*").execute().data
    table = PrettyTable(["Payment ID", "Subscription ID", "Member Name", "Plan Name", "Amount", "Date", "Method", "Status"])
    
    for p in payments:
        table.add_row([
            p["payment_id"],
            p["subscription_id"],
            p.get("member_name", "N/A"),
            p.get("plan_name", "N/A"),
            p["amount"],
            p["payment_date"],
            p["method"],
            p["status"]
        ])
    print(table)

    
