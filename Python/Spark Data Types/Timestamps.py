from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp,lit,to_date,col
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

dateformat="yyyy-dd-MM"
dateDF1=spark.range(1).select(to_date(lit("2020-27-08"),dateformat).alias("date"),to_date(lit("2020-26-08"),dateformat).alias("date1"))
dateDF1.createOrReplaceTempView("dataTable2")
dateDF1.select(to_timestamp(col("date"),dateformat)).show()
