import boto3
from botocore.exceptions import ClientError

def check_mfa_status():
    iam = boto3.client('iam')                                               # Initialize the IAM client

    try:
        paginator = iam.get_paginator('list_users')                         # Gets all users in the account using a paginator
        print(f"{'User Name':<30} | {'MFA Enabled':<12}")
        print("-" * 45)

        for page in paginator.paginate():
            for user in page['Users']:
                username = user['UserName']
                
                mfa_devices = iam.list_mfa_devices(UserName=username)       # Checks for MFA devices for this specific user
               
                is_mfa_enabled = len(mfa_devices['MFADevices']) > 0         # If the list is empty then MFA is not enabled
                
                status_text = "YES" if is_mfa_enabled else "NO (!!!)"
                print(f"{username:<30} | {status_text:<12}")

    except ClientError as e:
        print(f"Error connecting to AWS: {e}")

if __name__ == "__main__":
    check_mfa_status()