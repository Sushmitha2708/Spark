from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

from pyspark.sql import Row
from pyspark.sql.types import StructField, StringType, StructType, LongType

mySchema = StructType([ StructField("column1", StringType(), True),
                        StructField("column2", StringType(), True),
                        StructField("column3", LongType(), False)
                      ])
myRow = Row("Bonjour", "French", 1)
myDf = spark.createDataFrame([myRow], mySchema)
myDf.show()
