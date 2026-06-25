from dotenv import load_dotenv
import os
import joblib
load_dotenv(override=True)
APP_NAME=os.getenv("APP_NAME")
VERSION=os.getenv("VERSION")
SECRET_KEY_TOKEN=os.getenv("SECRET_KEY_TOKEN")



PATH_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# L:\courses\AI Agoor Course\NEW Material Udemy\04- Machine Learning\sec 9\MY PROJECT\Models\processor.pkl

#  L:\courses\AI Agoor Course\NEW Material Udemy\04- Machine Learning\sec 9\MY PROJECT\Models\processor.pkl
MODEL_FOLDER_PATH=os.path.join(PATH_DIR,"Models")
preprocessor=joblib.load(os.path.join(MODEL_FOLDER_PATH,"processor.pkl"))
RandomForestTuned=joblib.load(os.path.join(MODEL_FOLDER_PATH,"RandomForestTuned.pkl"))
xgb_tuned=joblib.load(os.path.join(MODEL_FOLDER_PATH,"xgb_tuned.pkl"))


