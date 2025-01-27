from django.shortcuts import render
import os
 
def index(request):
    image_folder = os.path.join('coolUIOfDeath', 'static', 'backgrounds')
    images = [
            f"{file}"
            for file in os.listdir(image_folder)
            if file.endswith(('jpg', 'jpeg', 'png', 'ico'))
        ]
    
    buttons = [
        ("192.168.1.186:8006", "proxmox.png", "proxmox"),
        ("http://jellyfin:8096", "jellyfin.png", "Jellyfin"), 
        ("http://cumulonimbus:9090", "nextcloud.png", "Nextcloud"),
        ("http://pihole/admin", "pihole.png", "Pihole"),
        ("https://torrentmachine:8080", "qbittorrent.png", "Torrents"),
        ("http://homeassistant:8123", "homeassistant.png", "Home Assistant"),
        ("/2nd", "test.png", "Website")
    ]
    
    return render(request, 'index.html', {'images': images, 'buttons': buttons})