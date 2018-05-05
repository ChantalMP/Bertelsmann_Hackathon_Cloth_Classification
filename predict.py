from sample import prediction_key, training_key, trainer, iteration, project
from gender_recognizer import get_gender
from give_recomendation import recommend

#PREDICTION
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

# Now there is a trained endpoint that can be used to make a prediction

def evaluate_person(image_url='Images/test/test_image.jpg', wish='business'):

    predictor = prediction_endpoint.PredictionEndpoint(prediction_key)

    # Open the sample image and get back the prediction results.
    with open(image_url, mode="rb") as test_data:
         results = predictor.predict_image(project.id, test_data.read(), iteration.id)

    # Display the results. and save
    predictions = {};
    for prediction in results.predictions:
        print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))
        predictions[prediction.probability] = prediction.tag

    keys = predictions.keys()
    max_key = max(keys)
    best_prediction = predictions[max_key]
    #print(best_prediction)
    gender = get_gender(image_url)
    intern_gender = 'man' if gender == 'male' else 'woman'

    if best_prediction == wish+'_'+gender:
        return (True, None)
    
    else:
        return (False, recommend(image_url, wish))



