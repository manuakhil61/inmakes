from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,'home.html')

# def about(request):
#     return render(request,'about.html')
#
# def contact(request):
#     return render(request,'contact.html')
#
# def details(request):
#     return render(request,'details.html')
#
# def thanks(request):
#     return render(request,'thanks.html')
#
# def operations(request):
#     X=int(request.GET['number1'])
#     Y = int(request.GET['number2'])
#     res=X+Y
#     res1=X*Y
#     res2=X-Y
#     res3=X/Y
#     return render (request,"home.html",{'addition':res,'multiply':res1,'sub':res2,'divide':res3})