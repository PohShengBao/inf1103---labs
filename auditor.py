inventory = 0
failed_entries = 0

while True:
    entry = input("Enter stock quantity (or type quit): ").strip()

    if entry.lower() == "quit":
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Failed/Rejected Entries: {failed_entries}")
        break

    if not entry.isdigit():
        print("Error: Please enter a non-negative integer.")
        failed_entries += 1
        continue
		
    quantity = int(entry)	
    if quantity < 0:
        print("Error: Negative stock quantities are not allowed.")
        failed_entries += 1
        continue
	
    inventory += quantity
    if inventory > 500:
        print("Alert: Overstock threshold exceeded.")
        break