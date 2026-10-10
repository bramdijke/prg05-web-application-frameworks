from django.shortcuts import render


def index(request):
    # Hard-coded data die we naar de template (de "view") sturen
    blogs = [
        {'title': 'Mijn eerste blog', 'author': 'Bram', 'text': 'Hallo wereld vanuit Django!'},
        {'title': 'Django vs Laravel', 'author': 'Bram', 'text': 'Beide werken met routes, controllers en views.'},
        {'title': 'Templates', 'author': 'Bram', 'text': 'In een template kun je met {{ }} data tonen.'},
    ]

    context = {
        'page_title': 'Mijn blogs',
        'blogs': blogs,
    }

    return render(request, 'blog/index.html', context)
