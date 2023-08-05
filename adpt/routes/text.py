from flask import Blueprint, request, jsonify
from adpt.model.model import ADPTModel
from adpt.model.utils import load_model, techniques
from adpt.model.inference import predict_labels_probs
from adpt.configs import load_config
from adpt.logger import logger
import numpy as np

config = load_config('config.yml')

routes = Blueprint('routes', __name__)

model_path = config.pop('model_path')
model = ADPTModel(**config)
model = load_model(model, model_path)

@routes.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.json.get('text', '') 
        
        if not isinstance(text, str):
            raise ValueError('Invalid "text" input. "text" must be a string.')

        get_probs = request.json.get('probs', False)

        probs = predict_labels_probs(text, model)

        if get_probs:
            result = dict(zip(techniques, probs))
            logger.info(f'Predicted probabilities: {result}')
        else:
            result = probs_to_labels(probs)
            logger.info(f'Predicted technique: {result}')
        return jsonify(result)
    except Exception as e:
        error_message = str(e)
        logger.error(f'Error during prediction: {error_message}')
        return jsonify({'error': error_message}), 400
    

def probs_to_labels(probs):
    labels_index = np.where(np.array(probs) > 0.5)[0]
    return [techniques[i] for i in labels_index]