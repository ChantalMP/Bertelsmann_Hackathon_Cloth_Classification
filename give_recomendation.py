from gender_recognizer import get_gender
from os import listdir
import os.path
import PIL
from PIL import Image
import random

def recommend(image_url='Images/test/test_image_man.jpg',wish="business"):
    gender = get_gender(image_url)
    intern_gender = 'man' if gender=='male' else 'woman'

    path = 'Images/recomendations/{}_{}'.format(wish, intern_gender)
    pics = [f for f in listdir(path) if os.path.isfile(os.path.join(path, f))]

    image = Image.open(path+'/'+pics[random.randint(0,len(pics)-1)])
    #image.show()

    return image





