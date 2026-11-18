# Currency Converter
# PS No. 40
# Supported currencies: INR, USD, EUR, GBP

EXCHANGE_RATES = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}


def convert_to_inr(amount, currency):
    """Convert an amount from the given currency to INR."""
    return amount * EXCHANGE_RATES[currency]


def convert_currency(amount, from_currency, to_currency):
    """Convert between any two supported currencies via INR."""
    amount_in_inr = convert_to_inr(amount, from_currency)
    converted_amount = amount_in_inr / EXCHANGE_RATES[to_currency]
    return round(converted_amount, 2)


def main():
    print("===== CURRENCY CONVERTER =====")
    print("Supported currencies:", ", ".join(EXCHANGE_RATES.keys()))

    try:
        amount = float(input("Enter amount: ").strip())

        if amount < 0:
            print("Amount cannot be negative.")
            return

        from_currency = input("From currency: ").strip().upper()
        to_currency = input("To currency: ").strip().upper()

        if from_currency not in EXCHANGE_RATES:
            print(
                f"Unsupported currency '{from_currency}'. "
                f"Available: {', '.join(EXCHANGE_RATES.keys())}"
            )
            return

        if to_currency not in EXCHANGE_RATES:
            print(
                f"Unsupported currency '{to_currency}'. "
                f"Available: {', '.join(EXCHANGE_RATES.keys())}"
            )
            return

        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount:g} {from_currency} = {result:.2f} {to_currency}")

    except ValueError: 
        print("Invalid amount. Enter a number.")


if __name__ == "__main__":
    main()
