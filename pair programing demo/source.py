import random
from openai import OpenAI
def ai_fraud_detection_model(data):
	'''
	Requirements:
	1. Return an boolean output
	2. Consistent output
	3. Reflect actual resut with accuracry > 0.5
	4. Reflect both precision and recall
	'''

	client = OpenAI()

	completion = client.chat.completions.create(
	    model="gpt-4o",
	    messages=[
	        {"role": "system", "content": "You are a helpful assistant."},
	        {
	            "role": "system",
	            "content": 
	            f"""With the given data of ({data}), 
	            Detect if this entry has a >0.5 probability of fraud.
	            Data Schema is 
	            <start of schema>
	            User ID
	            Historical Ave Spending per Month (SGD) 
	            Historical Ave Per Txn Amt (SGD)
	            Txn ID
	            Txn Amount (SGD)
	            Txn Timestamp	
	            Overseas Payment?	
	            Device Finger Print (DFP) 
	            Label	
	            IP Address	
	            IP Address Country	
	            Browser/ OS Outdated?
	            <end of schema>
	            Return Either 1 or 0

"""
	        }
	    ]
	)

	return completion.choices[0].message