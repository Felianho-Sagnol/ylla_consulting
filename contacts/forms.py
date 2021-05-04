
from django import forms


from captcha.fields import ReCaptchaField, ReCaptchaV3


from .models import Contact



class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(
    widget=ReCaptchaV3(
        attrs={
            'required_score':0.95,
        }
        )
    )
    class Meta:
        model = Contact
        fields = ["prenom", "nom", "email", "sujet", "message"]

        widgets = {
            "prenom": forms.TextInput(
            attrs = {
            # "class": "form-control input-sm",
            "placeholder": "Votre prénom",


            }
            ),
        	"nom": forms.TextInput(
					attrs = {
						# "class": "form-control input-sm",
                        "placeholder": "Votre nom",

					}
			),

			"email": forms.EmailInput(
					attrs = {
						# "class": "form-control input-sm",
                        "placeholder": "E-Mail",


					}
			),


            "sujet": forms.TextInput(
            attrs = {
            # "class": "form-control input-sm",
            "placeholder": "Sujet",


            }
            ),
        	"message": forms.Textarea(
					attrs = {
						# "class": "form-control input-sm",
                        "placeholder": "Votre message",

					}
			),

        }
