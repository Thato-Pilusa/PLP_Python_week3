def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it's 20% or higher.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.
    
    Returns:
        float: The final price after discount if applicable, otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percentage)
    print(f"The final price after applying the discount (if applicable) is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
