from django.shortcuts import redirect


def new_joby(request) -> redirect:
    if request.method == "POST":
        pass
    return redirect("pages:home")
