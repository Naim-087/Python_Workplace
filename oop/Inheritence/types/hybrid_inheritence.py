class DataScienceProject:

    def __init__(self, project_name):
        self.project_name = project_name

    def show_project(self):
        print(f"Project: {self.project_name}")


class DataLoader(DataScienceProject):

    def load_data(self):
        print("Loading dataset...")

    def clean_data(self):
        print("Cleaning dataset...")


class ModelTrainer(DataScienceProject):

    def train_model(self):
        print("Training model...")

    def evaluate_model(self):
        print("Evaluating model...")


class MLPipeline(DataLoader, ModelTrainer):

    def deploy_model(self):
        print("Deploying model...")


pipeline = MLPipeline("Customer Churn Prediction")

pipeline.show_project()
pipeline.load_data()
pipeline.clean_data()
pipeline.train_model()
pipeline.evaluate_model()
pipeline.deploy_model()