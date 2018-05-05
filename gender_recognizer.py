import cognitive_face as CF
import urlparse
import urllib
# import urllib.parse, urllib.error
import requests
import json

from take_image import take_photo

def get_gender(image_path='camImage.png'):
    take_photo()
    print('HEY')
    KEY = '5aac802b7953441f89b56f5f33b1d3a4'  # Replace with a valid subscription key (keeping the quotes in place).
    # You can use this example JPG or replace the URL below with your own URL to a JPEG image.
    #LOAD PIC FROM ROBOT

    face_api_url = 'https://southcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    headers = {
        # Request headers
         'Content-type': 'application/octet-stream',
         'Ocp-Apim-Subscription-Key': KEY,
    }

    params = urllib.urlencode({
        # Request parameters
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'gender',
    })

    data = open(image_path, 'rb').read()

    response = requests.post(face_api_url, data=data, params=params, headers=headers)
    faces = response.json()
    if len(faces) > 0:
        gender = faces[0]['faceAttributes']['gender']
    else:
        return 'male'

    print(gender)
    return gender


get_gender()