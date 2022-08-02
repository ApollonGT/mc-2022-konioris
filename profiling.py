import cProfile
import pstats
import io
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt
from plotting_tools import df
from models_selection import models
from model_deployment import best_model

# In this step we apply profiling in our most time-consuming functions

def models(df):

    X_train, X_test, y_train, y_test = train_test_split(df.drop('rating', axis = 1), df['rating'], test_size = 0.2)
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
        
    results = {}
    models = [LinearRegression(),
                Ridge(),
                DecisionTreeRegressor(),
                RandomForestRegressor()]
    for model in models:
        fit = model.fit(X_train, y_train)
        y_pred = fit.predict(X_test)
        results[fit.__class__.__name__] = [
            round(fit.score(X_test, y_test), 2),
            round(mean_absolute_error(y_test, y_pred), 2),
            round(mean_squared_error(y_test, y_pred), 2),
            round(sqrt(mean_squared_error(y_test, y_pred)), 2)]
    index = ['Accuracy', 'Mean Absolute Error', 'Mean Squared Error', 'Root Mean Squared Error']
    results_df = pd.DataFrame(data = results, index = index, columns = list(results.keys()))
    return results_df

def best_model(df):

    iso = df[['rating_count', 'app_name', 'size', 'rating']]
    X_train, X_test, y_train, y_test = train_test_split(iso.drop('rating', axis = 1), iso['rating'], test_size = 0.2)
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
        
    best_model = RandomForestRegressor()
    results = {}
    fit = best_model.fit(X_train, y_train)
    y_pred = fit.predict(X_test)
    results[fit.__class__.__name__] = [
        round(fit.score(X_test, y_test), 2),
        round(mean_absolute_error(y_test, y_pred), 2),
        round(mean_squared_error(y_test, y_pred), 2),
        round(sqrt(mean_squared_error(y_test, y_pred)), 2)]
    index = ['Accuracy', 'Mean Absolute Error', 'Mean Squared Error', 'Root Mean Squared Error']
    outcome = pd.DataFrame(data = results, index = index, columns = list(results.keys()))
    return outcome

pr_models = cProfile.Profile()
pr_models.enable()
my_result_models = models(df)
pr_models.disable()
s_models = io.StringIO()
ps_models = pstats.Stats(pr_models, stream = s_models).sort_stats('tottime')
ps_models.print_stats()
with open('profile_models.txt', 'w+') as f:
    f.write(s_models.getvalue())

pr_best_model = cProfile.Profile()
pr_best_model.enable()
my_result_best_model = best_model(df)
pr_best_model.disable()
s_best_model = io.StringIO()
ps_best_model = pstats.Stats(pr_best_model, stream = s_best_model).sort_stats('tottime')
ps_best_model.print_stats()
with open('profile_best_model.txt', 'w+') as f:
    f.write(s_best_model.getvalue())