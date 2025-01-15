# Short program to calculate the sum of numbers
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]  # Convert input strings to floats
total = sum(numbers)
print(f"The sum of the numbers is: {total}")
