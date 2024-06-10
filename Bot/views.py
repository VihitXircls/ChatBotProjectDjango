from django.shortcuts import render
import json
from django.http import JsonResponse
from decouple import config
import google.generativeai as genai
# Create your views here.
GEMINI_API_KEY = config('GEMINI_API_KEY')
def index(request):
    customer_query = str(request.POST.get('query')).capitalize()
    employee_reply = {"message":""}
    # with open('/home/sys17/Desktop/Vihit/ChatBot/Bot/BOT_JSON_DATA/chat.json', 'r') as file:
    #     data = json.load(file)
    # for query in data:
    #     if query["Customer"] == customer_query:
    #         employee_reply["message"] = query["Employee"]
    
    # if employee_reply["message"] == "":
    #     return JsonResponse({"message":"Invalid Query"})
    # return JsonResponse(employee_reply)
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(f'Act as a customer relationship manager of an e-commerce store. I want you to reply to the customer query which I have provided in a professional manner. Make sure the responses are 100% accurate.Customer Query is: {customer_query}')
    employee_reply['message'] = response.text

    print(response.text)
    return JsonResponse(employee_reply)
