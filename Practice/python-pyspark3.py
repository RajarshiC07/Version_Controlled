from pyspark.sql import SparkSession as SS
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType
import pandas as pd
from Practice import pythonpandasprac2 as ppd2
from pyspark.sql.functions import *

session = SS.builder.appName('Sample').getOrCreate()
rdd = session.sparkContext.parallelize([1, 2, 3, 4, 5], 1)
print(rdd.collect())
print(rdd.getNumPartitions())

# **************** Reading files using option and options. Option can chain one after another to perform like options
# ****************** ###
file1 = session.read.option('header', 'true').csv('csvfile1.csv', inferSchema=True)
file2 = session.read.options(header=True, inferSchema=True).csv('.\\Files\\csvfile1.csv')
file1.printSchema()
# **************** Accessing values in row formats ****************** ###
print(file1.take(1))
print(file1.head(1))
print(file1.limit(1).show())
file1.show(1)
print(file1.first())
print(file1.sample(0.1))

print(file2.limit(2).show())
print(file2.describe())
# **************** Accessing columns and understanding DataFrames ****************** ###
columns = file1.columns
print(columns)
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = columns
print(c10, type(c10))


file2.toDF(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10).limit(2).show()
print(file2.columns == file2.toDF(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10).columns)

print(file2['Year'])
print(file2.Year)
file1.select('Year', file1.Value, file1['Units']).show(3)
file1.select(concat(lit('Year'), file1.Value)).withColumnRenamed('concat(Year, Value)', 'Code').show(5)
file1.select(concat('Year', file1.Value)).withColumnRenamed('concat(Year, Value)', 'Code').show(5)
file3 = file1.withColumnRenamed('Year', 'Year-of-Access')
schema = StructType(
    [StructField('day', StringType()), StructField('month', StringType()), StructField('year', StringType())])
file3.select(col('Year-of-Access').cast(StringType())).show(2)
print(file3.select(file3.Units, col('Value')).distinct().show())




