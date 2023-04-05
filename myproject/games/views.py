from django.http import HttpResponse
import requests


def home_view(request):
    url = "https://api-basketball.p.rapidapi.com/timezone"
    headers = {
        "X-RapidAPI-Key": "3abf050e2amsh9e5855714821316p1697a2jsnb693eba29248",
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    return HttpResponse(response)
