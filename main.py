#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
  
#Write your code below this line 👇

print("Welcome to the tip calculator!\n")

total_bill = input("What was the total bill?\n$")

total = float(total_bill)

tip_percentage = input("How much tip would you like to give? 10, 12 or 15?\n")

tip = int(tip_percentage)/100+1

people_split= input("How many people to split the bill?\n")

split = int(people_split)

output = "{:.2f}".format((total/split)*tip)


message = f"Each person should pay ${output}."

print(message)
