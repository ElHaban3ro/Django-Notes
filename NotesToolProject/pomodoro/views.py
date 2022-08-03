from django.shortcuts import render

# Create your views here.

def pomodoro(request):
    time = list(range(1, 61, 1))

    context = {'time': time}


    print(time)
    return render(request, 'pomodoro.html', context)