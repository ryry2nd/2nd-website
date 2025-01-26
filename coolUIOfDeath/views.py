from django.shortcuts import render
import os
 
 
def index(request):
    image_folder = os.path.join('coolUIOfDeath', 'static', 'backgrounds')
    images = [
            f"{file}"
            for file in os.listdir(image_folder)
            if file.endswith(('jpg', 'jpeg', 'png', 'ico'))
        ]
    
    return render(request, 'index.html', {'images': images})