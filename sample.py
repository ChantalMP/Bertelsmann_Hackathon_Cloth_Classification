from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry

# Replace with a valid key
training_key = "1dcf529eee10461c951c4e1b324dcdc8"
prediction_key = "f5bbd790c81e4b379e0250cab326b1ab"

trainer = training_api.TrainingApi(training_key)

# Create a new project
print ("Creating project...")
project = trainer.create_project("My Project")

# Make two tags in the new project
casual_woman_tag = trainer.create_tag(project.id, "casual_woman_tag")
casual_man_tag = trainer.create_tag(project.id, "casual_man")

sport_woman_tag = trainer.create_tag(project.id, "sport_woman")
sport_man_tag = trainer.create_tag(project.id, "sport_man")

business_woman_tag = trainer.create_tag(project.id, "business_woman")
business_man_tag = trainer.create_tag(project.id, "business_man")

wedding_bride_tag = trainer.create_tag(project.id, "wedding_bride")


# Alternatively, if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following:

import os
casual_woman_dir = "Images\\casual_woman"
for image in os.listdir(os.fsencode("Images\\casual_woman")):
   with open(casual_woman_dir + "\\" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ casual_woman_tag.id ])

casual_man_tag_dir = "Images\\casual_man_tag"
for image in os.listdir(os.fsencode("Images\\casual_man_tag")):
   with open(casual_man_tag + "\\" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ casual_man_tag.id ])

sport_woman_dir = "Images\\sport_woman"
for image in os.listdir(os.fsencode("Images\\sport_woman")):
   with open(sport_woman_dir + "\\" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ sport_woman_tag.id ])

sport_man_tag_dir = "Images\\sport_man_tag"
for image in os.listdir(os.fsencode("Images\\sport_man_tag")):
   with open(sport_man_tag + "\\" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ sport_man_tag.id ])

business_woman_dir = "Images\\business_woman"
for image in os.listdir(os.fsencode("Images\\business_woman")):
   with open(business_woman_dir + "\\" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ business_woman_tag.id ])

business_man_tag_dir = "Images\\business_man_tag"
for image in os.listdir(os.fsencode("Images\\business_man_tag")):
   with open(business_man_tag + "\\" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ business_man_tag.id ])

business_man_tag_dir = "Images\\wedding_bride_tag"
for image in os.listdir(os.fsencode("Images\\wedding_bride_tag")):
   with open(wedding_bride_tag + "\\" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ wedding_bride_tag.id ])


import time

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status == "Training"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Make it the default project endpoint
trainer.update_iteration(project.id, iteration.id, is_default=True)
print ("Done!")


#PREDICTION
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

# Now there is a trained endpoint that can be used to make a prediction

predictor = prediction_endpoint.PredictionEndpoint(prediction_key)

# Alternatively, if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following.
#
# Open the sample image and get back the prediction results.
with open("Images\\test\\test_image.jpg", mode="rb") as test_data:
     results = predictor.predict_image(project.id, test_data.read(), iteration.id)

# Display the results.
for prediction in results.predictions:
    print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))


