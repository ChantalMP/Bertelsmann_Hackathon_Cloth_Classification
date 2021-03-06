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
casual_woman_tag = trainer.create_tag(project.id, "casual_woman")
casual_man_tag = trainer.create_tag(project.id, "casual_man")

sport_woman_tag = trainer.create_tag(project.id, "sport_woman")
sport_man_tag = trainer.create_tag(project.id, "sport_man")

business_woman_tag = trainer.create_tag(project.id, "business_woman")
business_man_tag = trainer.create_tag(project.id, "business_man")

# Alternatively, if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following:

import os
casual_woman_dir = "Images/casual_woman"
for image in os.listdir(os.fsencode(casual_woman_dir)):
   with open(casual_woman_dir + "/" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ casual_woman_tag.id ])

casual_man_dir = "Images/casual_man"
for image in os.listdir(os.fsencode(casual_man_dir)):
   with open(casual_man_dir + "/" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ casual_man_tag.id ])

sport_woman_dir = "Images/sport_woman"
for image in os.listdir(os.fsencode(sport_woman_dir)):
   with open(sport_woman_dir + "/" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ sport_woman_tag.id ])

sport_man_dir = "Images/sport_man"
for image in os.listdir(os.fsencode(sport_man_dir)):
   with open(sport_man_dir + "/" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ sport_man_tag.id ])

business_woman_dir = "Images/business_woman"
for image in os.listdir(os.fsencode(business_woman_dir)):
   with open(business_woman_dir + "/" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ business_woman_tag.id ])

business_man_dir = "Images/business_man"
for image in os.listdir(os.fsencode(business_man_dir)):
   with open(business_man_dir + "/" + os.fsdecode(image), mode="rb") as img_data:
       trainer.create_images_from_data(project.id, img_data.read(), [ business_man_tag.id ])

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