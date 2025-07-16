def start_cli():
    print("1. Check weather")
    print("2. View routes")
    print("3. Monitor comms (disabled)")
    choice = input("Choose: ")
    if choice == "1":
        print("Fetching METAR... (mock)")
