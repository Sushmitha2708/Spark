from pyspark.sql import SparkSession
from pyspark.sql.functions import col,get_json_object,json_tuple
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

jsonDF= spark.range(1).selectExpr(""" 
	'{"key":
			{"value":[1,2,3]}}' 
					as jsonString """)

jsonDF.select(
	get_json_object(col("jsonString"),"$.key.value[0]").alias("column"),
	json_tuple(col("jsonString"),"key")).show(2)