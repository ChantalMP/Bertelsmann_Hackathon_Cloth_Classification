# from gender_recognizer import get_gender
# from os import listdir
# import os.path
# import PIL
# from PIL import Image
# import random
# from take_image import take_photo

# def recommend(image_url='camImage.png',wish="business",gender=None):
# 	if gender == None:
#     	gender = get_gender(image_url)
#     intern_gender = 'man' if gender=='male' else 'woman'

#     path = 'Images/recomendations/{}_{}'.format(wish, intern_gender)
#     pics = [f for f in listdir(path) if os.path.isfile(os.path.join(path, f))]
    
#     image = Image.open(path+'/'+pics[random.randint(0,len(pics)-1)])
#     #image.show()

#     return image





