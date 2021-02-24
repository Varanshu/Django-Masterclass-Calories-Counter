from django.shortcuts import render,redirect
from .models import Consume,Food

# Create your views here.
def index(request):
    if request.method=="POST":
        food_consumed = request.POST.get("food_consumed")
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consumed = Consume(user=user,food_consumed=consume)
        consumed.save()
        food = Food.objects.all()
    else:
        consumed_food = Consume.objects.filter(user=request.user)
        food = Food.objects.all()
    return render(request,'myapp/index.html',{
        'foods':food,
        'consumed_food':Consume.objects.filter(user=request.user)
    })

def delete_item(request,id):
    item = Consume.objects.get(id=id)
    if request.method=="POST":
        item.delete()
        return redirect('/')
    else:
        return render(request,"myapp/delete.html")
