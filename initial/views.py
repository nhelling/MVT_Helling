from django.shortcuts import render
from initial.models import Initial



def list_initial(request):
    all_initial = Initial.objects.all()
    print(all_initial)
    context = {
        'initials':all_initial,        
    }
    return render(request, 'index.html', context=context)


