from src.dependency import greet, add_numbers

def main():
    # Using the greet function from dependency.py
    message = greet("World")
    print(message)
    
    # Using the add_numbers function from dependency.py
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")


    print("I made a change as part of the assessment")

if __name__ == "__main__":
    main()

