# app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .models import Framework, Language

def send_test_email(request):
    # Enviar correo electrónico
    subject = "Test Email"
    message = "This is a test email from Django."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["cahuianthony6@gmail.com"]
    
    try:
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse("Test email sent successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def generate_pdf(request):
    languages = Language.objects.all()
    frameworks = Framework.objects.all()
    
    # Render the HTML template with context data
    html_string = render_to_string('pdf_template.html', {
        'languages': languages,
        'frameworks': frameworks
    })

    # Convert HTML to PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    # Create a HTTP response with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    return response
