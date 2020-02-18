from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()
    
    worddictionary = {}
    for word in wordlist:
        #increase count
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            #add word to dictionary
            worddictionary[word] = 1
    
    
    return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist),'worddictionary':worddictionary })
