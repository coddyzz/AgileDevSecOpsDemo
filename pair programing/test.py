import pytest
import numpy as np
import pandas as pd
from source import ai_fraud_detection_model

sample_data = pd.read_csv('test_data.csv')

def return_test():
	assert ai_fraud_detection_model(sample_data)

def consistent_test():
	result = sample_data.apply(lambda x: ai_fraud_detection_model(x), axis=1)
	result2 = sample_data.apply(lambda x: ai_fraud_detection_model(x), axis=1)
	assert result.equals(result2)