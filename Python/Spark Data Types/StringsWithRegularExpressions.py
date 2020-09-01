from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace,col,translate,regexp_extract,instr
spark = SparkSession.builder.appName("Pyspark example").getOrCreate()

df= spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:/Users/Lenovo/Desktop/spark_data/retail_store.csv")
#'regexp_replace' is used to replace substitute color names with NOCOLOR
str1="BLACK|WHITE|RED|BLUE|GREEN"
df.select(regexp_replace(col("Description"),str1,"NOCOLOR").alias("no_color_column"),col("Description")).show(5)

#'translate' function is to replace given characters with other characters
df.select(translate(col("Description"),"ABCD","1234"),col("Description")).show(5)

#'regexp_extract' is used to extract values
df.select(regexp_extract(col("Description"),str1,0).alias("color"),col("Description")).show(5)

#'instr' function checks for the existance of a value
containsRed= instr(col("Description"),"RED")>=1
containsWhite= instr(col("Description"),"WHITE")>=1
df.withColumn("hasColor",containsWhite| containsRed).where("hasColor").select("Description").show(5)