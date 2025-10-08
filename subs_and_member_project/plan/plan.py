from config import get_supabase
from prettytable import PrettyTable # type: ignore

supabase = get_supabase()

def add_plan(name, price, duration):
    response = supabase.table("plans").insert({
        "name": name,
        "price": price,
        "duration_days": duration
    }).execute()
    if response.data:
        print(f"Plan added: {response.data}")
    else:
        print("Error adding plan:", response.error)

def view_plans():
    response = supabase.table("plans").select("*").execute()
    rows = response.data
    table = PrettyTable(["ID", "Name", "Price", "Duration(Days)"])
    for row in rows:
        table.add_row([row["plan_id"], row["name"], row["price"], row["duration_days"]])
    print(table)
