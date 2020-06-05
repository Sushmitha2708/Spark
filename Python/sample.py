from pyspark import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("simpleapp").getOrCreate() # Spark session is created
print("Hey!")
spark.stop()
