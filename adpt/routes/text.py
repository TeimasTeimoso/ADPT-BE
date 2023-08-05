from flask import Blueprint, request, jsonify
from adpt.model.model import ADPTModel
from adpt.model.utils import load_model, techniques
from adpt.model.inference import predict_labels_probs
from adpt.configs import load_config
from adpt.logger import logger

config = load_config('config.yml')

routes = Blueprint('routes', __name__)

model_path = config.pop('model_path')
model = ADPTModel(**config)
model = load_model(model, model_path)

@routes.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    
    probs = predict_labels_probs(text, model)
    probs = dict(zip(techniques, probs))

    logger.info(f'Predicted probabilities: {probs}')
    return jsonify(probs)
