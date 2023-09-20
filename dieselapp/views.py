from django.shortcuts import render

from dieselapp.models import*
from django.http import HttpResponseRedirect


def index(request):
	r=product.objects.all()
	return render(request,'index.html',{'iii':r})

def reg(request):
	if request.method=='POST':
		n=request.POST['name']
		e=request.POST['email']
		p=request.POST['pd']
		t=request.POST['sele']
		if tools.objects.filter(em=e):
			return render(request,'registration.html',{'msg':'email already exist'})
		else:
			if t=='user':
				c=tools(na=n,em=e,pd=p ,usertype='user',status='approve')
				c.save()
	return render(request,'registration.html')


def log(request):
	if request.method=='POST':
		e=request.POST['email']
		p=request.POST['pd']
		g=tools.objects.filter(em=e,pd=p,status='approve')
		if g:
			for h in g:
				ut=h.usertype
				if ut=='user':
					return HttpResponseRedirect('/')
				elif(ut=='admin'):
					return HttpResponseRedirect('/addproduct/')
		
		else:
			return render(request,'login.html',{'msg':'invalid email or password'})

	return render(request,'login.html')
def addproduct(request):
	if request.method=='POST':
		pn=request.POST['pname']
		pr=request.POST['price']
		p=request.FILES['file']
		a=product(pname=pn,price=pr,t=p)
		a.save()
	return render(request,'addproduct.html')

def productdetails(request):
	r=product.objects.all()
	return render(request,'productdetails.html',{'ww':r})

def updateid(request):
	f=request.GET['i_d']
	x=product.objects.filter(id=f)
	return render(request,'update.html',{'ww':x})

def update(request):
	if request.method=='POST':
		pn=request.POST['pname']
		pr=request.POST['price']
		u=request.POST['u_id']
		t=product.objects.filter(id=u).update(pname=pn,price=pr)
		return HttpResponseRedirect('/productdetails/')
	

def removep(request):
	k=request.GET['i_d']
	y=product.objects.filter(id=k).delete()
	return HttpResponseRedirect('/productdetails/')


def steth(request):
	return render(request,'stethscope.html')

def probe(request):
	return render(request,'probe.html')

def multimkit(request):
	return render(request,'multim kit.html')


def product_id(request):
	m=request.GET['i_d']
	o=product.objects.filter(id=m)
	return render(request,'productdetails',{'msg':o})


def shop(request):
	d=product.objects.all()
	return render(request,'shop.html',{'msg':d})
	


# Create your views here.
