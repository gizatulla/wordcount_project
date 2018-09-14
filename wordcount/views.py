from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()

    wordd={}

    for word in wordlist:
        if word in wordd:
            #Increase
            wordd[word] += 1
        else:
            #add to the dictionary
            wordd[word]=1

    wsorted = [(k, wordd[k]) for k in sorted(wordd, key=wordd.get, reverse=True)]
    wsorted=dict(wsorted)

    return render(request,'count.html',
                  {
                      'fulltext':fulltext,
                      'count':len(wordlist),
                      'wordd':wsorted.items()
                  })