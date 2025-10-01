# predictor/views.py
from django.shortcuts import render
import pickle
import numpy as np

model = pickle.load(open('titanic_model.pkl', 'rb'))

def predict(request):
    if request.method == 'POST':
        pclass = int(request.POST['pclass'])
        sex = int(request.POST['sex'])
        age = float(request.POST['age'])
        fare = float(request.POST['fare'])
        
        prediction = model.predict([[pclass, sex, age, fare]])
        result = "Survived" if prediction[0] == 1 else "Did Not Survive"
        
        return render(request, 'result.html', {'result': result})

    return render(request, 'predict.html')
