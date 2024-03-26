from django.shortcuts import redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.conf import settings
from .models import Joby


def new_joby(request) -> redirect:
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        project_type = request.POST.get('project-type')
        project_description = request.POST.get('project-description')

        # Validation
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
        
        # Created new joby
        create_new_joby = Joby(
            customer_first_name=first_name,
            customer_last_name=last_name,
            customer_phone=phone,
            customer_email=email,
            project_type=project_type,
            project_description=project_description
        )

        create_new_joby.save()
        
        # send e-mail
        html_content = render_to_string(
            'jobys/email/new_joby.html', 
            {
                'customer_full_name': first_name + ' ' + last_name,
                'project_type':project_type,
            }
        )

        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            'Confirmação de pedido de orçamento',
            text_content,
            settings.EMAIL_HOST_USER,
            [f'{email}',]
        )

        email.attach_alternative(html_content, 'text/html')
        email.send()

        # Message to User
        messages.success(
            request,
            'Pedido enviado com sucesso! Verifique seu E-mail'
        )

    return redirect("pages:home")
