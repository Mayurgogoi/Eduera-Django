from django.shortcuts import render
from django.contrib import messages
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client['eduera-db']

# Create your views here.
def home(request):
    return render(request, "home.html")

def aboutUs(request):
    return render(request, "aboutus.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        messege = request.POST["messege"]

        contactDetails = {
            "name":name,
            "email":email,
            "subject":subject,
            "phone":phone,
            "message":messege,
            "datetime":datetime.now()
        }
        collection = db['contacts']
        collection.insert_one(contactDetails).inserted_id
        messages.success(request, 'Successfuly Sended !')
    return render(request, "contact.html")

def courses(request):
    Img = []
    for i in range(1,7):
        i = str(i)
        t_img = f"t-{i}.jpg"
        c_img = f"cu-{i}.jpg"
        Img.append({"teacherImg":t_img,"courseImg":c_img})
    return render(request, "courses.html", {"Img":Img})