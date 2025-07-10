# food_recommender.py
def recommend_foods(df, goal, top_n=10):
    if goal == 'weight loss':
        filtered = df[df['Cals_per100grams'] <= 100]
    elif goal == 'weight gain':
        filtered = df[df['Cals_per100grams'] >= 200]
    else:
        filtered = df[(df['Cals_per100grams'] > 100) & (df['Cals_per100grams'] < 200)]
    return filtered.sort_values("Cals_per100grams").head(top_n).to_dict(orient="records")

def food_goal_tag(cal):
    if cal <= 100:
        return "🧘‍♂️ Weight Loss"
    elif cal >= 200:
        return "🏋️‍♂️ Weight Gain"
    return "⚖️ Maintenance"
