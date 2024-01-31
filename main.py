currencies = ["GBP", "USD", "EUR", "INR", "EGP"]
available_currencies = ", ".join(currencies)

while True:
    try:
        currency = input(f"What would you like to convert from? Pick one: {available_currencies}: ").upper()
        if currency not in currencies:
            raise ValueError("Invalid currency. Please choose from the available currencies.")

        converted_currency = input(f"What would you like to convert to? Pick one: {available_currencies}: ").upper()
        if converted_currency not in currencies:
            raise ValueError("Invalid currency. Please choose from the available currencies.")

        amount = int(input("How much do you want to convert? Enter a number: "))

        if currency == "GBP":
            if converted_currency == "EUR":
                converted = amount * 1.17
            elif converted_currency == "USD":
                converted = amount * 1.28
            elif converted_currency == "INR":
                converted = amount * 106.12
            elif converted_currency == "EGP":
                converted = amount * 39.47
        elif currency == "EUR":
            if converted_currency == "GBP":
                converted = amount / 1.17
            elif converted_currency == "USD":
                converted = amount * 0.92
            elif converted_currency == "INR":
                converted = amount * 90.79
        elif currency == "USD":
            if converted_currency == "GBP":
                converted = amount / 1.28
            elif converted_currency == "EUR":
                converted = amount / 0.92
            elif converted_currency == "INR":
                converted = amount * 83.09
            elif converted_currency == "EGP":
                converted = amount * 30.90
        elif currency == "INR":
            if converted_currency == "GBP":
                converted = amount / 106.12
            elif converted_currency == "EUR":
                converted = amount / 90.79
            elif converted_currency == "USD":
                converted = amount / 83.09
            elif converted_currency == "EGP":
                converted = amount * 0.37
        elif currency == "EGP":
            if converted_currency == "GBP":
                converted = amount / 39.47
        else:
            print("Invalid currency combination. Please choose from the available currencies.")

        print("This will be " + str(converted) + " " + converted_currency)

    except ValueError as e:
        print(f"Error: {e}")
