import os



def get_filename(filepath):
	base_name = os.path.basename(filepath)
	name_file, extension_file = os.path.splitext(base_name)
	return name_file, extension_file
# 
# def get_file_name_and_ext(filename):
# 	name_file, extension_file = os.path.splitext(base_name)
# 	return n


def upload_file(instance, filename, location):
	id_ = instance.id
	if id_ is None:
		Klass = instance.__class__
		qs = Klass.objects.all().order_by("-pk")
		if qs.exists():
			id_ = qs.first().id + 1
		else:
			id_ = 0
	name_file, extension_file =get_filename(filename)

	final_filename = "{name_file}_{id_}{extension_file}".format(name_file=name_file, id_=id_, extension_file=extension_file)


	return f"{location}/{final_filename}"


def upload_file_location(instance, filename):
	name_product = instance.name
	id_ = instance.id
	if id_ is None:
		Klass = instance.__class__
		qs = Klass.objects.all().order_by("-pk")
		if qs.exists():
			id_ = qs.first().id + 1
		else:
			id_ = 0
	name_file, extension_file =get_filename(filename)

	final_filename = "{name_file}_{id_}{extension_file}".format(name_file=name_file, id_=id_, extension_file=extension_file)


	return "products/{name_product}/{final_filename}".format(name_product=name_product, final_filename=final_filename)



def upload_file_location_slide(instance, filename):
	id_ = instance.id
	if id_ is None:
		Klass = instance.__class__
		qs = Klass.objects.all().order_by("-pk")
		if qs.exists():
			id_ = qs.first().id + 1
		else:
			id_ = 0
	name_file, extension_file =get_filename(filename)

	final_filename = "{name_file}_{id_}{extension_file}".format(name_file=name_file, id_=id_, extension_file=extension_file)


	return "slide/{final_filename}".format(final_filename=final_filename)




def upload_file_blog(instance, filename):
	return upload_file(instance=instance, filename=filename,  location="blogs")


def upload_file_banniere(instance, filename):
	return upload_file(instance=instance, filename=filename,  location="baniere")
