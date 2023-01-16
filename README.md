# twitter-airflowproject

## Prerequisites
To keep it simple, we have
* An EC2 instance running Airflow.
* The necessary credentials (Access keys and Consumer keys) to access the Twitter API and for that we need to create an app in the [developer portal](https://developer.twitter.com/en/portal/dashboard)
* The necessary credentials (AWS access and secret key) to access the S3 bucket.

#### Creating a project App

![](https://github.com/nadinelabidi/Ehealth-Kafka-Project/blob/main/Kafka_file/gateway.py)

#### Creating an EC2 instance running on Ubuntu
Here are the steps to create an EC2 instance running Ubuntu on the AWS platform:
1. Sign in to the AWS Management Console.
2. Go to EC2
3. Choose "Launch Instance" to start creating a new instance.
4. Name you instance
6. In the "Application an OS Images" section, select the Ubuntu Server image you want to use.
7. Choose the instance Type that suits you. For the free tier, we can use a "t2.micro" instance.
8. Generate an Key-pair and save it to your local folder (were your project's files exist)
9. create a new security group attached to the instance that allows SSH trafic from anywhere, allows HTTP and HTTPS traffic from the internet.
10. Finally, launch the instance

![](https://github.com/nadinelabidi/Ehealth-Kafka-Project/blob/main/Kafka_file/gateway.py)

####  connect the EC2 instance running Ubuntu to Airflow
Here are the steps to  connect an EC2 instance running Ubuntu to Airflow
1. Log in to your EC2 instance using SSH link
2. Install all the necessary dependencies for the project to run
```
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas 
sudo pip install s3fs
sudo pip install tweepy
``` 
3. Verify that airflow is installed 
```
airflow
``` 
![](https://github.com/nadinelabidi/Ehealth-Kafka-Project/blob/main/Kafka_file/gateway.py)
4. Run the airflow surver
```
airflow standalone
```
5. Use the public IPv4 DNS to open airflow interface
![](https://github.com/nadinelabidi/Ehealth-Kafka-Project/blob/main/Kafka_file/gateway.py)


####  Create the s3 bucket where we will store the tweets
Here are the general steps to create an S3 bucket on the AWS platform:
1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/)
2. Choose "Create Bucket" to start creating a new bucket.
3. In the "Create a Bucket" page, enter a unique and DNS-compliant bucket name and configure your s3 bucket
![](https://github.com/nadinelabidi/Ehealth-Kafka-Project/blob/main/Kafka_file/gateway.py)

####  Execute and run the run_twitter_etl function 

1. Log in to your EC2 instance using SSH link
2. Enter the airflow folder
3. Create a folder where you will install all the dependencies: the [twitter_etl_py]() and the [twitter_dag.py]()
![](https://github.com/nadinelabidi/Ehealth-Kafka-Project/blob/main/Kafka_file/gateway.py)
4. Run airflow server 
```
airflow standalone
```
5. Use the public IPv4 DNS to open airflow interface
6. Look for the twitter_dag in the list of dags
7. Run the dag
![](https://github.com/nadinelabidi/Ehealth-Kafka-Project/blob/main/Kafka_file/gateway.py)
8. Create a role and attach it to the ec2:
   - Give the EC2 instance full access to s3 bucket to be able to write the reuslts in the s3 bucket we created
9. Once the tasks are marked as success,check your dataframe is stored in the s3 bucket.


