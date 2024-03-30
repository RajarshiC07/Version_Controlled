from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Sample1').getOrCreate()
rdd = spark.sparkContext.parallelize('texts.txt')
rdd1 = spark.sparkContext.textFile('texts.txt')
lines = rdd.flatMap(lambda x: x.split(","))

