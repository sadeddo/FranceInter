from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os
import json
import sys
import time
from PIL import Image
def personCount(nomImg):
       
        subscription_key = "f3ef8cd8abdc4aa986fea81498ca5aa5"
        endpoint = "https://api-ia.cognitiveservices.azure.com/"

        computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
        '''
        END - Authenticate
        '''
        images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")


        
        # Get local image with different objects in it
        local_image_path_objects = os.path.join (images_folder, nomImg)
        local_image_objects = open(local_image_path_objects, "rb")
        # Call API with local image
        detect_objects_results_local = computervision_client.detect_objects_in_stream(local_image_objects)

        if len(detect_objects_results_local.objects) == 0:
            print("No objects detected.")
        else:
            i=0
            for object in detect_objects_results_local.objects:
                if (object.object_property == 'person'):
                    i=i+1
            return(i)


        with open('fichier.json') as fichier:
                    y = {"nb_scanne" : i}
                    json.dump(y, "fichier.json")