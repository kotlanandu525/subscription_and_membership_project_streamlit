from member.member import add_member, view_members
from plan.plan import add_plan, view_plans
from subscription.subscription import create_subscription
from payment.payment import process_payment
from reports.reports import members_report, plans_report, subscriptions_report, payments_report

def main():
    while True:
        print("\n--- Subscriptify CLI ---")
        print("1. Add Member")
        print("2. View Members")
        print("3. Add Plan")
        print("4. View Plans")
        print("5. Create Subscription")
        print("6. Process Payment")
        print("7. Reports")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_member(input("Name: "), input("Email: "))
        elif choice == "2":
            view_members()
        elif choice == "3":
            add_plan(input("Plan Name: "), float(input("Price: ")), int(input("Duration(Days): ")))
        elif choice == "4":
            view_plans()
        elif choice == "5":
            create_subscription(int(input("Member ID: ")), int(input("Plan ID: ")))
        elif choice == "6":
            process_payment(int(input("Subscription ID: ")), float(input("Amount: ")), input("Method: "))
        elif choice == "7":
            print("\n--- Reports ---")
            print("1. Members Report")
            print("2. Plans Report")
            print("3. Subscriptions Report")
            print("4. Payments Report")
            rep_choice = input("Enter choice: ")
            if rep_choice == "1": members_report()
            elif rep_choice == "2": plans_report()
            elif rep_choice == "3": subscriptions_report()
            elif rep_choice == "4": payments_report()
        elif choice == "8":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
