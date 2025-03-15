import pytest
import numpy as np
import pandas as pd
from source import ai_fraud_detection_model
from sklearn.metrics import accuracy_score,f1_score

sample_data = pd.read_csv('test_data.csv')
sample_test = sample_data.drop('fraud')
sample_result = sample_data['fraud']

def return_test():
	assert ai_fraud_detection_model(sample_data)

def consistent_test():
	result = sample_data.apply(lambda x: ai_fraud_detection_model(x), axis=1)
	result2 = sample_data.apply(lambda x: ai_fraud_detection_model(x), axis=1)
	assert result.equals(result2)

def accuracy_test():
	y_true = sample_result
	y_pred = sample_data.apply(lambda x: ai_fraud_detection_model(x), axis=1)
	assert accuracy_score(y_true, y_pred) > 0.5

def f1_test():
	y_true = sample_result
	y_pred = sample_test.apply(lambda x: ai_fraud_detection_model(x), axis=1)
	assert f1_score(y_true, y_pred) > 0.9	