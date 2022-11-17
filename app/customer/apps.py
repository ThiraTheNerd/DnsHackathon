from django.apps import AppConfig
import os
import joblib
from django.conf import settings

class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
    MODEL_FILE = os.path.join(settings.MODELS, "DecisionTreeModel.joblib")
    model = joblib.load(MODEL_FILE)