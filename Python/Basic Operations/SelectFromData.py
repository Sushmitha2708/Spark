from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()


df = spark.read.format("json").load("/data/sample_data1.json")
df.createOrReplaceTempView("dftable")

df.select("DEST_COUNTRY_NAME").show(5)
df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(5)
