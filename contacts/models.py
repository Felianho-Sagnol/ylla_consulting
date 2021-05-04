from django.db import models

# Create your models here.


class Contact(models.Model):
    nom = models.CharField("Nom", max_length=255)
    prenom = models.CharField("Prénom", max_length=255)
    email  = models.EmailField("Email")
    type_contact = models.CharField("Type", max_length=255)
    sujet  = models.CharField("Sujet", max_length=255)
    message = models.TextField()
    timestamp   = models.DateTimeField("Création", auto_now_add=True)
    updated     = models.DateTimeField("Modification", auto_now=True)
    contact_document_pdf = models.FileField(upload_to="rdv_pp_document", null=True, blank=True)


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ["-timestamp", "-updated"]
