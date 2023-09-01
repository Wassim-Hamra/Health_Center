import numpy as np
from django.shortcuts import render
from polls import forms
from joblib import load
import numpy
# importing models
model_diabetes = load('./Models/diabetes_model.jbl')
scaler_diabetes = load('./Models/scaler_diabetes.jbl')





def index(request):
    form = forms.Message()
    if request.method == "POST":
        form = forms.Message(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, "index.html", context={"form": form})


def diabetes(request):
    if request.method == "POST":
        pregnancies = int(request.POST["pregnancies"])
        glucose = int(request.POST["glucose"])
        blood_pressure = int(request.POST["blood"])
        age = int(request.POST["age"])
        skin_thickness = int(request.POST["skin"])
        insulin = int(request.POST["insulin"])
        BMI = float(request.POST["bmi"])
        pedigree = float(request.POST["pedigree"])
        prediction = model_diabetes.predict(
            scaler_diabetes.transform(
                np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, BMI, pedigree, age]).reshape(1,
                                                                                                                      8))
        )
        if prediction[0] == 0:
            prediction = 0
        else:
            prediction = 1
        recommendation = ''
        average_glucose_range = (70, 120)
        average_BMI_range = (18.5, 24.9)
        average_blood_pressure_range = (90, 120)
        average_skin_thickness_range = (15, 25)
        average_insulin_range = (5, 15)

        if not (average_glucose_range[0] <= glucose <= average_glucose_range[1]):
            recommendation += f"\nMonitor your glucose levels regularly and consider a balanced diet. Optimal glucose range is between {average_glucose_range[0]} and {average_glucose_range[1]}."
        if not (average_BMI_range[0] <= BMI <= average_BMI_range[1]):
            recommendation += f"\nAim for a healthy weight through exercise and a balanced diet. Optimal BMI range is between {average_BMI_range[0]} and {average_BMI_range[1]}."
        if not (average_blood_pressure_range[0] <= blood_pressure <= average_blood_pressure_range[1]):
            recommendation += f"\nManage your blood pressure through lifestyle changes and, if necessary, medication. Optimal blood pressure range is between {average_blood_pressure_range[0]} and {average_blood_pressure_range[1]}."
        if not (average_skin_thickness_range[0] <= skin_thickness <= average_skin_thickness_range[1]):
            recommendation += f"\nFocus on overall health and fitness. Optimal skin thickness range is between {average_skin_thickness_range[0]} and {average_skin_thickness_range[1]}."
        if not (average_insulin_range[0] <= insulin <= average_insulin_range[1]):
            recommendation += f"\nConsider consulting a healthcare professional to manage insulin levels. Optimal insulin range is between {average_insulin_range[0]} and {average_insulin_range[1]}."

        recommendation_lines = recommendation.split('\n')
        if len(recommendation_lines)==1:
            recommendation_lines = ['',"Your health is on point. Keep up the good work !"]
        print(recommendation_lines)
        user_values = f"Pregnancies: {pregnancies} | Glucose: {glucose} | Blood Pressure: {blood_pressure} | Skin Thickness: {skin_thickness} | Insulin: {insulin} | BMI: {BMI} | Age: {age} | Pedigree: {pedigree}"

        return render(request, "result_diabetes.html",
                      context={'prediction': prediction, 'recommendation_lines': recommendation_lines[1:],
                               'user_values': user_values})
    else:
        return render(request, "diabetes.html", context={})


def heart(request):
    return render(request, "heart.html", context={})


def parkinson(request):
    return render(request, "parkinson.html", context={})
