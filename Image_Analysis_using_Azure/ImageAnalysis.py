
import os
import vision
# pip install msrest
from msrest.authentication import CognitiveServicesCredentials
# pip install azure-cognitiveservices-vision-computervision
from azure.cognitiveservices.vision.computervision import ComputerVisionClient

cog_key = 'YOUR_COG_KEY'
cog_endpoint = 'YOUR_COG_ENDPOINT'

# Get a client for the computer vision service
computervision_client = ComputerVisionClient(
    cog_endpoint, CognitiveServicesCredentials(cog_key))

# Get the path to an image file
image_path = os.path.join('data', 'iron.jpg')

# Specify the features we want to analyze
features = ['Description', 'Tags', 'Adult', 'Objects', 'Faces']

# Get an analysis from the computer vision service
image_stream = open(image_path, "rb")
analysis = computervision_client.analyze_image_in_stream(
    image_stream, visual_features=features)

# Show the results of analysis (code in vision.py)
vision.show_image_analysis(image_path, analysis)
