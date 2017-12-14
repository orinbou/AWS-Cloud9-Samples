###############################
# boto3 demo
# AWS SDK for Python (Boto3)
###############################
import boto3

# list
def listBuckets():
    s3client = boto3.client('s3')
    resource = s3client.list_buckets()
    for bucket in resource['Buckets']:
        print("Bucket: %s" % bucket['Name'])

# create
def createBucket(bucketName):
    s3client = boto3.client('s3')
    s3client.create_bucket(Bucket=bucketName)
    print("create Bucket: %s" % bucketName)

# delete
def deleteBucket(bucketName):
    s3client = boto3.client('s3')
    s3client.delete_bucket(Bucket=bucketName)
    print("delete Bucket: %s" % bucketName)

##################
# demo
##################
print("[DEMO START]")

# list
createBucket('btc-arch-cloud9-demo')
# create
listBuckets()
# delete
deleteBucket('btc-arch-cloud9-demo')

print("[DEMO END]")
