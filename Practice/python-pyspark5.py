from pyspark.sql import SparkSession
from pyspark.sql.functions import count, desc, col

ss = SparkSession.builder.appName('prac').getOrCreate()

genre_path = r"C:\Users\RAJARSCH\Downloads\genre.csv"
genre_df = ss.read.options(header=True, inferSchema=True).csv(genre_path)

listenings_path = r"C:\Users\RAJARSCH\Downloads\listenings.csv"
listenings_df = ss.read.options(header=True, inferSchema=True).csv(listenings_path)

listenings_df.show(2)
genre_df.show(2)

listenings_df.select('artist', 'track').groupby('artist', 'track').agg(count('*').alias("count")).orderBy(
    desc("count")).show(10)
# listenings_df.filter(col("track") == "Sorry").show()

listenings_df.createOrReplaceTempView("listenings_df")
ss.sql("select * from listenings_df").show(2)
