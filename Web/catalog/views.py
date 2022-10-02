from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Cover(request, *args,**kwargs):
	print(args, kwargs)
	return render(request, "cover.html", {})

def New_Data(request, *args,**kwargs):
	print(args, kwargs)
	return render(request, "add.php", {})

def Position(request, *args,**kwargs):
	print(args, kwargs)
	return render(request, "position.php", {})

def All_DATA(request, *args,**kwargs):
	print(args, kwargs)
	return render(request, "alldata.php", {})

def Scan(request, *args,**kwargs):
	print(args, kwargs)
	return render(request, "index_Scan.php", {})

def Search(request, *args,**kwargs):
	print(args, kwargs)
	return render(request, "index_Search.php", {})

def Logout(request, *args,**kwargs):
	print(args, kwargs)
	return render(request, "includes/logout.inc.php", {})
