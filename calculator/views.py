from django.shortcuts import render

from . import nas_modul

def calculator(request):
    error_msg = None
    vysledek = None
    if request.method == "POST":
            try:
                float(request.POST["a"])
                float(request.POST["b"])
            except:
                error_msg = "A nebo B není číslo!"
                return render(request, "calculator/calculator.html", dict(error_msg=error_msg, vysledek=vysledek))

            if (float(request.POST["b"]) == 0 and request.POST["operator"] == "/"):
                    error_msg = "Chyba dělení nulou"
                    return render(request, "calculator/calculator.html", dict(error_msg=error_msg, vysledek=vysledek))
            if (request.POST["operator"] == "+"):
                vysledek = nas_modul.add(request.POST["a"], request.POST["b"])
            elif (request.POST["operator"] == "-"):
                vysledek = nas_modul.sub(request.POST["a"], request.POST["b"])
            elif (request.POST["operator"] == "/"):
                vysledek = nas_modul.divide(request.POST["a"], request.POST["b"])
            elif (request.POST["operator"] == "*"):
                vysledek = nas_modul.times(request.POST["a"], request.POST["b"])
            else:
                error_msg = "Něco se pokazilo :("
                return render(request, "calculator/calculator.html", dict(error_msg=error_msg, vysledek=vysledek))
    return render(request, "calculator/calculator.html", dict(error_msg=error_msg, vysledek=vysledek))