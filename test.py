# def check_categorical(self, threshold_of_num_cat: int = None):
#     if threshold_of_num_cat is None:
#         threshold_of_num_cat = self.df.shape[0]  # TODO: подумать как оценить границу
#
#     categorical_names = []
#
#     for i in self.df.columns:
#         if self.df[i].dtype in ('category', 'bool'):
#             categorical_names.append(i)
#         elif self.df[i].dtype == 'object':
#             if len(self.df[i].astype(str).unique()) <= threshold_of_num_cat:
#                 categorical_names.append(i)
#         elif self.df[i].dtype == 'float64':
#             if len(self.df[i].round(10).unique()) <= threshold_of_num_cat:
#                 categorical_names.append(i)
#         elif len(self.df[i].unique()) <= threshold_of_num_cat: # other datatypes: 'int64', 'float64', 'timedelta[ns]', 'datetime64'
#             categorical_names.append(i)
#
#     return categorical_names


#path_to_ds = r'..\Sleep_health_and_lifestyle_dataset.csv'
#
# dataset = Dataset(path_to_ds)
#
# print(dataset.print_info())
#
# dataset.display("Box", "Age")
# dataset.display("Box")
# dataset.display()