print('Welcome to the tip calculator!')
total_bill = input('What was the total bill? $')
tip_percentage = input('What percentage tip would you like to give? 10, 12 or 15? ')
num_people = input('How many people to split the bill?')
each_person = (float(total_bill)/int(num_people)) * (100 + int(tip_percentage)) / 100
print(f"Each person should pay {each_person:.2f}")