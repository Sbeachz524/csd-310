# lbs_to_oz_converter.py

def lbs_to_oz(pounds: float) -> float:
    """
    Convert weight from pounds to ounces.
    1 pound = 16 ounces.
    """
    return pounds * 16

def main():
    print("=== Pounds to Ounces Converter ===")
    try:
        pounds = float(input("Enter weight in pounds: "))
        ounces = lbs_to_oz(pounds)
        print(f"{pounds} lbs is equal to {ounces} oz.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    