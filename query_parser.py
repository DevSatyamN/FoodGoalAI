# query_parser.py
import spacy
nlp = spacy.load("en_core_web_sm")

def parse_query(query):
    doc = nlp(query.lower())
    filters = {"nutrient": None, "calorie_limit": None, "direction": None, "category": None}
    for token in doc:
        if token.text in ["protein", "fat", "sugar"]:
            filters["nutrient"] = token.text
        elif token.like_num:
            filters["calorie_limit"] = int(token.text)
        elif token.text in ["under", "below", "less"]:
            filters["direction"] = "under"
        elif token.text in ["over", "above", "more"]:
            filters["direction"] = "over"
        elif token.text in ["snack", "fruit", "dairy", "meat"]:
            filters["category"] = token.text.capitalize()
    return filters

def search_foods(df, filters):
    result = df.copy()
    if filters["category"]:
        result = result[result["FoodCategory"] == filters["category"]]
    if filters["direction"] == "under" and filters["calorie_limit"]:
        result = result[result["Cals_per100grams"] <= filters["calorie_limit"]]
    elif filters["direction"] == "over" and filters["calorie_limit"]:
        result = result[result["Cals_per100grams"] >= filters["calorie_limit"]]
    return result[["FoodItem", "FoodCategory", "Cals_per100grams"]].head(10)
