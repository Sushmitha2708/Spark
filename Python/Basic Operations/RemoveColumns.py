from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Pyspark example").getOrCreate()


df = spark.read.format("json").load("/data/sample_data1.json")
df.createOrReplaceTempView("dftable")

df.drop("ORIGIN_COUNTRY_NAME").columns
