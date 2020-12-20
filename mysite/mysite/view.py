from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'name': 'Sheetal', 'place': 'makrana'}
    return render(request, 'index.html', params)

def analyse(request):
    pText = request.POST.get('text' , 'default')
    removePunc = request.POST.get('removepunc','off')
    caps = request.POST.get('capslock','off')
    print(pText)
    print(removePunc)
    
    title=""
    punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*~`|_=+'''
    if removePunc == "on":
        analysed = ""
        for char in pText:
            if char not in punctuations:
               analysed = analysed + char;
               title = "Your punctuated text is-"
        pText = analysed
    if caps == "on":
        analysed = ""
        for char in pText:
            analysed = analysed + char.upper();
            title = "Your Capitalize text  is-"
        pText = analysed
    if removePunc == "on" and caps == "on":
        title = "Your punctuated and Capitalize text  is-"
    else:
        return HttpResponse("<h1>ERROR!</h1>please select atleast one chaeck box")

    params = {'heading':title,'punctext': analysed}
    return render(request, 'analyse.html' , params)

 