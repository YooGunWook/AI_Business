from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')

def predict(request):
    return render(request, 'mainapp/predict.html')

def result(request):
    if request.method=='POST':
        group1 = int(request.POST.get('group1'))
        group2 = int(request.POST.get('group2'))
        group3 = int(request.POST.get('group3'))
        weekend = int(request.POST.get('weekend'))
        soccer = int(request.POST.get('soccer'))
        meantemp = float(request.POST.get('meantemp'))
        smalldust = float(request.POST.get('smalldust'))
        rainfall = float(request.POST.get('rainfall'))
        chickencall = 5.1933 + (0.0003 * smalldust) + (-0.0066 * meantemp) + (0.0011 * rainfall) + (0.3391 * weekend) + (-0.0087 * soccer) + (-2.1173 * group1) + (-1.7530 * group2) + (-0.3274 * group3)
        chickencall = round(chickencall, 2)
        chickencall = round(float(2.71828182846)**float(chickencall))
        return render(request,'mainapp/result.html',{'chickencall':chickencall})
    else:
        return render(request, 'mainapp/predict.html')