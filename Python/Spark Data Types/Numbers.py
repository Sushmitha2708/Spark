from pyspark.sql import SparkSession
from pyspark.sql.functions import expr,pow,col
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

df= spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:/Users/Lenovo/Desktop/spark_data/retail_store.csv")
#df.printSchema() # Prints the schema of 'retail_store.csv'
df.createOrReplaceTempView("dfTable")

newQuantity= pow(col("Quantity")*col("UnitPrice"),2)+5 #(current quantity*unit price)^2 +5
df.select(expr("CustomerId"),newQuantity.alias("New Quantity")).show(3)


from pyspark.sql.functions import lit, round, bround
df.select(round(lit("2.5")),bround(lit("2.5"))).show(3)

df.describe().show() #To display count,mean,avg,min and max