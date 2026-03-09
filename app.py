from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for
import rules

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        # 1. Data Acquisition
        age = int(request.form.get("age", 25))
        weight = float(request.form.get("weight", 70))
        height = float(request.form.get("height", 1.7))
        gender = request.form.get("gender")
        activity = request.form.get("activity", "Moderate")
        goal = request.form.get("goal", "Maintenance")
        high_bp = "bp" in request.form
        diabetes = "diabetes" in request.form

        # 2. Inference Logic
        bmi = weight / (height ** 2)
        bmi_category = rules.classify_bmi(bmi)

        # BMR Calculation
        if gender == "Male":
            bmr = (10 * weight) + (6.25 * height * 100) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height * 100) - (5 * age) - 161

        # TDEE (Total Daily Energy Expenditure)
        activity_factors = {"Sedentary": 1.2, "Moderate": 1.55, "Active": 1.725}
        tdee = bmr * activity_factors.get(activity, 1.2)
        
        # Goal adjustments based on WHO standards
        goal_map = {"Weight Loss": -500, "Muscle Gain": 350, "Maintenance": 0}
        calories = int(tdee + goal_map.get(goal, 0))

        # 3. Knowledge Retrieval
        diet = rules.get_diet_focus(bmi_category, goal)
        weekly_meals = rules.get_weekly_plan(goal)
        health_tips = rules.health_rules(high_bp, diabetes)

        # 4. Safety Guardrail Logic
        warning_message = None
        
        # If user is underweight but wants to loose weight, override the goal
        if bmi_category == "Underweight" and goal == "Weight Loss":
            goal = "Maintenance" # Force to maintenance for safety
            warning_message = "Notice: Your BMI indicates you are underweight. We have adjusted your plan to 'Maintenance' to ensure your health safety."
        # If user is obese but wants to gain muscle, prioritize weight management 
        if bmi_category == 'Obese' and goal == "Muscle Gain":
            warning_message = "Note: While focusing on muscle, ensure you prioritize low-calorie, high-protein Kenyan staples like Omena and Greens"

        # Apply calorie adjustments
        goal_map = {"Weight Loss": -500, "Muscle Gain": 350, "Maintenance": 0}
        calories = int(tdee + goal_map.get(goal, 0))

        # 5. Response Generation
        return render_template("result.html", 
                               bmi=round(bmi, 1), 
                               bmi_category=bmi_category,
                               calories=calories,
                               diet=diet,
                               weekly_meals=weekly_meals,
                               health_tips=health_tips,
                               warning_message=warning_message
                               )
    except Exception as e:
        return f"Calculation Error: {e}"
    

@app.route("/admin")
def admin():
    all_meals = rules.load_meals()
    return render_template("admin.html", all_meals=all_meals)

@app.route("/update_meal", methods=["POST"])
def update_meal():
    goal = request.form.get("goal")
    day_index = int(request.form.get("day_index"))
    
    meals = rules.load_meals()
    meals[goal][day_index]["bf"] = request.form.get("bf")
    meals[goal][day_index]["lunch"] = request.form.get("lunch")
    meals[goal][day_index]["supper"] = request.form.get("supper")
    
    rules.save_meals(meals)
    return redirect(url_for('admin'))
    
    

if __name__ == "__main__":
    app.run(debug=True)