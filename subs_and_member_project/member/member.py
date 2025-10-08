from config import get_supabase
from prettytable import PrettyTable # type: ignore

supabase = get_supabase()

def add_member(name, email):
    # Check if a member with the same email already exists
    existing = supabase.table("members").select("*").eq("email", email).execute()
    if existing.data:
        print(f"Member with email '{email}' already exists! Cannot add duplicate.")
        return

    # Insert new member
    response = supabase.table("members").insert({"name": name, "email": email}).execute()
    if response.data:
        print(f"Member added successfully: {response.data[0]}")
    else:
        print("Error:", response.error)

def view_members():
    response = supabase.table("members").select("*").execute()
    rows = response.data
    table = PrettyTable(["ID", "Name", "Email", "Join Date"])
    for row in rows:
        table.add_row([row["member_id"], row["name"], row["email"], row["join_date"]])
    print(table)
