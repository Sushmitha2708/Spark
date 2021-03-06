from pyspark.sql import SparkSession
from pyspark.sql.functions import desc,asc

spark = SparkSession.builder.appName("Pyspark example").getOrCreate()


df = spark.read.format("json").load("/data/sample_data1.json")
df.createOrReplaceTempView("dftable")

df.sort("count").show(5)
#OR
df.orderBy("count","DEST_COUNTRY_NAME").show(5)

#To specify sort direction use 'asc' and 'desc' functions.
from pyspark.sql.funcctions import desc,asc
df.orderBy("count desc").show(5)
df.orderBy("count desc", "DEST_COUNTRY_NAME asc").show(5)
