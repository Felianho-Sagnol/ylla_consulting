

from django.conf import settings

def ga_tracking_id(request):
    return {'ga_tracking_id': settings.GA_TRACKING_ID}






def use_ga(request):
    return {'use_ga': settings.USE_GA}






def ipinfo_token(request):
    print("Il a été appelé, voici le token", settings.IPINFO_TOKEN)
    return {'ipinfo_token': settings.IPINFO_TOKEN}
