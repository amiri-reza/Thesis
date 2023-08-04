from django.views.generic import TemplateView
from cutting_performance.views import CuttingData, Abrasive, NaturalStone
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Users
from django.core.mail import send_mail
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import EmailForm
import logging
import os
import json

class MainPage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmailForm()
        return context

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            text = json.dumps({
                'sender_name': form.cleaned_data['sender_name'],
                'sender_email': form.cleaned_data['sender_email'],
                'text': form.cleaned_data['text'],
            })
            subject = form.cleaned_data['subject']
            sender_name = form.cleaned_data['sender_name']
            sender_email = form.cleaned_data['sender_email']

            try:
                send_mail(
                    subject=subject,
                    message=text,
                    from_email=f'{sender_name} <{sender_email}>',
                    recipient_list=['amiri.reza68@yahoo.com'],
                    fail_silently=False,
                    auth_user=os.getenv("EMAIL_HOST_USER"),
                    auth_password=os.getenv("EMAIL_HOST_PASSWORD"),
                )

                logger = logging.getLogger('email_app')  
                logger.info('Email sent successfully!')
                return self.render_to_response(self.get_context_data(success=True))
            

            except Exception as e:
                logger = logging.getLogger('email_app') 
                logger.error(f'Error sending email: {str(e)}')

                error_message = str(e)
                return self.render_to_response(self.get_context_data(form=form, error_message=error_message))

        return self.render_to_response(self.get_context_data(form=form))
    

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    def get_context_data(self):
        context = super().get_context_data()
        
        context["user"] = Users.objects.get(id = self.request.user.id)
        #breakpoint()
        context["stones"] = NaturalStone.objects.all()
        context["stones_num"] = NaturalStone.objects.count()
        context["abrasives"] = Abrasive.objects.all()
        context["abrasives_num"] = Abrasive.objects.count()
        context["cutting_data"] = CuttingData.objects.all()
        context["cut_num"] = CuttingData.objects.count()
        context["plots_num"] = NaturalStone.objects.count()
        return context
