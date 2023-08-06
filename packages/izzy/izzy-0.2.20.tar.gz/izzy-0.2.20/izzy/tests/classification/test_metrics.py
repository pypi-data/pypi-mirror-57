"""
test_metrics.py
===============
written in Python3

author: C. Lockhart <chris@lockhartlab.org>
"""

from izzy.classification.metrics import *

from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import sklearn.metrics as sk_m
import unittest


#
classes = st.integers(min_value=2, max_value=10)
samples = st.integers(min_value=100, max_value=100000)


# Test metrics
class TestMetrics(unittest.TestCase):
    @given(classes, samples)
    def test_accuracy(self, n_classes, n_samples):
        # Generate data
        y_true, y_pred = _generate_data(n_classes, n_samples)

        # Compute accuracy simply
        fn, fp, tn, tp = _get_fn_fp_tn_tn(y_true, y_pred, n_classes)
        acc1 = (tp + tn) / (tp + tn + fp + fn)

        # Compute accuracy using izzy function
        acc2 = list(accuracy(y_true, y_pred).values())

        # Assert equal
        np.testing.assert_equal(acc1, acc2)

    # Tests that we know how to compute AIC
    @given(st.floats(allow_nan=False),
           st.integers())
    def test_aic(self, log_likelihood, degrees_of_freedom):
        # We can compute this here and from the function
        value1 = -2 * log_likelihood + 2 * degrees_of_freedom
        value2 = aic(log_likelihood, degrees_of_freedom)

        # These must be equal
        self.assertEqual(value1, value2)

    # Tests that we know how to compute BIC
    @given(st.floats(allow_nan=False),
           st.integers(),
           st.integers(min_value=1, max_value=1000000))
    def test_bic(self, log_likelihood, degrees_of_freedom, num_samples):
        # We can compute this here and from the function
        value1 = -2 * log_likelihood + np.log(num_samples) * degrees_of_freedom
        value2 = bic(log_likelihood, degrees_of_freedom, num_samples)

        # These must be equal
        self.assertEqual(value1, value2)

    @given(classes, samples)
    def test_false_negatives(self, n_classes, n_samples):
        # Generate data
        y_true, y_pred = _generate_data(n_classes, n_samples)

        # Compute false negatives
        fn1 = np.zeros(n_classes)
        for k in range(n_classes):
            fn1[k] = np.sum((y_true == k) & (y_pred != k))
        fn2 = list(false_negatives(y_true, y_pred).values())

        # Assert equal
        np.testing.assert_equal(fn1, fn2)

    @given(classes, samples)
    def test_false_positives(self, n_classes, n_samples):
        # Generate data
        y_true, y_pred = _generate_data(n_classes, n_samples)

        # Compute false positives
        fp1 = np.zeros(n_classes)
        for k in range(n_classes):
            fp1[k] = np.sum((y_true != k) & (y_pred == k))
        fp2 = list(false_positives(y_true, y_pred).values())

        # Assert equal
        np.testing.assert_equal(fp1, fp2)

    @given(samples)
    def test_roc_random(self, n_samples):
        # Generate data
        y_true = np.random.randint(low=0, high=2, size=n_samples)
        y_prob = np.random.rand(n_samples)

        # Get ROC data
        fpr0, tpr0, _ = sk_m.roc_curve(y_true, y_prob)
        fpr1, tpr1 = roc(y_true, y_prob)

        # Put together into DataFrames and merge
        df0 = pd.DataFrame({'fpr0': fpr0, 'tpr0': tpr0}).pivot_table(index='fpr0', values='tpr0', aggfunc='max')
        df1 = pd.DataFrame({'fpr1': fpr1, 'tpr1': tpr1}).pivot_table(index='fpr1', values='tpr1', aggfunc='max')
        df = df0.merge(df1, how='inner', left_index=True, right_index=True)

        # Assert equal
        np.testing.assert_almost_equal(df['tpr0'].values, df['tpr1'].values)

    @given(samples)
    def test_roc_auc_random(self, n_samples):
        # Generate data
        y_true = np.random.randint(low=0, high=2, size=n_samples)
        y_prob = np.random.rand(n_samples)

        # We can also test the AUC as a separate test
        auc0 = sk_m.roc_auc_score(y_true, y_prob)
        auc1 = roc_auc(y_true, y_prob)

        # Assert equal
        self.assertAlmostEqual(auc0, auc1)

    @given(classes, samples)
    def test_true_positives(self, n_classes, n_samples):
        # Generate data
        y_true, y_pred = _generate_data(n_classes, n_samples)

        # Compute true positives
        tp1 = np.zeros(n_classes)
        for i in range(n_classes):
            tp1[i] = np.sum((y_true == y_pred) & (y_true == i))
        tp2 = list(true_positives(y_true, y_pred).values())

        # Assert equal
        np.testing.assert_equal(tp1, tp2)

    @given(classes, samples)
    def test_true_negatives(self, n_classes, n_samples):
        # Generate data
        y_true, y_pred = _generate_data(n_classes, n_samples)

        # Compute true negatives
        tn1 = np.zeros(n_classes)
        for i in range(n_classes):
            tn1[i] = np.sum((y_true == y_pred) & (y_true != i))
        tn2 = list(true_negatives(y_true, y_pred).values())

        # Assert equal
        np.testing.assert_equal(tn1, tn2)


# Helper function to generate data for tests
def _generate_data(n_classes, n_samples):
    # Generate y_true; must contain every class
    while True:
        y_true = np.random.randint(low=0, high=n_classes, size=n_samples)
        if np.min(np.in1d(np.arange(n_classes), y_true)):
            break

    # Generate y_pred
    y_pred = np.random.randint(low=0, high=n_classes, size=n_samples)

    # Return
    return y_true, y_pred


# Helper function to compute FN, FP, TN, TP
def _get_fn_fp_tn_tn(y_true, y_pred, n_classes):
    # Zero out arrays to store results
    fp = np.zeros(n_classes)
    fn = np.zeros(n_classes)
    tp = np.zeros(n_classes)
    tn = np.zeros(n_classes)

    # Loop over all classes and compute
    for k in range(n_classes):
        # For 3 classes, if we're predicting the first class we would see
        # TP FN FN    TN FP TN    TN TN FP
        # FP TN TN    FN TP FN    TN TN FP
        # FP TN TN    TN FP TN    FN FN TP
        # The bottom squares are all TN because in a one-vs-rest scheme, these are true negatives
        # TODO implement accuracy in a true multiclass scheme
        fn[k] = np.sum((y_true == k) & (y_pred != k))
        fp[k] = np.sum((y_true != k) & (y_pred == k))
        tp[k] = np.sum((y_true == y_pred) & (y_true == k))
        tn[k] = np.sum((y_true == y_pred) & (y_true != k))

    # Return
    return fn, fp, tn, tp
