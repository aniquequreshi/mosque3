def getmosqueinfo(request):
    from iftar.models import Mosque
    #return {'mosqueInfo': Mosque.objects.all()}
    return {'mosqueInfo': Mosque.objects.first()}