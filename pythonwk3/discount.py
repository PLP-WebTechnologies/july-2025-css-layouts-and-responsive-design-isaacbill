def calculate_discount(price, discount_percent):
    """
    Calculate final price after discount if discount >= 20%.
    :param price: Original price of the item (positive number)
    :param discount_percent: Discount percentage (0–100)
    :return: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for inputs with validation
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Validation checks
    if original_price <= 0:
        print("Price must be greater than zero.")
    elif discount_percentage < 0 or discount_percentage > 100:
        print("Discount percentage must be between 0 and 100.")
    else:
        final_price = calculate_discount(original_price, discount_percentage)

        if discount_percentage >= 20:
            print(f" Final price after {discount_percentage}% discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. Price remains: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numerical values for price and discount.")
