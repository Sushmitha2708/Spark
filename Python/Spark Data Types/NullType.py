from pyspark.sql import SparkSession
from pyspark.sql.functions import col,coalesce,asc_nulls_first,col
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

df= spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:/Users/Lenovo/Desktop/spark_data/retail_store.csv")
df.createOrReplaceTempView("dfTable")

#'coalesce' function selects the first non-null value from a set of columns
df.select(coalesce(col("Description"),col("CustomerId"))).show()

#'drop' method removes rows that contains null values. The 'all' argument drpos the rows only if all the values are null.
df.na.drop("all",subset=["StockCode","InvoiceNo"]).show()

#'fill' method fills all null values in a column with specified values
fillValues={"StockCode":10,"Description":"String value"}
df.na.fill(fillValues).show()

#'replace' null values or spaces with specified values
df.na.replace([""],["Unknown"],"Description").show()

#'asc_nulls_first' method displays the rows which have null values first in the table
df.orderBy(col("Description").asc_nulls_first(),col("Description")).show()