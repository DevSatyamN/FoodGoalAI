# bmr_calculator.py
def calculate_bmr(age, gender, weight, height):
    if gender.lower() == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def get_activity_multiplier(activity_level):
    return {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }.get(activity_level.lower(), 1.2)

def calculate_daily_calories(age, gender, weight, height, activity_level, goal):
    bmr = calculate_bmr(age, gender, weight, height)
    tdee = bmr * get_activity_multiplier(activity_level)
    if goal == "weight loss":
        return tdee - 500
    elif goal == "weight gain":
        return tdee + 500
    return tdee
 