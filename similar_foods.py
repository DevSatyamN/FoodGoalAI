# similar_foods.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similar_foods(df, food_name, top_n=3, max_cal=None):
    items = df['FoodItem'].str.lower().tolist()
    if food_name.lower() not in items:
        return []
    vec = TfidfVectorizer()
    tfidf = vec.fit_transform(items)
    idx = items.index(food_name.lower())
    sims = cosine_similarity(tfidf[idx], tfidf).flatten()
    sorted_idx = sorted(list(enumerate(sims)), key=lambda x: x[1], reverse=True)[1:]
    suggestions = []
    for i, score in sorted_idx:
        row = df.iloc[i]
        if max_cal and row['Cals_per100grams'] > max_cal:
            continue
        suggestions.append({
            "FoodItem": row['FoodItem'],
            "Calories": row['Cals_per100grams'],
            "Category": row['FoodCategory'],
            "Similarity": round(score * 100, 1)
        })
        if len(suggestions) == top_n:
            break
    return suggestions
