import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

data = pd.read_csv("student_data.csv")

# Features (inputs) and target (output)
features = ['study_hours_per_week', 'attendance_pct', 'sleep_hours_per_day',
            'extracurricular', 'previous_gpa']
X = data[features]
y = data['final_score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
# print(y_pred)

print("\n\n===================================================")
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("===================================================\n\n")


while(True):
    hours = float(input("Study hours per week: "))
    attendance = float(input("Attendance %: "))
    sleep = float(input("Sleep hours per day: "))
    extra = int(input("Extracurricular (1 = yes, 0 = no): "))
    gpa = float(input("Previous GPA: "))

    # Predict
    student = pd.DataFrame([[hours, attendance, sleep, extra, gpa]], columns=features)
    score = model.predict(student)[0]

    print(f"Final score: {score:.1f}")
    print("\n")

    choice = input("Continue (y/n)?  ")
    if choice == "n":
        break
    print("\n")


print("\n============Exiting=================\n")