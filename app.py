#from xray import logger
#from xray.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from xray.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
#from xray.pipeline.stage_03_training import ModelTrainingPipeline
#from xray.pipeline.stage_04_evaluation import EvaluationPipeline

from flask import Flask, request, justify, render_template
import os
from flask_cors import CORS, cross_origin
from xray.utils.common import decodeImage
#from xray.pipeline.predict import PredictionPipeline

 