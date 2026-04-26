import boto3
from botocore.exceptions import ClientError

def fix_public_buckets():
    # 1. Connect to the S3 Service
    s3 = boto3.client('s3')
    
    try:
        # 2. Ask AWS for all your buckets
        response = s3.list_buckets()
        
        print(f"Checking {len(response['Buckets'])} buckets...\n")

        for bucket in response['Buckets']:
            name = bucket['Name']
            print(f"Inspecting bucket: {name}")

            # 3. Apply the 'Block Public Access' settings
            # This is the "Self-Healing" part.
            try:
                s3.put_public_access_block(
                    Bucket=name,
                    PublicAccessBlockConfiguration={
                        'BlockPublicAcls': True,
                        'IgnorePublicAcls': True,
                        'BlockPublicPolicy': True,
                        'RestrictPublicBuckets': True
                    }
                )
                print(f"--- ✅ SUCCESS: {name} is now locked and PRIVATE.")
            
            except ClientError as e:
                print(f"--- ❌ ERROR: Could not secure {name}. {e}")

    except ClientError as e:
        print(f"Critical connection error: {e}")

if __name__ == "__main__":
    fix_public_buckets()