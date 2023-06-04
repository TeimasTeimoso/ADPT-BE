from typing import List
from model.model import ADPTModel
from model.utils import encode_text, predict_probs
    
def predict_labels_probs(text: str, model: ADPTModel) -> List[float]:
    input_ids, attention_mask = encode_text(text)
    probs = predict_probs(model, input_ids, attention_mask)
    
    return probs