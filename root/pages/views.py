from django.http  import HttpResponse


def homePageView(request) -> HttpResponse:
    return HttpResponse('Initial View')
