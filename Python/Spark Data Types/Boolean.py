from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

df= spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:/Users/Lenovo/Desktop/spark_data/retail_store.csv")
#df.printSchema() # Prints the schema of 'retail_store.csv'
df.createOrReplaceTempView("dfTable")

df.where(col("InvoiceNo")!=536365).select("InvoiceNo","Description").show(5,False)


