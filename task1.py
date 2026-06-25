def convert_from_celsius(celsius):
    """Converts Celsius to Fahrenheit and Kelvin."""
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def convert_from_fahrenheit(fahrenheit):
    """Converts Fahrenheit to Celsius and Kelvin."""
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

def convert_from_kelvin(kelvin):
    """Converts Kelvin to Celsius and Fahrenheit."""
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

def main():
    print("=" * 45)
    print("     THERMAL SCALE CONVERSION TOOL v1.0     ")
    print("=" * 45)
    
    # 1. Get and validate the temperature value
    while True:
        try:
            temp_input = input("Enter the temperature value: ").strip()
            value = float(temp_input)
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number (e.g., 25, -10.5).")

    # 2. Get and validate the original unit
    print("\nSupported Units:")
    print("C - Celsius")
    print("F - Fahrenheit")
    print("K - Kelvin")
    
    while True:
        unit = input("Enter the original unit (C/F/K): ").strip().upper()
        if unit in ['C', 'F', 'K']:
            break
        print("❌ Invalid unit. Please enter 'C', 'F', or 'K'.")

    print("\n" + "-" * 45)
    print("CONVERSION RESULTS:")
    print("-" * 45)

    # 3. Perform conversions and display results
    if unit == 'C':
        f, k = convert_from_celsius(value)
        print(f"Original: {value:,.2f}°C")
        print(f"➡️ Fahrenheit: {f:,.2f}°F")
        print(f"➡️ Kelvin:     {k:,.2f} K")
        
    elif unit == 'F':
        c, k = convert_from_fahrenheit(value)
        print(f"Original: {value:,.2f}°F")
        print(f"➡️ Celsius:    {c:,.2f}°C")
        print(f"➡️ Kelvin:     {k:,.2f} K")
        
    elif unit == 'K':
        if value < 0:
            print("⚠️ Warning: Absolute zero is 0 K. Negative Kelvin values are theoretically impossible.")
        c, f = convert_from_kelvin(value)
        print(f"Original: {value:,.2f} K")
        print(f"➡️ Celsius:    {c:,.2f}°C")
        print(f"➡️ Fahrenheit: {f:,.2f}°F")
        
    print("=" * 45)

if __name__ == "__main__":
    main()