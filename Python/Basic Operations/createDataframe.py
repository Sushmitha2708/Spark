from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()


df= spark.read.format("json").load("F:/Spark/Python/Basic Operations/data/sample_data1.json")
df.createOrReplaceTempView("dfTable")
df.show(5)
