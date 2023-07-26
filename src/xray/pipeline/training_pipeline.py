from xray.config.configuration import ConfigurationManager
from xray.components.prepare_callbacks import PrepareCallback
from xray.components.training import Training
from xray import logger


class TrainingPipeline():
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
        
        # Process Data
        training_config = config.get_training_config()
        training = Training(config=training_config)
        X_train, y_train, X_test, y_test, X_val, y_val = training.process_data()
         
        model = training.build_model()

        # Train and Save the Model
        history = training.train_model(model, X_train, y_train, X_val, y_val)
        
        loss, accuracy = model.evaluate(X_test, y_test)
        print("Loss of the model is -", loss)
        print("Accuracy of the model is -", accuracy * 100, "%")
        
        
STAGE_NAME = "Training Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\n************************")
        
    except Exception as e:
        logger.exception(e)
        raise(e)