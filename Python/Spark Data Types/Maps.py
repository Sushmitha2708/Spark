from pyspark.sql import SparkSession
from pyspark.sql.functions import col,create_map,explode
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

df= spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:/Users/Lenovo/Desktop/spark_data/retail_store.csv")
df.createOrReplaceTempView("dfTable")

df.select(create_map(col("Description"),col("InvoiceNo")).alias("map_column")).show(3)

