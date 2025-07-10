# main.py
from load_data import load_data
from bmr_calculator import calculate_daily_calories
from goal_predictor import train_model, predict_goal
from food_recommender import recommend_foods, food_goal_tag
from similar_foods import get_similar_foods
from query_parser import parse_query, search_foods

def food_goal_mode(df):
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in cm): "))
    activity = input("Activity level (sedentary/light/moderate/active/very active): ")
    goal = input("Your goal (weight loss / maintenance / weight gain): ")

    daily_cal = calculate_daily_calories(age, gender, weight, height, activity, goal)
    print(f"\n🔥 Your recommended daily calorie intake: {round(daily_cal)} kcal\n")

    model, le = train_model(df)
    foods = recommend_foods(df, goal)
    for item in foods:
        predicted = predict_goal(model, le, item["Cals_per100grams"], item["KJ_per100grams"])
        print(f"- {item['FoodItem']} | {item['Cals_per100grams']} kcal | {item['FoodCategory']} | 🤖 ML Goal: {predicted}")
        print("  🔄 Healthier options:")
        similar = get_similar_foods(df, item["FoodItem"], max_cal=item["Cals_per100grams"])
        for sim in similar:
            print(f"   👉 {sim['FoodItem']} ({sim['Calories']} kcal) [{sim['Similarity']}% match]")
        print()

def nlp_query_mode(df):
    query = input("Ask your nutrition query (e.g., high protein snacks under 200 calories):\n> ")
    filters = parse_query(query)
    result = search_foods(df, filters)
    print("\n📋 Search Results:")
    for _, row in result.iterrows():
        print(f"- {row['FoodItem']} | {row['Cals_per100grams']} kcal ")

def main():
    df = load_data("Projects/New Project/FoodGoalAI/data/your_dataset.csv")
    print("📢 Welcome to FoodGoal AI")
    print("1️⃣ - Smart Recommendation by Body Info")
    print("2️⃣ - Natural Language Query Search")
    choice = input("Choose mode (1 or 2): ")

    if choice == '1':
        food_goal_mode(df)
    elif choice == '2':
        nlp_query_mode(df)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
