from django.shortcuts import render,redirect
from random import randrange
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'es-CL') 

# Create your views here.
def index(request):
    return render(request, "index.html")

def process_money(request):
    datenow = datetime.now()
    formatDate = datenow.strftime("%d-%B-%Y %H:%M:%S %p")
    # print(request.session["gold"])
    if 'gold' in request.session:
        # print(request.POST)
        if request.POST['tipo'] == 'farm':
            val = randrange(10, 21, 1)
        elif request.POST['tipo'] == 'cave':
            val = randrange(5,11,1)
        elif request.POST['tipo'] == 'house':
            val = randrange(2,6,1)
        elif request.POST['tipo'] == 'casino':
            val = randrange(-50,51,1)
        request.session['gold'] += val
        # print(request.session["info"])
        if val > 0:
            request.session['info'].append({'class': 'verde', 'msg': f"Earned {val} golds from the {request.POST['tipo']}! {formatDate}"})
        else:
            request.session['info'].append({'class': 'rojo', 'msg': f"Entered a casino and lost {-1*val} golds at the {request.POST['tipo']}... Ouch!!! {formatDate}"})
    else:
        request.session['gold'] = 0
        request.session['info'] = []

    return redirect("/")

def reset(request):
    request.session['gold'] = 0
    request.session['info'] = []
    return redirect('/')