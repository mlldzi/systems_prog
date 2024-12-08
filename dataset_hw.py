import pandas as pd
from matplotlib import pyplot as plt
from sklearn import *
from sklearn import preprocessing
import seaborn as sns
import tensorflow as tf
import torch



class Dataset:
    def __init__(self, path: str):
        self.path = path
        self.df = pd.read_csv(self.path)

    def print_info(self):
        info = {
            'Типы данных': self.df.dtypes,
            'Количество пропущенных значений': self._missing_values()
        }
        return info

    def _missing_values(self):
        return self.df.isnull().sum()

    def fill_missing(self, strategy='mean', value=None):
        for column in self.df.select_dtypes(include=['float64', 'int64']).columns:
            if self.df[column].isnull().sum() > 0:
                if strategy == 'mean':
                    self.df[column].fillna(self.df[column].mean(), inplace=True)
                elif strategy == 'median':
                    self.df[column].fillna(self.df[column].median(), inplace=True)
                elif strategy == 'constant' and value is not None:
                    self.df[column].fillna(value, inplace=True)

    def remove_outliers(self, column_name: str):
        q = self.df[column_name].quantile(q=0.99)
        self.df = self.df[self.df[column_name] <= q]

    def check_categorical(self, threshold_of_num_cat: int = None):
        threshold_of_num_cat = threshold_of_num_cat or self.df.shape[0]  # TODO: подумать как оценить границу

        def is_categorical(column):
            if column.dtype in ('category', 'bool'):
                return True
            elif column.dtype == 'object':
                return len(column.astype(str).unique()) <= threshold_of_num_cat
            elif column.dtype == 'float64':
                return len(column.round(10).unique()) <= threshold_of_num_cat
            # other datatypes: 'int64', 'float64', 'timedelta[ns]'
            return len(column.unique()) <= threshold_of_num_cat

        categorical_names = [column for column in self.df.columns if is_categorical(column)]
        return categorical_names

    def eval_categorical(self, categorical_names, strategy='Onehot') -> None:
        if strategy == 'Onehot':
            encoder = preprocessing.OneHotEncoder()  # TODO: узнать про sparse=False
            for col in categorical_names:
                sub = encoder.fit_transform(self.df[col].to_numpy().reshape(-1, 1))
                df_encoded = pd.DataFrame(sub, columns=encoder.get_feature_names_out([col]))
                self.df = pd.concat([self.df, df_encoded], axis=1)

        elif strategy == 'Label':
            encoder = preprocessing.LabelEncoder()
            for col in categorical_names:
                self.df[col + '_labeled'] = encoder.fit_transform(self.df[col].to_numpy().reshape(-1, 1))

        else:
            raise ValueError("strategy must be 'Onehot' or 'Label'")

    def preparation(self, threshold_of_num_cat: int = None, strategy='Onehot') -> None:
        self.fill_missing(strategy='mean')
        categorical = self.check_categorical(threshold_of_num_cat=threshold_of_num_cat)
        self.eval_categorical(categorical, strategy)

    def display(self, plot_type='Hist', column=None):
        if column:
            self._display_column_plot(plot_type, column)
        else:
            self._display_all_columns_plot(plot_type)
        plt.show()

    def _display_column_plot(self, plot_type, column):
        if plot_type == 'Hist':
            self.df[column].plot(kind='hist', title=f'Histogram of {column}')
        elif plot_type == 'Box':
            sns.boxplot(x=self.df[column])
            plt.title(f'Boxplot of {column}')
        else:
            raise ValueError

    def _display_all_columns_plot(self, plot_type):
        if plot_type == 'Hist':
            self.df.hist(figsize=(10, 8))
        elif plot_type == 'Box':
            sns.boxplot(data=self.df.select_dtypes(include=['float64', 'int64']))
            plt.title('Boxplot for all numeric columns')
        else:
            raise ValueError

    def transform_to_tensor(self, framework='tensorflow'):
        if framework == 'tensorflow':
            return tf.convert_to_tensor(self.df.values)
        elif framework == 'pytorch':
            return torch.tensor(self.df.values)
        elif framework == 'numpy':
            return self.df.values

        raise ValueError("framework must be 'tensorflow', 'pytorch', or 'numpy'")

