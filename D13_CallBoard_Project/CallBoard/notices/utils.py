import os
from time import time
from itertools import chain


def generate_unique_name(path):
    def wrapper(instance, filename):
        extension = "." + filename.split('.')[-1]
        filename = str(time()*100)[:-6] + extension
        return os.path.join(path, filename)
    return wrapper


def get_content(obj, context):
    from .models import Image
    photos = obj.photo.all()
    videos = obj.video.all()
    content = list(chain(photos, videos))
    if len(content) > 0:
        context['first_con'] = content[0]
    if len(content) > 1:
        context['rest_con'] = content[1:]
    elif len(content) == 0:
        context['first_con'] = Image.objects.first()
    return context
