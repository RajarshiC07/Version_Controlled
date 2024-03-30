from pyspark.sql import SparkSession
import numpy as nm
import pandas as pd
from pyspark.context import SparkContext
spark = SparkSession.builder.appName("Sample").getOrCreate()
file1 = spark.read.csv('D:\python projects\Practice\Files\csvfile1.csv')
sch = file1.schema

# file1.show()
# print(type(file1))
# file2 = spark.read.option('header', 'true').csv('texts.txt', lineSep='\n', inferSchema=True)
# # print(file2)
# # file2.printSchema()
# file2.show()
# file3 = spark.read.csv('texts.txt', inferSchema=True, header=True)
# # print(file3)
# file3.show()
# cols = list(file3.columns)
# # print(cols)
# file3.withColumnRenamed('C', 'ThirdColumn').show()
# file3.select(['A', 'D']).show()
# # print(file3.dtypes)
# # print(file3.describe())
# file3.withColumn('E', file3['D'] * 2).show()
#
# # print(type(file3['D']))

file4 = spark.read.csv('sparkfile.csv', inferSchema=True, header=True)
file4.show()
# file4.na.drop(how='any', thresh=1, subset='D').show()

# file4.na.df.show()
file4.filter('D<=30').select(['C', 'D']).show()
file4.groupBy('A').sum('D').show()
file4.groupby('A').max('D').show()
file4.toPandas().drop(columns='_c0')
rdd = spark.sparkContext.parallelize('text.txt')
string = str(type(spark.sparkContext))


