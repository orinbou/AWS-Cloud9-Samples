# AWS-Cloud9-Samples

## AWS Cloud9 DEMO

### AWS SDK for Python (Boto3)
https://aws.amazon.com/jp/sdk-for-python/

### How to instal Boto3
$ sudo pip install boto  
$ sudo pip install boto3  

### How to execute demo
$ git clone https://github.com/orinbou/AWS-Cloud9-Samples.git

demoS3Bucket.py を[Run]して実行してください。  

### Note
* コメントに日本語（マルチバイト文字）を書くとエラーになるみたい。
* ソースコードの【boto3.client('s3')】を'S3'って書くとエラーになる。（※地味にハマりました）

### 参考URL
* https://www.slideshare.net/AmazonWebServicesJapan/aws-black-belt-online-seminar-aws-84039142  
  ※ [@afukui](https://twitter.com/afukui) さんどうもありがとうございます。  
* https://qiita.com/akinoriikeda/items/82bd91fa0d5eb9f974a7
* https://pages.awscloud.com/DeveloperMeetup20171207.html
