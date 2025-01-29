from django.shortcuts import render
import requests
from django.http import HttpResponse
import pickle
import os
from django.conf import settings

def home(request):
    return render(request, 'index.html')
MODEL_PATH = os.path.join(settings.BASE_DIR, 'spam_mail', 'static', 'model.sav')

def spam_prediction(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()  # Ensure no NoneType issues
        if not email:
            return render(request, 'index.html', {'result': 'Invalid input'})

        if not os.path.exists(MODEL_PATH):
            return render(request, 'index.html', {'result': 'Model file not found'})

        with open(MODEL_PATH, 'rb') as model_file:
            model = pickle.load(model_file)

        try:
            prediction = model.predict([email])[0]  # Ensure correct indexing
            result = 'Spam' if prediction == 1 else 'Not Spam'
        except Exception as e:
            result = f"Error: {str(e)}"

        return render(request, 'index.html', {'result': result})

    return render(request, 'index.html')



