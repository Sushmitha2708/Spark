from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

spark = SparkSession.builder.appName("Pyspark example").getOrCreate()



df = spark.read.format("json").load("data/sample_data1.json")
df.createOrReplaceTempView("dftable")

df.withColumn("One", lit(1)).show(5)
#OR
df.withColumn("withihcountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME")).show(5)
