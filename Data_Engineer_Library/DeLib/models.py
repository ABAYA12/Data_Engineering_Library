from django.db import models

# Create your models here.
class PipelineDetails(models.Model):

    # Choices for different fields
    project_purpose_choices = [
        ('ETL', 'ETL'),
        ('Data Analysis', 'Data Analysis'),
        ('Data Visualization', 'Data Visualization'),
        ('Data Modeling', 'Data Modeling'),
        ('Data Warehousing', 'Data Warehousing'),
        ('Data Lake', 'Data Lake'),
        ('Data Science', 'Data Science'),
        ('Machine Learning', 'Machine Learning'),
        ('Deep Learning', 'Deep Learning'),
        ('Natural Language Processing', 'Natural Language Processing'),
        ('Computer Vision', 'Computer Vision'),
        ('Big Data', 'Big Data'),
        ('Data Engineering', 'Data Engineering'),
        ('Data Governance', 'Data Governance'),
        ('Data Quality', 'Data Quality'),
        ('Data Security', 'Data Security'),
        ('Data Privacy', 'Data Privacy'),
        ('Data Catalog', 'Data Catalog'),
        ('Data Lineage', 'Data Lineage'),
        ('Data Profiling', 'Data Profiling'),
        ('Data Masking', 'Data Masking'),
        ('Data Monitoring', 'Data Monitoring'),
        ('Data Orchestration', 'Data Orchestration'),
        ('Data Pipelines', 'Data Pipelines'),
        ('Data Replication', 'Data Replication'),
        ('Data Integration', 'Data Integration'),
        ('Data Migration', 'Data Migration'),
        ('Data Transformation', 'Data Transformation'),
        ('Data Ingestion', 'Data Ingestion'),
        ('Data Streaming', 'Data Streaming'),
        ('Data Batch Processing', 'Data Batch Processing'),
        ('Data Real-time Processing', 'Data Real-time Processing')
    ]

    database_choices = [
        ('MySQL', 'MySQL'),
        ('PostgreSQL', 'PostgreSQL'),
        ('MongoDB', 'MongoDB'),
        ('Azure SQL Database', 'Azure SQL Database'),
        ('Amazon Redshift', 'Amazon Redshift'),
        ('Google Cloud Spanner', 'Google Cloud Spanner'),
        ('DynamoDB', 'DynamoDB'),
        ('Cassandra', 'Cassandra'),
        ('Snowflake', 'Snowflake'),
        ('Oracle Database', 'Oracle Database'),
        ('IBM Db2', 'IBM Db2'),
        ('SQL Server', 'SQL Server'),
        ('Sybase', 'Sybase'),
        ('MariaDB', 'MariaDB'),
        ('SQLite', 'SQLite'),
        ('Firebase', 'Firebase'),
        ('Google Cloud Firestore', 'Google Cloud Firestore'),
        ('Google Cloud Bigtable', 'Google Cloud Bigtable'),
        ('Apache Cassandra', 'Apache Cassandra')
    ]

    datawarehouse_choices = [
        ('Amazon Redshift', 'Amazon Redshift'),
        ('Google Cloud Spanner', 'Google Cloud Spanner'),
        ('Snowflake', 'Snowflake'),
        ('Oracle Database', 'Oracle Database'),
        ('IBM Db2', 'IBM Db2'),
        ('SQL Server', 'SQL Server'),
        ('MariaDB', 'MariaDB'),
        ('Google Cloud Firestore', 'Google Cloud Firestore'),
        ('Google Cloud Bigtable', 'Google Cloud Bigtable')
    ]

    cloud_provider_choices = [
        ('AWS', 'Amazon Web Services (AWS)'),
        ('Azure', 'Microsoft Azure'),
        ('GCP', 'Google Cloud Platform (GCP)'),
        ('IBM Cloud', 'IBM Cloud'),
        ('Oracle Cloud', 'Oracle Cloud'),
        ('Alibaba Cloud', 'Alibaba Cloud'),
        ('Snowflake', 'Snowflake'),
        ('Databricks', 'Databricks'),
        ('Cloudera', 'Cloudera'),
        ('BigQuery', 'Google BigQuery'),
        ('Redshift', 'Amazon Redshift'),
        ('Synapse', 'Azure Synapse Analytics'),
        ('Dremio', 'Dremio'),
        ('Flink', 'Apache Flink Cloud Services'),
        ('Confluent', 'Confluent Cloud (Kafka)'),
        ('DataBricks', 'DataBricks on AWS/Azure'),
        ('Firebolt', 'Firebolt'),
        ('ClickHouse', 'ClickHouse Cloud'),
        ('ElasticSearch', 'Elastic Cloud'),
        ('MinIO', 'MinIO Object Storage')
    ]

    project_type_choices = [
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Government', 'Government'),
        ('Healthcare', 'Healthcare'),
        ('Insurance', 'Insurance'),
        ('Manufacturing', 'Manufacturing'),
        ('Retail', 'Retail'),
        ('Service', 'Service'),
        ('Technology', 'Technology'),
        ('Transportation', 'Transportation'),
        ('Other', 'Other')
    ]

    category_choices = [
        ('Personal', 'Personal'),
        ('Company', 'Company'),
        ('Group', 'Group'),
        ('Community', 'Community')
    ]

    # Model Fields
    author = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100, choices=project_purpose_choices, default='ETL')
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=250)
    category = models.CharField(max_length=100, choices=category_choices, default='Personal')
    database_type = models.CharField(max_length=100, choices=database_choices, default='MySQL')
    cloud_provider = models.CharField(max_length=100, choices=cloud_provider_choices, default='AWS')
    datawarehouse = models.CharField(max_length=100, choices=datawarehouse_choices, default='Amazon Redshift')
    type_of_project = models.CharField(max_length=100, choices=project_type_choices, default='Business')
    version = models.CharField(max_length=50)
    source_code_url = models.URLField(max_length=250)
    description = models.TextField()
    year = models.IntegerField()

