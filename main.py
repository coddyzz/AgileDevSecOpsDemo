import argparse
from utils import *

def bandguardAI(method, data,target_email):

	if method == 'all':
		is_threat = threat_identification(data)
		threat_cate, threat_level = threat_classification(data,is_threat)
		return threat_notifications(data,is_threat,threat_cate,threat_level,target_email)


	if method == 'identification':
		return threat_identification(data)

	if method == 'classification':
		return threat_classification(data,is_threat)

	return raise "no such method"


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
                    prog='BankGuard AI CLI',
                    epilog='This is an app for BankGuard AI')
	parser.add_argument('-m','--method')           # positional argument
	parser.add_argument('-d', '--data')    
	parser.add_argument('-e', '--target_email')    

	args = parser.parse_args()

	# data = json.loads(args.data)
	data = args.data
	print(data)

	bandguardAI(args.method, args.data,args.target_email)