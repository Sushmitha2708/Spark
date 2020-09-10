from pyspark.sql import SparkSession
from pyspark.sql.functions import col,split,size,array_contains,explode
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

df= spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:/Users/Lenovo/Desktop/spark_data/retail_store.csv")
df.createOrReplaceTempView("dfTable")

#'split' function splits values in a column based on a specified delimiter
df.select(split(col("Description")," ")).show(3)
df.select(split(col("Description")," ").alias("new_col")).show(3)

#'size' method determines the length of the array
df.select(size(split(col("Description")," "))).show(3)

#'array_contains' method determines if an array contains a specufied value
df.select(array_contains(split(col("Description")," "),"WHITE")).show(3)

#'explode' method takes a column of arrays and creates a new row oer value in the array
df.withColumn("split",split(col("Description")," ")).withColumn("exploded",explode(col("split"))).select("Description","exploded").show(7)
