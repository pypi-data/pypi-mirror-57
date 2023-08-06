import requests

def get_branch_details(ifsc):
    API = f'https://ifsc.razorpay.com/{ifsc}'
    result = {}
    result['IFSC'] = ifsc
    try:
        r = requests.get(API)
        if r.status_code == 404:
            result['STATUS'] = 404
            return result
        
        result['STATUS'] = r.status_code
        result['BANK'] = r.json()['BANK']
        result['BRANCH'] = r.json()['BRANCH']
        result['ADDRESS'] = r.json()['ADDRESS'] + ', ' + r.json()['STATE']
    except requests.ConnectionError:
        result['STATUS'] = 503
    return result

def print_branch_details(data):
    print("IFSC:", data['IFSC'], end='\n\n')
    if(data['STATUS'] == 503):
        print('Please check your internet connection')
    elif(data['STATUS'] == 404):
        print("bank details not found, invalid IFSC")
    else:
        print("Bank name:", data['BANK'])
        print("Branch name:", data['BRANCH'])
        print("Branch address:", data['ADDRESS'])
    
