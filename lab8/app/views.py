# lab8/app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from .models import Framework, Language

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

