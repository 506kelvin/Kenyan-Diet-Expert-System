# rules.py

# The Knowledge Base: A structured dictionary of Kenyan meals
import json
import os

# Path to our "Database"
DATA_FILE = 'meals.json'

def load_meals():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_meals(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_weekly_plan(goal):
    meals = load_meals()
    return meals.get(goal, meals.get("Maintenance", []))


def classify_bmi(bmi):
    if bmi < 18.5: return "Underweight"
    elif 18.5 <= bmi < 25: return "Normal"
    elif 25 <= bmi < 30: return "Overweight"
    else: return "Obese"

def get_diet_focus(bmi_category, goal):
    if goal == "Weight Loss" or bmi_category in ["Overweight", "Obese"]:
        return "High Fiber & Indigenous Greens"
    elif goal == "Muscle Gain":
        return "High Protein & Complex Starches"
    else:
        return "Balanced Kenyan Wholefoods"


def health_rules(high_bp, diabetes):
    recommendations = []
    if high_bp:
        recommendations.append("Limit salt; use garlic and ginger for flavor.")
    if diabetes:
        recommendations.append("Use whole grains (Brown Ugali) to control blood sugar.")
    if not recommendations:
        recommendations.append("Drink 8 glasses of water daily.")
        recommendations.append("Walk for 30 minutes every day.")
    return recommendations