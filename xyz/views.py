from django.shortcuts import render
from django.http import HttpResponse
import markdown2

from encyclopedia import util

# Create your views here.
def page(request, name):
    try:
        return render(request, "xyz/index.html", {
            "contents": markdown2.markdown(util.get_entry(name)), "name":name
        })
    except: 
        return render(request, "xyz/error.html", {
            "query": name
        })