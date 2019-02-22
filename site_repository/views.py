from django.shortcuts import render

# Create your views here.
def home(request):
    conhecimentos = ['HTML','CSS','JavaSccript','Python','Django','Git','Uncharted']

    return render(request, 'index.html', {'conhecimentos':conhecimentos})
