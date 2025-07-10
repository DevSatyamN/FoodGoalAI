# goal_predictor.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def train_model(df):
    df['GoalLabel'] = df['Cals_per100grams'].apply(
        lambda x: 'weight loss' if x <= 100 else 'weight gain' if x >= 200 else 'maintenance')
    X = df[['Cals_per100grams', 'KJ_per100grams']]
    y = df['GoalLabel']
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y_encoded)
    return model, le

def predict_goal(model, le, cal, kj):
    return le.inverse_transform(model.predict([[cal, kj]]))[0]
