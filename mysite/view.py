from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	# return HttpResponse("<h1>hello Koushik I am your guide for today.</h1>")
	return render(request, "home.html")

def count(request):
	fulltext = request.GET['fulltext']
	wordCount = len(fulltext.split())
	wordList = {}
	for i in fulltext.split():
		if i in wordList:
			wordList[i] += 1
		else:
			wordList[i] = 1
	sortWordList = sorted(wordList.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, "count.html", {'fulltext': fulltext, 'wordCount': wordCount, 'sortWordList': sortWordList})

def about(request):
	return render(request, "about.html")
