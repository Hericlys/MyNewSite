from django.shortcuts import render


def index(request) -> render:
    context = {
        'page_settings': {
            'title': 'Home',
        },
    }
    return render(request, "pages/index.html", context)
