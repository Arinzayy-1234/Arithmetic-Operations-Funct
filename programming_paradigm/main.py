
import sys
import os # Add this line
print("--- sys.path ---")
for p in sys.path:
    print(p)
print("----------------")
print(f"Current working directory: {os.getcwd()}") # Add this line
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()