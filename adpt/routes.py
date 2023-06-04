from flask import Blueprint, request, jsonify
from model.model import ADPTModel
from model.utils import load_model, techniques
from model.inference import predict_labels_probs

routes = Blueprint('routes', __name__)

model = ADPTModel(20, [3], 1024, 128,  0.06)
model_path = 'models/adpt_finetuned_distilbert_cnn.bin'

model = load_model(model, model_path)

@routes.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    probs = predict_labels_probs(text, model)
    probs = dict(zip(techniques, probs))
    return jsonify(probs)
