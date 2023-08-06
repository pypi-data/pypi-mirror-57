#Django PDF
## reportlabs z3c.rml

https://github.com/zopefoundation/z3c.rml/

## Quick start

1. Add "django_pdf" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_pdf',
    ]

2. Include the django_pdf URLconf in your project urls.py like this::

    path('pdf/', include('django_pdf.urls')),

3. Run `python manage.py migrate` to create the django_pdf models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a pdf (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/pdf/ to view the demo pdfs.
