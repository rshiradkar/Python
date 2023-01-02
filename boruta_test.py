import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from boruta import BorutaPy

# load X and y
# NOTE BorutaPy accepts numpy arrays only, hence the .values attribute
X, y = make_classification(n_samples=1000, n_features=15,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)

y = y.ravel()

# define random forest classifier, with utilising all cores and
# sampling in proportion to y labels
rf = RandomForestClassifier(n_jobs=-1, class_weight='balanced', max_depth=5)

# define Boruta feature selection method
feat_selector = BorutaPy(rf, n_estimators='auto', random_state=1)

# find all relevant features - 5 features should be selected
feat_selector.fit(X, y)

# check selected features - first 5 features are selected
temp = feat_selector.support_

X_select = X[:,temp]

select = np.argwhere(temp== True)

# check ranking of features
ranks = feat_selector.ranking_

print(select.size)



# call transform() on X to filter it down to selected features
X_filtered = feat_selector.transform(X)
# print(X_filtered)