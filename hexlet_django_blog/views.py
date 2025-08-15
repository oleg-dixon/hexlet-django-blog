from django.shortcuts import render


def index(request):
    return render(
        request,
        'index.html',
        context={
            'app_name': 'Приложение на Django!',
        },
    )


def about(request):
    return render(
        request,
        'about.html',
    )