# Student Score Prediction using Linear Regression

## 📌 Overview

This is my first machine learning training project, built using **Python, NumPy, Pandas, and Scikit-learn**.

The project uses **Linear Regression** to predict a student's final score based on academic and lifestyle-related features.

The model takes the following inputs:

* Study hours per week
* Attendance percentage
* Sleep hours per day
* Extracurricular activity
* Previous GPA

It then predicts the student's expected **final score**.

---

## 🤖 Machine Learning Model

**Algorithm:** Linear Regression

**Learning Type:** Supervised Learning

**Problem Type:** Regression

The model learns relationships between the input features and the student's final score using the training data.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

### Scikit-learn Components

* `LinearRegression`
* `train_test_split`
* `mean_absolute_error`
* `mean_squared_error`

---

## 📊 Features

The model uses five features:

| Feature                | Description                     |
| ---------------------- | ------------------------------- |
| `study_hours_per_week` | Student's weekly study hours    |
| `attendance_pct`       | Student's attendance percentage |
| `sleep_hours_per_day`  | Average daily sleep hours       |
| `extracurricular`      | 1 = Yes, 0 = No                 |
| `previous_gpa`         | Student's previous GPA          |

### Target

```text
final_score
```

The target is the student's final score that the model attempts to predict.

---

## 🔄 Machine Learning Workflow

```text
Student Dataset
      ↓
Load Dataset with Pandas
      ↓
Select Features (X)
      ↓
Select Target (y)
      ↓
Split Data
      ↓
Training Data + Testing Data
      ↓
Train Linear Regression Model
      ↓
Make Predictions
      ↓
Evaluate Model
      ↓
Predict Score for a New Student
```

---

## 📈 Model Evaluation

The model is evaluated using:

### MAE — Mean Absolute Error

Measures the average absolute difference between the actual and predicted scores.

### MSE — Mean Squared Error

Measures the average squared difference between actual and predicted scores.

### RMSE — Root Mean Squared Error

The square root of MSE, giving the error in approximately the same units as the target.

The program automatically displays these metrics after training.

---

## 💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/CodewithAwais05/student-score-prediction-linear-regression.git
```

### 2. Open the project directory

```bash
cd student-score-prediction-linear-regression
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the program

```bash
python main.py
```

---

## 🧪 Example

The program asks for information about a student:

```text
Study hours per week: 20
Attendance %: 85
Sleep hours per day: 7
Extracurricular (1 = yes, 0 = no): 1
Previous GPA: 3.4
```

The trained model then produces a predicted final score:

```text
Final score: XX.X
```

The program can continue predicting scores for additional students until the user chooses to exit.

---

## 📁 Project Structure

```text
student-score-prediction-linear-regression/
│
├── main.py
├── student_data.csv
├── requirements.txt
└── README.md
```

---

## 🎯 Learning Objectives

Through this project, I practiced:

* Loading datasets using Pandas
* Selecting features and targets
* Splitting datasets into training and testing sets
* Training a machine learning model
* Making predictions
* Evaluating regression models
* Using Scikit-learn
* Creating predictions from new user input
* Understanding the basic machine learning workflow

---

## 🚀 Future Improvements

Possible future improvements include:

* Data preprocessing
* Handling missing values
* Feature scaling
* Data visualization
* R² evaluation
* Comparing multiple regression models
* Saving and loading the trained model
* Building a graphical/web interface

---

## 👨‍💻 Author

**Awais**

BS Artificial Intelligence Student

GitHub: [CodewithAwais05](https://github.com/CodewithAwais05)
