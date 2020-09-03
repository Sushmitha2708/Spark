from pyspark.sql import SparkSession
from pyspark.sql.functions import struct
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

df= spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:/Users/Lenovo/Desktop/spark_data/retail_store.csv")
df.createOrReplaceTempView("dfTable")

#'StructType' is used to define the schema of a dataframe
df1= df.select(struct("UnitPrice","InvoiceNo").alias("complex"))
df1.createOrReplaceTempView("df1table")
df1.show()

df1.select("complex.UnitPrice").show()