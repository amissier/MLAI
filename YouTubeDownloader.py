# Install pytube using the following command
!pip install pytube

import pytube

# choose a youtube video - note the following link is a link to my API talk which is 48minutes long

ds_url = 'https://www.youtube.com/watch?v=siUq4ZykORI&t=346s' 
try:
    video = pytube.YouTube(ds_url).streams.first()  
    video.download('.')  
    print("Downloaded successfully")
except:
    print("Error: There might be an issue with the url provided.")
