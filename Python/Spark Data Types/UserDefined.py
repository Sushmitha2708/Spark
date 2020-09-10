from pyspark.sql import SparkSession
from pyspark.sql.functions import col,udf
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

exampledf= spark.range(5).toDF("num")
def power3(val):
	return val ** 3


power3udf= udf(power3)
exampledf.select(power3udf(col("num"))).show(3)