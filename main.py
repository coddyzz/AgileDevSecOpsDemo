import argparse
from utils import threat_identification,threat_classification,threat_notifications

def bandguardAI(method, data,target_email):
	'''
	call various function by given method
	all -> None Output
	identification -> Boolean
	classification -> Tuple (String, Int)
	'''

    if method == 'all':
        is_threat = threat_identification(data)
        threat_cate, threat_level = threat_classification(data,is_threat)
        threat_notifications(data,is_threat,threat_cate,threat_level,target_email)

    elif method == 'identification':
        return threat_identification(data)

    elif method == 'classification':
        return threat_classification(data,is_threat)

    else:
        raise "no such method"


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

    # call main function
    bandguardAI(args.method, args.data,args.target_email)