# A Python program that uses the Harris-Benedict equation to calculate the daily macronutrient intake in grams needed for weight loss.
# The equation I use to calculate BMR was revised by Mifflin and St Jeor in 1990.

while True:
    try:
        age = float(input("Enter your age: "))
        height = float(input("Enter your height: "))
        weight = float(input("Enter your weight: "))
        gender = int(input("Enter your gender (1: Woman, 2: Man): "))
        
        if weight < 0 or age < 0 or height < 0 or gender > 2 or gender < 1:
            print("Please do not enter a negative value.")
        else:
            break  
    except ValueError:
        print("Please enter a valid number.")


while True:
    try:
        activityLevel = int(input("Enter your activity level (1: Sedentary, 2: Lightly Active, 3: Moderately Active, 4: Very Active, 5: Super Active): "))

        if not activityLevel >= 1 and activityLevel <= 5:
            print("Please enter a valid number.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

activityRate = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
} # Activity factor

calorieToGram = {
    "carbonhydrate": 4,
    "protein": 4,
    "fat": 9
} # 1 kcal to gram

if gender == 1: # Basal Metabolic Rate
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161 
else:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5 

tdee = bmr * activityRate[activityLevel] # Total Daily Energy Expenditure

if weight <= 100:
    targetCalories = tdee - 500
else:
    targetCalories = tdee - 700

protein = (weight * 2) # 2 grams of protein per kilogram of body weight
carbonhydrate = (targetCalories * 0.45) / calorieToGram["carbonhydrate"]  # 45% of daily calories
fats = (targetCalories * 0.25) / calorieToGram["fat"] # 25% of daily calories

print(f"\nYou should consume {protein:.0f} grams of protein, {carbonhydrate:.0f} grams of carbohydrates, and {fats:.0f} grams of fat daily to lose weight.")

