import os
import io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'my_work.json'

client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
client = vision.ImageAnnotatorClient(client_options=client_options)


def detectText(img):
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)

    return response.text_annotations


def pandasRead(texts):
    df = pd.DataFrame(columns=['locale', 'description'])
    df = df.append(
        dict(
            locale=texts[0].locale,
            description=texts[0].description
        ),
        ignore_index=True
    )
    return df
