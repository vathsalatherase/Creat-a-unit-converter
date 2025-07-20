# Conversion functions
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

# Dictionary of conversion mappings
conversion_options = {
    "1": ("Celsius to Fahrenheit", c_to_f, "°F"),
    "2": ("Fahrenheit to Celsius", f_to_c, "°C"),
    "3": ("Celsius to Kelvin", c_to_k, "K"),
    "4": ("Kelvin to Celsius", k_to_c, "°C")
}

# Menu-driven program
def main():
    while True:
        print("\n🌡️ Temperature Conversion Menu")
        for key, (desc, _, _) in conversion_options.items():
            print(f"{key}. {desc}")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting... Thank you!")
            break

        if choice not in conversion_options:
            print("❌ Invalid choice. Try again.")
            continue

        try:
            value = float(input("Enter the temperature to convert: "))
            desc, func, unit = conversion_options[choice]
            result = func(value)
            print(f"✅ {desc}: {value} converted is {result:.2f} {unit}")
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
