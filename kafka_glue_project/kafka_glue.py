from aws_cdk import (
    Stack,
    aws_msk as msk,
    aws_glue as glue,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_s3 as s3,
    aws_redshift as redshift,
    aws_events as events,
    aws_events_targets as targets,
)
from constructs import Construct


class DataEngineeringStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define your resources here

        # Example: MSK Cluster
        kafka_cluster = msk.CfnCluster(
            self,
            "MyKafkaCluster",
            cluster_name="my-kafka-cluster",
            kafka_version="3.5.1",  # Specify the Kafka version
            number_of_broker_nodes=3,  # Number of broker nodes in the cluster
            broker_node_group_info={
                "instance_type": "kafka.t3.small",  # Specify the instance type
                "client_subnet_ids": ["subnet-12345678", "subnet-87654321"],
            },
        )

        # Example: Glue Job
        glue_job = glue.CfnJob(
            self,
            "MyGlueJob",
            name="my-glue-job",
            role="your-glue-role-arn",
            command=glue.CfnJob.JobCommandProperty(
                script_location="s3://your-glue-scripts-bucket/glue_script.py"
            ),
            # ... other configurations
        )

        # Example: Lambda Function
        lambda_function = _lambda.Function(
            self,
            "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="your_lambda_function.handler",
            code=_lambda.Code.from_asset("path/to/your/lambda/code"),
            # ... other configurations
        )

        # Example: DynamoDB Table
        dynamo_table = dynamodb.Table(
            self,
            "MyDynamoDBTable",
            table_name="my-dynamo-table",
            # ... other configurations
        )

        # Example: S3 Buckets
        landing_bucket = s3.Bucket(self, "LandingBucket", bucket_name="landing-bucket")
        raw_data_bucket = s3.Bucket(
            self, "RawDataBucket", bucket_name="raw-data-bucket"
        )

        # Example: Redshift Cluster
        redshift_cluster = redshift.CfnCluster(
            self,
            "MyRedshiftCluster",
            cluster_identifier="my-redshift-cluster",
            # ... other configurations
        )

        # Example: CloudWatch Event Rule for Scheduler
        event_rule = events.Rule(
            self,
            "MyEventRule",
            schedule_expression="cron(0 0 * * ? *)",  # Daily at midnight
        )
        event_rule.add_target(targets.LambdaFunction(lambda_function))
