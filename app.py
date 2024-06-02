import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
from keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import random
from tensorflow.keras.preprocessing.image import load_img, img_to_array


from llama_cpp import Llama
from homeassistant_api import Client
import secret
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

"""Create an instance of the Llama model"""

LLM = Llama(model_path="llama-2-7b-chat.Q5_K_M.gguf", n_ctx=1024)

app = Flask(__name__)

model = load_model('model.h5')
print('Model loaded. Check http://127.0.0.1:5000/')

labels = {0: 'Healthy', 1: 'Powdery', 2: 'Rust'}

def get_result(image_path):
    img = load_img(image_path, target_size=(225, 225))
    x = img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)[0] # here
    #return labels[np.argmax(predictions)] + " <h5>no</h5>" # -1
    result = np.argmax(predictions)
    if(result == 0):
        return "The leaf is healthy"
    elif(result == 1):
        texts = [
        "POWDERY detected. Prune Infected Leaves: Remove any leaves or plant parts showing signs of powdery mildew. This helps prevent the spread of the fungus to healthy parts of the plant.",
        "POWDERY detected. Improve Air Circulation: Powdery mildew thrives in humid conditions with poor air circulation. Increase airflow around your plants by spacing them out, pruning overcrowded branches, and avoiding dense planting.",
        "POWDERY detected. Water Wisely: Avoid overhead watering, as wet leaves provide an ideal environment for powdery mildew to develop. Water the soil directly at the base of the plant to keep foliage dry. Water early in the day so that leaves have time to dry before nightfall.",
        ]
        return random.choice(texts)
    else:
        texts = [
            "RUST detected. Apply Fungicides: Use fungicides labeled for rust control, such as those containing chlorothalonil, myclobutanil, or sulfur. Follow the application instructions and safety precautions provided on the product label.",
            "RUST detected. Clean Garden Tools: To prevent spreading rust spores, clean and disinfect garden tools after each use, especially if they come into contact with infected plants.",
            "RUST detected. Maintain Plant Health: Keep your plants healthy and vigorous by providing adequate sunlight, nutrients, and proper care. Healthy plants are better able to resist and recover from disease infections."
        ]
        return random.choice(texts)

@app.route('/')
def index():
    return render_template('index.html')





@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'
    f = request.files['file']
    if f.filename == '':
        return 'No selected file'
    if f:
        filename = secure_filename(f.filename)
        file_path = os.path.join('uploads', filename)
        try:
            # Ensure that the directory exists before saving the file
            os.makedirs('uploads', exist_ok=True)
            f.save(file_path)
            result = get_result(file_path)
            return result
        except Exception as e:
            return str(e)
    return 'Error'

@app.route('/fieldResult', methods=['POST'])
def fieldResult():
    LLM = Llama(model_path="llama-2-7b-chat.Q5_K_M.gguf", n_ctx=1024)


    ha_ip_addr = '10.11.22.52'
    entity_id_co2 = "sensor.psoc6_micropython_sensornode_working_space_co2_ppm"
    entity_id_temperature = "sensor.psoc6_micropython_sensornode_working_space_temperature"
    entity_id_light = "sensor.psoc6_micropython_sensornode_working_space_light"
    history_minutes = 5

    with Client(
        f'http://{ha_ip_addr}:8123/api',
        secret.ha_access_token
    ) as client:
    
        entity_co2 = client.get_entity(entity_id=entity_id_co2)
        entity_temperature = client.get_entity(entity_id=entity_id_temperature)
        entity_light = client.get_entity(entity_id=entity_id_light)

    # Get data from this entity id for last n minutes
        start = datetime.now() - timedelta(minutes=history_minutes)
        history_co2 = client.get_entity_histories(entities=[entity_co2], start_timestamp=start)
        history_temperature = client.get_entity_histories(entities=[entity_temperature], start_timestamp=start)
        history_light = client.get_entity_histories(entities=[entity_light], start_timestamp=start)

    # Go through each entity of the returned history data and save it's state values (here: atmospheric pressure) to a list
        for entry in history_co2:
            values_co2 = [float(x.state) for x in entry.states]

        for entry in history_temperature:
            values_temperature = [float(x.state) for x in entry.states]

        for entry in history_light:
            values_light = [float(x.state) for x in entry.states]


    fig, ax = plt.subplots()
    ax.plot(values_co2)
    ax.plot(values_temperature)
    ax.plot(values_light)



    prompt = f'These are CO2 measurement values of the last 5 minutes in ppm:\n' + \
         '\n'.join([str(v) for v in values_co2]) + \
         '\nThese are temperature measurement values of the last 5 minutes in Celcius:\n' + \
         '\n'.join([str(v) for v in values_temperature]) + \
         '\nThese are light measurement values of the last 5 minutes in lx:\n' + \
         '\n'.join([str(v) for v in values_light]) + \
         '\nDo you have a recommendation for our office based on these values?'

    print('Prompt:')
    print(prompt)

    output = LLM(prompt, max_tokens=2000)

    print('Model output:')
    print(output["choices"][0]["text"])

    print(output)

    return output["choices"][0]["text"]

if __name__ == '__main__':
    app.run(debug=True)