from pyspark.sql import SparkSession
from pyspark.sql.functions import col, array_contains, udf, monotonically_increasing_id
import numpy as nm

session = SparkSession.builder.appName('Sample').getOrCreate()
areas_json = session.read.options(header=True, inferSchema=True).json(r"C:\Users\RAJARSCH\Desktop\areas.json")
countries_json = session.read.options(header=True, inferSchema=True).json(
    "C:\\Users\\RAJARSCH\\Desktop\\countries.json")
events_json = session.read.options(header=True, inferSchema=True).json(r"C:\Users\RAJARSCH\Desktop\events.json")
membership_json = session.read.options(header=True, inferSchema=True).json(
    r"C:\Users\RAJARSCH\Desktop\memberships.json")
organization_json = session.read.options(header=True, inferSchema=True). \
    json(r"C:\Users\RAJARSCH\Desktop\organizations.json")
persons_json = session.read.options(header=True, inferSchema=True).json(r"C:\Users\RAJARSCH\Desktop\persons.json")

persons_json.printSchema()

absent = [None, 'null', 0]

# showing non null values ******************************************************************************
for rows in persons_json.select('contact_details').collect():
    if any(str(absent_val).upper() in str(rows) for absent_val in absent):
        print(rows)

persons_json.filter(persons_json['given_name'].contains("null")).show(5)
persons_json.select(persons_json['given_name']).show(10)
file1 = persons_json.where(persons_json['given_name'].endswith("l"))
file1.show()
persons_json.filter(persons_json['family_name'].isNotNull()).sort(persons_json['family_name']).show(10)

#
# def func(x):
#     print(x)
#
# pudf = udf(lambda x: func(x))
# print(persons_json.withColumn("family_name", pudf(persons_json['family_name'])))

persons_json.drop("_corrupt_record").show(10)

# Using sample ******************************************************************************************************
print(persons_json.count())
print(persons_json.sample(0.5).count())
print(persons_json.sample(0.5, 123).show(2))
print(persons_json.sample(0.5, 123).show(2))
print(persons_json.sample(0.5, 456).show(2))

# Magic of collect **************************************************************************************************
print(persons_json.select("identifiers").collect()[0])
print(persons_json.select("identifiers").collect()[0][0])
print(persons_json.select("identifiers").collect()[0][0][0])
print(persons_json.select("identifiers").collect()[0][0][0][0])

persons_json.dropna().show()
print((persons_json.count(), len(persons_json.columns)))
persons_json.select(col('birth_date'), col('death_date')).show(5)

# Inserting special id column ***************************************************************************************

new_persons_json = persons_json.withColumn("Ref_id", monotonically_increasing_id()).drop("_corrupt_record")
new_areas_json = areas_json.withColumn("Ref_id", monotonically_increasing_id())

# Writing to a json file ********************************************************************************************

new_persons_json.toPandas().to_json(r"C:\Users\RAJARSCH\Desktop\new_persons.json")
new_areas_json.toPandas().to_json(r"C:\Users\RAJARSCH\Desktop\new_areas.json")
