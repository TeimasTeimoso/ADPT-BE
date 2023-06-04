class Config:
    DEBUG = True
    model_path = 'models/adpt_finetuned_distilbert_cnn.bin'
    
class DevConfig(Config):
    pass

class ProdConfig(Config):
    DEBUG = False