# Bucket Data
The bucket_data.py script will provide comprehensive data on S3 buckets inside of an AWS account. On the v1.0 intial commit, the script returns Bucket Name, number of objects in bucket, and bucket size (for each bucket). As development progresses, this script will generate a .csv file which outputs additional metadata information like bucket region, owner, etc..

## Prerequisites
* A machine with AWS CLI access configured for access with the account you wish to query.
* Python 3.7 or higher installed.

## Using The Script
For Windows Machines:
* On a machine with AWS CLI access configured, run the command "python bucket_data.py" from the directory where the file is saved.

For Linux Machines:
* On a machine with AWS CLI access configured, run the command "python3 bucket_data.py" from the directory where the file is saved.

## Versioning
v1.0 - commit date 02/10/2020 (initial commit)

## Authors
Stephen Daugherty
LinkedIn Profile: https://www.linkedin.com/in/stephenpdaugherty/

## License
Open Source - use and modify as you please.
