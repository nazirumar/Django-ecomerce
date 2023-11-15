from django.shortcuts import render


def file_not_found_404(request, exception):
    page_title = "Page Not Found"
    context ={
        'page_title': page_title
    }
    return render(request, "404.html", context)