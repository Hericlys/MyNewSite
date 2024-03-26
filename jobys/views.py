from django.shortcuts import redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib import messages
from .models import Joby


def new_joby(request) -> redirect:
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        project_type = request.POST.get('project-type')
        project_description = request.POST.get('project-description')

        if len(first_name) < 2 and len(last_name) < 2:
            messages.error(
                request,
                'Opa, tente não abreviar muito seu nome'
            )
            return redirect("pages:home")

        if len(phone) < 15:
            messages.error(
                request,
                'Use esse padrão "(00) 00000-0000" para digitar seu número'
            )
            return redirect("pages:home")

        try:
            validate_email(email)
        except ValidationError:
            messages.error(
                request,
                'Tem algo errado com seu E-mail, tente novamente'
            )
            return redirect("pages:home")

        if len(project_description) < 50:
            messages.error(
                request,
                'Não seja timido(a) me fale mais sobre seu projeto.'
            )
            return redirect("pages:home")

        create_new_joby = Joby(
            customer_first_name=first_name,
            customer_last_name=last_name,
            customer_phone=phone,
            customer_email=email,
            project_type=project_type,
            project_description=project_description
        )

        create_new_joby.save()

    send_mail(
        'Assunto',
        'Esse é o email de teste que estou te enviando',
        'webmail@mail.com',
        ['hericlysdesa@gmail.com']
    )

    messages.success(
        request,
        'Pedido enviado com sucesso! Verifique seu E-mail'
    )

    return redirect("pages:home")
