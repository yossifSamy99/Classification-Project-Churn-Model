

import pandas as pd


def predict_new(preprocessor,data,model):
    df=pd.DataFrame([data.model_dump()])
    
    x_procceced=preprocessor.transform(df)

    y_pred=model.predict(x_procceced)
    y_prob=model.predict_proba(x_procceced)
    return {
        "probability" : y_prob.tolist(),
        "prediction" :  bool(y_pred[0])
    }