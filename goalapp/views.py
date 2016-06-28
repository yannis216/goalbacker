from django.shortcuts import render

# Create your views here.
def front_site(request):
    return render(request, 'goalapp/front_site.html')
