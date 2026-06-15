class DataLoader:
    def __init__(self, dataset_name, **kwargs):
        super().__init__(**kwargs)
        self.dataset_name = dataset_name

    def load_data(self):
        print(f"Loading {self.dataset_name} dataset...")

    def show_dataset(self):
        print(f"Dataset: {self.dataset_name}")


class ModelTrainer:
    def __init__(self, model_name, **kwargs):
        super().__init__(**kwargs)
        self.model_name = model_name

    def train_model(self):
        print(f"Training {self.model_name} model...")

    def evaluate_model(self):
        print(f"Evaluating {self.model_name} model...")


class MLProject(DataLoader, ModelTrainer):
    def __init__(self, dataset_name, model_name, project_name):
        super().__init__(
            dataset_name=dataset_name,
            model_name=model_name
        )
        self.project_name = project_name

    def project_details(self):
        print(f"Project Name: {self.project_name}")
        print(f"Dataset: {self.dataset_name}")
        print(f"Model: {self.model_name}")


project = MLProject(
    "Titanic",
    "Random Forest",
    "Passenger Survival Prediction"
)

project.project_details()
project.load_data()
project.show_dataset()
project.train_model()
project.evaluate_model()