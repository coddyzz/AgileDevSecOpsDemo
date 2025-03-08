import pytest
import numpy as np
import pandas as pd
from source import ai_fraud_detection_model

sample_data = pd.DataFrame([[2829,1000,100,7123259,50,'2025-02-22T14:26:00Z',N,Low risk,'192.168.1.1','SG','N']])

def return_test():
	assert ai_fraud_detection_model(sample_data)

		
