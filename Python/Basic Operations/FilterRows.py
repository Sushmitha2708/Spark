from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()


df = spark.read.format("json").load("/data/sample_data1.json")
df.createOrReplaceTempView("dftable")

df.where("count < 3").show(5)

#For multiple conditions
df.where("count < 3").where("ORIGIN_COUNTRY_NAME != 'Croatia'").show(5)

#Getting unique rows
df.select("ORIGIN_COUNTRY_MANE").distinct().count()

