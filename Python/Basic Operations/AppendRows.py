from pyspark.sql import SparkSession
from pyspark.sql.functions import Row
spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()


df = spark.read.format("json").load("F:/Spark/Python/Basic Operations/data/sample_data1.json")
df.createOrReplaceTempView("dftable")

#To append to dataframe, UNION of original dataframe along with the new dataframe
from pyspark.sql import Row
schema = df.schema
newrows = [Row("New Country","Other country",1),
         Row("New Country1","Other country1",5)]
     
parallelizedRows=spark.sparkContext.parallelize(newrows)
newDf = spark.createDataFrame(parallelizedRows,schema)

df.union(newDf)
