

df= spark.read.format("json").load("F:/Spark/Python/Basic Operations/data/sample_data1.json")
df.createOrReplaceTempView("dfTable")
df.show(5)
