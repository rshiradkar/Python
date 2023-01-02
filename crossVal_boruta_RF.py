import numpy as np
import pandas as pd
import math
import collections
import statistics
from sklearn.datasets import make_classification
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from boruta import BorutaPy


def cvClassify(feats,label):
    n_runs = 3
    k = 3

    auc_cv = []
    feats_cv = []

    for r in range(n_runs):

        kf = KFold(n_splits=k, shuffle=True)

        for train, test in kf.split(feats):
            feats_train = feats.iloc[train, :]
            label_train = label.iloc[train]

            feats_test = feats.iloc[test, :]
            label_test = label.iloc[test]

            rf = RandomForestClassifier(n_jobs=-1, class_weight='balanced', max_depth=5)
            feat_selector = BorutaPy(rf, n_estimators='auto', verbose=2, random_state=1)

            feat_selector.fit(feats_train, label_train)

            feats_train_ = feat_selector.transform(feats_train)
            select_feats = feat_selector.support_
            select_feats = np.argwhere(select_feats == True)
            feats_cv.extend(select_feats)

            feats_train = feats_train.iloc[:,select_feats]
            feats_test = feats_test.iloc[:,select_feats]

            feats_train_ = feats_train.to_numpy()
            label_train_ = label_train.to_numpy()

            feats_test_ = feats_test.to_numpy()
            label_test_ = label_test.to_numpy()

            model = rf.fit(gamma='auto', probability=True)
            model.fit(feats_train,label_train)

            probs_test = model.predict_proba(feats_test_)
            fpr, tpr, thresholds = metrics.roc_curve(label_test_, probs_test[:,1], pos_label=1)
            auc_cv.append(metrics.auc(fpr,tpr))


    counter = collections.Counter(feats_cv)
    top_feats_sorted = np.array(counter.most_common(5))
    top_feats = top_feats_sorted[:,0]

    final_feats = feats.iloc[:, top_feats]
    final_feats = final_feats.to_numpy()
    label = label.to_numpy()

    final_model = SVC(gamma='auto', probability=True)
    final_model.fit(final_feats,label)

    return statistics.mean(auc_cv), final_model, top_feats


if __name__ == "__main__":
    
    # I generate some dummy data here feats and label. feats1 is for cross validation, feats 2 is hold out test.
    
    feats, label = make_classification(n_samples = 100, n_features = 20, n_informative = 5, n_redundant = 15)
    feats = pd.DataFrame(feats)
    label = pd.Series(label)

    feats1 = feats.iloc[:90, :]
    label1 = label.iloc[:90]



    cvAUC, cvModel, topFeats = cvClassify(feats1,label1)
    print("cross validation AUC is "+ str(cvAUC))

    feats2 = feats.iloc[90:,topFeats]
    label2 = label.iloc[90:]

    feats2 = feats2.to_numpy()
    label2 = label2.to_numpy()
    probs_ = cvModel.predict_proba(feats2)

    fpr, tpr, thresholds = metrics.roc_curve(label2, probs_[:,1], pos_label=1)
    testAUC = metrics.auc(fpr,tpr)
    print("test AUC is "+ str(testAUC))
