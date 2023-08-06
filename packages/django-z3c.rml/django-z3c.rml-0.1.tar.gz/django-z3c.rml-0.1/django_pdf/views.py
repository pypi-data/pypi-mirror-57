from django.utils import timezone
from django.http import HttpResponse
from django.template import loader

from z3c.rml import rml2pdf


def pdf(request):
    response = HttpResponse(content_type='application/pdf')
    if 'download' in request.GET:
        response['Content-Disposition'] = 'attachment; filename=out_dj.pdf'
    pdf_template = rml2pdf.parseString(loader.render_to_string('pdf/hello.rml', {'title': "PDF"}))
    response.write(pdf_template.read())
    return response


def din5008(request):
    response = HttpResponse(content_type='application/pdf')
    if 'download' in request.GET:
        response['Content-Disposition'] = 'attachment; filename={0}.pdf'.format("out_dj")
    data = {'title': "PDF",
            'subject': "my subject",
            'date_local': timezone.now(),
            'user_name': request.user}
    address = {'address': "<b>address</b><br/>home",
               'address_extra': "extra",
               'info': "info<br/>foo",
               'address_return': "return address"}
    pdf_template = rml2pdf.parseString(loader.render_to_string('pdf/din5008.rml', {**data, **address}))
    response.write(pdf_template.read())
    return response
