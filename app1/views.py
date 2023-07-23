from django.shortcuts import render
from .models import app1
from .FormClass import market

# Create your views here.
def get_u(request):
    if(request.method=='POST'):
        form=market(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            item=form.cleaned_data['Item']
            quantity=form.cleaned_data['Quantity']
            rate=form.cleaned_data['Rate']
            amount=quantity*rate
            s=app1(Name=name,Item=item,Quantity=quantity,Rate=rate,Amount=amount)
            s.save()
    else:
        form=market()
    return render(request,'base.html',{'form':form})
def put_u(request):
    alll=app1.objects.all()
    all=alll.count()
    if all>=2:
        return render(request,'output.html',{'allval':alll})
    else:
        return render(request,'output11.html')
