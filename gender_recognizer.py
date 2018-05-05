import cognitive_face as CF
import urllib.parse, urllib.error
import requests
import json

def get_gender(image_path='Images/test/test_image_man.jpg'):
    KEY = '5aac802b7953441f89b56f5f33b1d3a4'  # Replace with a valid subscription key (keeping the quotes in place).
    # You can use this example JPG or replace the URL below with your own URL to a JPEG image.
    #LOAD PIC FROM ROBOT

    face_api_url = 'https://southcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    headers = {
        # Request headers
         'Content-type': 'application/octet-stream',
         'Ocp-Apim-Subscription-Key': KEY,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'gender',
    })

    data = open(image_path, 'rb').read()

    response = requests.post(face_api_url, data=data, params=params, headers=headers)
    faces = response.json()
    gender = faces[0]['faceAttributes']['gender']

    return gender