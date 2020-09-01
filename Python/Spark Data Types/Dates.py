from pyspark.sql import SparkSession
from pyspark.sql.functions import col,current_date,current_timestamp,date_sub,date_add,datediff,months_between,to_date
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()
dateDf= spark.range(10).withColumn("Today",current_date()).withColumn("Now",current_timestamp())
dateDf.createOrReplaceTempView("dftable")
dateDf.show()
dateDf.printSchema()

#'date_sub' and 'date_add' can be used to add and subtract from a particular date
dateDf.select(date_sub(col("Today"),5),date_add(col("Today"),4)).show(2)

#'dateddiff' and 'months_between' functions give number of dates and number of months between two dates
dateDf.withColumn("week_ago",date_sub(col("Today"),7)).select(datediff(col("week_ago"),col("Today"))).show(1)
