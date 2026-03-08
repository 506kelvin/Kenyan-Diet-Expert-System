
# 🇰🇪 Kenyan Diet Expert System (KD-ES)

An intelligent, rule-based Expert System designed to provide personalized nutritional guidance and 7-day meal plans based on Kenyan dietary staples.

##  Features

* **BMI Analysis:** Calculates Body Mass Index and classifies users based on WHO standards.
* **Calorie Estimation:** Uses the Mifflin-St Jeor equation to calculate Total Daily Energy Expenditure (TDEE).
* **Knowledge Base:** A structured repository of traditional Kenyan meals (Ugali, Sukuma Wiki, Githeri, Omena, etc.).
* **Weekly Meal Planner:** Generates a full 7-day breakfast, lunch, and supper schedule tailored to user goals (Weight Loss, Muscle Gain, or Maintenance).
* **Health Alerts:** Provides specific medical advice for users with High Blood Pressure or Diabetes.
* **Admin Dashboard:** A dedicated interface for "Knowledge Engineers" to update the meal dictionary in real-time.

##  Expert System Architecture

This project follows the classic architecture of an Expert System:

1. **User Interface (Flask Web App):** Collects user data (weight, height, age, medical history).
2. **Inference Engine (`app.py`):** Processes the logic to determine calorie needs and matches the user profile to a diet category.
3. **Knowledge Base (`rules.py` & `meals.json`):** Contains the "if-then" rules for health advice and the nested dictionary of meal plans.

---

##  Getting Started

### Prerequisites

* Python 3.x
* Flask



## 🛠 Project Structure

* `app.py`: The Inference Engine and web controller.
* `rules.py`: The logical rules and data processing functions.
* `meals.json`: The externalized Knowledge Base (Database).
* `templates/`: The User Interface (HTML files).
* 

