from django.shortcuts import render

from poete.models import NomPoete

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import string


def page(request):
    accounts = NomPoete.objects.all()
    paginator = Paginator(accounts, 25)
    page = request.GET.get('page')

    lettres = string.ascii_uppercase
    try:
        accounts = paginator.page(page)
    except PageNotAnInteger:
        accounts = paginator.page(1)
    except Emptypage:
        accounts = paginator.page(paginator.num_pages)
    return render(request, 'fr/public/accounts.html', {'accounts': accounts, 'lettres': lettres})




