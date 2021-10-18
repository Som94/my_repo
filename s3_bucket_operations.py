import boto3
import pandas as pd

s3_resource = boto3.resource('s3')


# Create a Bucket

s3_resource.create_bucket(Bucket='s-aroha')

# Display all buckets in s3
print("Buckets are :")
for bucket in s3_resource.buckets.all():
    print(bucket)
    
    

# Display all objects contain by buckets

print("objects are contain by the buckets :")
for bucket in s3_resource.buckets.all():
    for obj in bucket.objects.all():
        print(obj)
        
        
# How to upload a file into s3 bucket ?

s3_resource.meta.client.upload_file('abc.csv','s-aroha','abc.csv')

# How to access a file from s3 bucket

    # Create s3 bucket client
s3_client=boto3.client('s3')

file = s3_client.get_object(Bucket='s-aroha', Key='abc.csv')

# Read that file
  
file_data=pd.read_csv(file['Body'])

# How to delete a file/object from a s3 bucket

s3_resource.meta.client.delete_object(Bucket='s-aroha', Key='abc.csv')

# How to delete a bucket

# We can delect a bucket,If bucket not empty.


    # To delete a empty bucket
    
bucket=s3_resource.Bucket('s-aroha')

bucket.delete()


    # To delete a non empty bucket, first we have to make that bucket empty
    
bucket=s3_resource.Bucket('s-aroha')

for obj in bucket.objects.all():
    obj.delete()

bucket.delete()   


