from django.shortcuts import render

import datetime


from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template, render_to_string
from utils.pdf_render import render_to_pdf


# Create your views here.




def about(request):

	context = {}


	return render(request, "flex/about.html", context)
