import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

class NycCrimeCategoryRandomForestModel:
    def __init__(self,
                 random_state=42,
                 test_size=0.2,
                 n_estimators=200,
                 max_depth=20,
                 drop_columns=None,
                 target_column='Crime_Category',
                 model_filename='nyc_crime_category_random_forest_model.pkl',
                 verbose_level=1):
        """
        Initialize the NycCrimeCategoryModel with configurable parameters.

        Args:
            random_state (int): Random state for reproducibility.
            test_size (float): Proportion of the dataset to include in the test split.
            n_estimators (int): Number of trees in the RandomForest.
            max_depth (int): Maximum depth of the trees in the RandomForest.
            drop_columns (list): Columns to drop from the dataset.
            target_column (str): The name of the target column.
            model_filename (str): Default filename for saving and loading the model.
            verbose_level (int): Controls the verbosity of the RandomForestClassifier.
        """
        self.random_state = random_state
        self.test_size = test_size
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.drop_columns = drop_columns if drop_columns is not None else ['OFNS_DESC', 'OFNS_DESC_Severity_Score']
        self.target_column = target_column
        self.model_filename = model_filename
        self.verbose_level = verbose_level

        self.pipeline = None
        self.preprocessor = None
        self.label_encoder = None
        self.X_train = None
        self.y_train = None

    def load_data(self, file_path):
        """Load and preprocess the data."""
        self.df = pd.read_csv(file_path)
        self.df = self.df.drop(columns=self.drop_columns)

    def preprocess_data(self):
        """Identify categorical and numerical columns and apply preprocessing."""
        # Identify categorical and numerical columns
        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        categorical_cols.remove(self.target_column)
        numerical_cols = self.df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        # Label encode the target
        self.label_encoder = LabelEncoder()
        self.df[self.target_column] = self.label_encoder.fit_transform(self.df[self.target_column])

        # Separate features and target
        self.X = self.df.drop(self.target_column, axis=1)
        self.y = self.df[self.target_column]

        # Create the preprocessing pipelines
        numerical_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, numerical_cols),
                ('cat', categorical_transformer, categorical_cols)
            ]
        )

    def split_data(self):
        """Split the data into training and testing sets."""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=self.test_size, random_state=self.random_state)

    def train_model(self):
        """Train the RandomForest model."""
        self.pipeline = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('classifier', RandomForestClassifier(n_estimators=self.n_estimators, max_depth=self.max_depth, random_state=self.random_state, verbose=self.verbose_level))
        ])

        self.pipeline.fit(self.X_train, self.y_train)

        y_pred = self.pipeline.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        print(f"Model accuracy: {accuracy:.4f}")
        return accuracy

    def save_model(self, model_filename=None):
        """Save the trained model to a file."""
        if self.pipeline is not None:
            if model_filename is None:
                model_filename = self.model_filename
            joblib.dump(self.pipeline, model_filename)
            print(f"Model saved to {model_filename}")
        else:
            print("No model trained yet. Please train the model before saving.")

    def load_model(self, model_filename=None):
        """Load a model from a file."""
        if model_filename is None:
            model_filename = self.model_filename
        self.pipeline = joblib.load(model_filename)
        print(f"Model loaded from {model_filename}")

    def predict(self, X):
        """Make predictions with the trained model."""
        if self.pipeline is not None:
            return self.pipeline.predict(X)
        else:
            print("No model loaded or trained. Please train or load a model first.")
            return None

    def print_class_distribution(self):
        """Print the class distribution in the training data."""
        if self.y_train is not None:
            class_distribution = pd.Series(self.y_train).value_counts(normalize=True) * 100
            print("Class distribution in training data (percentage):")
            print(class_distribution)
        else:
            print("Training data not found. Please run the split_data() method first.")
