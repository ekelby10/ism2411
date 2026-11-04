print("---Exercise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("---Exercise 2: Index Practice---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2 # calculate middle index
print(inventory[middle]) # middle

print("---Exercise 3: Slicing Practice---")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every second item

print("---Exercise 4: Modify the list---")
inventory.append("envelope") # add an item to the end
print(inventory) #output: "['pen', 'notebook', 'stapler', 'tape', 'marker', 'envelope']"
inventory.remove("tape") # remove an item
print(inventory) #output: "['pen', 'notebook', 'stapler', 'marker', 'envelope']"

print("---Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("---Exercise 6: Average List of Sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")
print(f"Best: ${max(sales)}")
print(f"Worst: ${min(sales)}")

# Exam question explanation
#best = sales[0]
#worst = sales[0]
# [100, 250, 75, 480, 200]
#for amount in sales:
 #   if amount > best:
 #       best = amount
  #  if amount < worst:
   #     worst = amount

#print(f"Best (manual): ${best}")
#print(f"Worst (manual): ${worst}")

print("---Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2)) # apply 10% discount and round to 2 decimal places

print("Original prices:", prices)
print("Discounts:", discount)

print("---Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", f"${(sum(high_sales) / len(high_sales)):.2f}")

#What is the most surprising thing about how lists work in Python compared to what you expected coming in?
#Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel. 
# The most surprising thing about lists in python is the hierarchy of indexing and how flexible it truly is. I find this extremely useful when working with different forms of data such as words and numbers.
# One business situation where a list wouldve benefitted me is when I was looking over sales for my hometown golf course. I had to go throuvh everything manually which took a bit of time.