# from gender_recognizer import get_gender
# from give_recomendation import recommend
# # from azure.cognitiveservices.vision.customvision.training import training_api

# training_key = "1dcf529eee10461c951c4e1b324dcdc8"
# prediction_key = "f5bbd790c81e4b379e0250cab326b1ab"
# pred_key_test = "81f0135a10924fa8baabe39c5adb8e4a"

# #PREDICTION
# from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
# from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

# Now there is a trained endpoint that can be used to make a prediction
# from take_image import take_photo

def evaluate_person(image_url='camImage.png', wish='casual', gender=None):
    from gender_recognizer import get_gender
    # from azure.cognitiveservices.vision.customvision.training import training_api

    training_key = "1dcf529eee10461c951c4e1b324dcdc8"
    prediction_key = "f5bbd790c81e4b379e0250cab326b1ab"
    pred_key_test = "81f0135a10924fa8baabe39c5adb8e4a"

    #PREDICTION
    from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
    from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

    # Now there is a trained endpoint that can be used to make a prediction
    from take_image import take_photo

    if gender == None:
       gender = get_gender(image_url)

    predictor = prediction_endpoint.PredictionEndpoint(pred_key_test)
    print(predictor)

    # Open the sample image and get back the prediction results.
    with open(image_url, mode="rb") as test_data:
         results = predictor.predict_image('109b6711-e20a-47cb-ad0e-c90e6103d689', test_data.read())

    # Display the results. and save
    predictions = {};
    for prediction in results.predictions:
        #print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))
        predictions[prediction.probability] = prediction.tag

    keys = predictions.keys()
    max_key = max(keys)
    best_prediction = predictions[max_key]
    
    intern_gender = 'man' if gender == 'male' else 'woman'

    print(best_prediction)
    print(wish+'_'+intern_gender)
    if best_prediction == wish+'_'+intern_gender:
        print('MATCH')
        return True,best_prediction

    else:
        return False,best_prediction



