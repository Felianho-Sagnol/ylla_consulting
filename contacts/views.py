from django.urls import reverse
from django.shortcuts import render, redirect
from email.mime.base import MIMEBase
from io import BytesIO

from email import encoders

from django.conf import settings

from django.core.mail import  EmailMessage, send_mail

from django.contrib import messages

from utils.pdf_render import render_to_pdf

from .forms import ContactForm
# Create your views here.


def contact(request):
    selection_type = request.POST.get("type_contact")
    print("La selection est:", selection_type)
    context = {}
    form = ContactForm(request.POST or None)
    if form.is_valid() and selection_type is not None:
        instance = form.save(commit=False)
        instance.type_contact = selection_type
        context["models_instance"] = instance
        contact_pdf = render_to_pdf("contacts/pj/contact_pdf.html", context)
        filename = """Prise de contact {prenom} {nom}.pdf""".format(prenom=instance.prenom, nom=instance.nom)
        instance.contact_document_pdf.save(filename,BytesIO(contact_pdf.content))
        subject = "Prise de contact de la part de {prenom} {nom}".format(prenom=instance.prenom, nom=instance.nom)

        with open(settings.BASE_DIR / "contacts/templates/contacts/pj/contact_pj_message.txt") as f:
            contact_pj_message = f.read()

        from_email = settings.EMAIL_HOST_USER
        to_email = ["ambaguirabatrdv@gmail.com", "bnvnmmnl@gmail.com",]


        email_to_staff = EmailMessage(
        subject = subject,
        body= contact_pj_message,
        from_email= from_email,
        to= to_email,)
        email_attachment = MIMEBase('application', "octet-stream")
        email_attachment.set_payload(instance.contact_document_pdf.read())
        encoders.encode_base64(email_attachment)
        email_attachment.add_header("Content-Disposition", "attachment", filename="{prenom}_{nom}.pdf".format(prenom= instance.prenom, nom=instance.nom))

        email_to_staff.attach(email_attachment)
        email_to_staff.send()
        messages.success(request, "Message envoyé avec succès")
        return redirect(reverse("rdv:services"))

    else:
        print("Non valide")
    context = {"form": form}

    return render(request, "contacts/contact.html", context)



def emplacement(request):
    context = {}

    return render(request, "contacts/emplacement.html", context)
