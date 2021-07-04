from django.shortcuts import render

#I have created this file - shlok
from django.http import HttpResponse
def index(request):
    return render(request, "base.html")
def analyzetext(request):
    txt = request.GET.get("text", "default")
    removepunc = request.GET.get("rp", "off")

    punctuations = '''.,;:'"!?*(){}[]-_<>/\@#$%^&`~'''
    analyzed = ""
    if removepunc == "on":
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char

        dicto = {
            'purpose': 'Remove punctuations',
            'analyzedtexts': analyzed,
        }
        return render(request, 'analyze.html', dicto)
    else:
        return HttpResponse("error")