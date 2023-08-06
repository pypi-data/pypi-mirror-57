def run_regressors(df, target_column):
    '''
    df: Data (dataFrame)
    target_column: Target variable/column name (str)

    1. All regression models are ranked by RMSE (Root Mean Squared Error)
    2. Categorical variables are dummy encoded for regression models except for Catboost and LightGBM.

    '''

    import warnings
    warnings.filterwarnings("ignore")

    from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.svm import SVR
    from xgboost import XGBRegressor
    from lightgbm import LGBMRegressor
    from catboost import CatBoostRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from lightgbm import LGBMRegressor
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error
    import numpy as np

    models = [DecisionTreeRegressor(), KNeighborsRegressor(), SVR(gamma='auto'), RandomForestRegressor(n_estimators=100), AdaBoostRegressor(), GradientBoostingRegressor(), XGBRegressor(objective='reg:squarederror')]

    df = df.dropna()

    #cat_cols = df.select_dtypes(include='object').columns
    #num_cols = df.select_dtypes(exclude='object').columns

    # Decison Trees, Random Forest, SVM, KNN, Gradient Boosting, XGBoost
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    X_dummy = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X_dummy, y, test_size=0.3, random_state=42)

    result={}
    for model in models:
        model.fit(X_train, y_train)
        rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test))).astype(int)
        result[model.__class__.__name__]=rmse

    # Catboost:
    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y, test_size=0.3, random_state=42)
    cat_cols = X.select_dtypes(include='object').columns
    cat_indices = [X.columns.get_loc(col) for col in cat_cols]
    cb = CatBoostRegressor(cat_features=cat_indices)
    cb.fit(X_train_c,y_train_c, eval_set=(X_test_c, y_test_c),early_stopping_rounds=10, use_best_model=True, verbose=0 )
    result[cb.__class__.__name__] = np.sqrt(mean_squared_error(y_test_c, cb.predict(X_test_c))).astype(int)

    # Light GBM:
    lb = LabelEncoder()
    for col in cat_cols:
        X[col] = lb.fit_transform(X[col])

    lgb = LGBMRegressor()

    X_train_l, X_test_l, y_train_l, y_test_l = train_test_split(X, y, test_size=0.3, random_state=42)
    lgb.fit(X_train_l, y_train_l, categorical_feature=cat_cols.tolist())
    result[lgb.__class__.__name__] = np.sqrt(mean_squared_error(y_test_l, lgb.predict(X_test_l))).astype(int)

    b = pd.DataFrame.from_dict(result,orient='index').reset_index().rename(columns={'index':'Model',0:'RMSE'}).sort_values(by='RMSE', ascending=False)

    fig, ax = plt.subplots(figsize=(10,6))
    ax.barh(b.Model, b.RMSE, color='red')
    plt.title("Baseline Model Performance")
    for i, v in enumerate(b.RMSE):
        ax.text(v/2, i, 'RMSE='+str(v), color='white', va='center', fontweight='bold')

    return fig


def run_classifiers(df, target_column):
    '''
    df: Data (dataFrame)
    target_column: Target variable/column name

    1. All classification models are ranked by AUC
    2. Categorical variables are dummy encoded for classification models except for Catboost and LightGBM.
    '''
    import warnings
    warnings.filterwarnings("ignore")
    
    from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    from xgboost import XGBClassifier
    from lightgbm import LGBMClassifier
    from catboost import CatBoostClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.metrics import roc_auc_score
    import numpy as np

    models = [DecisionTreeClassifier(), KNeighborsClassifier(), SVC(gamma='auto', probability=True), RandomForestClassifier(n_estimators=100), AdaBoostClassifier(), GradientBoostingClassifier(), XGBClassifier()]

    df = df.dropna()

    #cat_cols = df.select_dtypes(include='object').columns
    #num_cols = df.select_dtypes(exclude='object').columns

    # Decison Trees, Random Forest, SVM, KNN, Gradient Boosting, XGBoost
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    X_dummy = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X_dummy, y, test_size=0.3, random_state=42)

    result={}
    for model in models:
        model.fit(X_train, y_train)
        auc = np.round(roc_auc_score(y_test, model.predict_proba(X_test)[:,1]),2)
        result[model.__class__.__name__]=auc

    # Catboost:
    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y, test_size=0.3, random_state=42)
    cat_cols = X.select_dtypes(include='object').columns
    cat_indices = [X.columns.get_loc(col) for col in cat_cols]
    cb = CatBoostClassifier(cat_features=cat_indices)
    cb.fit(X_train_c,y_train_c, eval_set=(X_test_c, y_test_c),early_stopping_rounds=10, use_best_model=True, verbose=0 )
    result[cb.__class__.__name__] = np.round(roc_auc_score(y_test_c, cb.predict_proba(X_test_c)[:,1]),2)

    # Light GBM:
    lb = LabelEncoder()
    for col in cat_cols:
        X[col] = lb.fit_transform(X[col])

    lgb = LGBMClassifier()

    X_train_l, X_test_l, y_train_l, y_test_l = train_test_split(X, y, test_size=0.3, random_state=42)
    lgb.fit(X_train_l, y_train_l, categorical_feature=cat_cols.tolist())
    result[lgb.__class__.__name__] = np.round(roc_auc_score(y_test_l, lgb.predict_proba(X_test_l)[:,1]),2)

    b = pd.DataFrame.from_dict(result,orient='index').reset_index().rename(columns={'index':'Model',0:'AUC'}).sort_values(by='AUC', ascending=True)

    fig, ax = plt.subplots(figsize=(10,6))
    ax.barh(b.Model, b.AUC)
    plt.title("Model Baseline Performance")

    for i, v in enumerate(b.AUC):
        ax.text(v/2, i, 'AUC='+str(v), color='white', va='center', fontweight='bold')

    return fig
