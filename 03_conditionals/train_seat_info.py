seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper class - non ac")
    case "general":
        print("general type - not even seats available in rush hours")
    case "ac":
        print("AC type - proper ac facilities")
    case "luxury":
        print("high class facilities available")
    case _:
        print("invalid seat type")