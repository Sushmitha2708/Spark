from pyspark.sql import SparkSession
from pyspark.sql.functions import lit,expr
spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()


df = spark.read.format("json").load("F:/Spark/Python/Basic Operations/data/sample_data1.json")
df.createOrReplaceTempView("dftable")

df.withColumn("One", lit(1)).show(5)
#OR
df.withColumn("withihcountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME")).show(5)
