from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
	return render(request,'website1/home.html')
def fun2(request):
	a='war'
	b='tum mile'
	c='joker'
	d='sahoo'
	my_dict={"mov1":a,"mov2":b,"mov3":c,"mov4":d}
	return render(request,'website1/movies.html',my_dict)