from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import util
from django.urls import reverse 
import markdown2

import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def rand(request):
    return HttpResponseRedirect(f"/wiki/{random.choice(util.list_entries())}")

def search(request):
    query = request.GET.get('q')
    list = util.list_entries()
    if query in list:
        return HttpResponseRedirect(f"/wiki/{query}")
    elif any(query in x for x in list) == True:
        valid = [x for x in list if query in x]
        return render(request, "encyclopedia/searchResults.html", {
            "entries":valid,
        })
    else:
        return HttpResponseRedirect(f"/wiki/{query}")
def create(request):
    return render(request, "encyclopedia/create.html")
def post(request):
    title = request.GET.get('title')
    desc = request.GET.get('textarea')
    if title not in util.list_entries():
        util.save_entry(title,desc)
        return HttpResponseRedirect(f'/wiki/{title}')
    else:
        return render(request, "encyclopedia/error.html", {"title":title

        })
def edit(request):
    name = request.GET.get('name')
    return render(request,"encyclopedia/edit.html",{
        "name":name,"desc":util.get_entry(name)
    })

def append(request):
    title = request.GET.get('title')
    desc = request.GET.get('textarea')
    util.save_entry(title,desc)
    return HttpResponseRedirect(f'/wiki/{title}')

def page(request, name):
    print(request)
    print(name)
    try:
        return render(request, "encyclopedia/wikiIndex.html", {
            "contents": markdown2.markdown(util.get_entry(name)), "name":name
        })
    except: 
        return render(request, "encyclopedia/wikiError.html", {
            "query": name
        })