import torch
from torch import cuda
from adpt.model.model import ADPTModel
from transformers import DistilBertTokenizer
from typing import Tuple, List

device = 'cuda' if cuda.is_available() else 'cpu'
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

def load_model(model: ADPTModel, model_path: str) -> ADPTModel:
    model.load_state_dict(torch.load(model_path, map_location=torch.device(device)))
    model.to(device)
    model.eval() 
    return model

def encode_text(text: str) -> Tuple[torch.Tensor, torch.Tensor]:
    encoded_input = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        return_tensors='pt'
    )
    return encoded_input['input_ids'].to(device), encoded_input['attention_mask'].to(device)

def predict_probs(model: ADPTModel, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> List[float]:
    with torch.no_grad():
        logits = model(input_ids, attention_mask)
        probs = torch.sigmoid(logits).tolist()[0]
        return probs
    
techniques = [
    'Appeal to authority',
    'Appeal to fear/prejudice',
    'Bandwagon',
    'Black-and-white Fallacy/Dictatorship',
    'Causal Oversimplification',
    'Doubt',
    'Exaggeration/Minimisation',
    'Flag-waving',
    'Glittering generalities (Virtue)',
    'Loaded Language',
    'Misrepresentation of Someone\'s Position (Straw Man)',
    'Name calling/Labeling',
    'Obfuscation, Intentional vagueness, Confusion',
    'Presenting Irrelevant Data (Red Herring)',
    'Reductio ad hitlerum',
    'Repetition',
    'Slogans',
    'Smears',
    'Thought-terminating cliché',
    'Whataboutism'
]