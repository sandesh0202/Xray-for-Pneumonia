import os
from xray import logger
from xray.pipeline.ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<</n/nx====================x")
     
except Exception as e:
    logger.exception(e)
    raise(e)


'''
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from xray.utils.common import decodeImage
#from xray.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp():
    def __init__(self) -> None:
        self.filename = "inputImage.jpg"
#        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods = ["GET"])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin
def trainRoute():
    os.system("python main.py")
    return "Training Done Successfully"

@app.route("/predict", methods=["POST"])
@cross_origin
def predictRoute():
    image = request.json["image"]
    decodeImage(filename, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080)
    '''