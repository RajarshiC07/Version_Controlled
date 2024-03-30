from Practice.utilityFunctions import flatten_df, column_assign
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, array_contains, udf, monotonically_increasing_id, explode_outer, flatten, explode

session = SparkSession.builder.appName('Sample').getOrCreate()
areas_json = session.read.options(header=True, inferSchema=True, multiline=True).json(
    r"C:\Users\rajar\Downloads\Files\areas.json")
persons_json = session.read.options(header=True, inferSchema=True, multiline=True).json(
    r"C:\Users\rajar\Downloads\Files\persons.json")
events_json = session.read.options(header=True, inferSchema=True, multiline=True).json(
    r"C:\Users\rajar\Downloads\Files\events.json")

areas_json.printSchema()
persons_json.printSchema()
events_json.printSchema()

new_persons_json = persons_json.withColumn("Ref_id", monotonically_increasing_id())
new_areas_json = areas_json.withColumn("Ref_id", monotonically_increasing_id())
new_events_json = events_json.withColumn("Ref_id", monotonically_increasing_id())

# new_persons_json.toPandas().to_json(r"C:\Users\rajar\Downloads\Files\New_Folder\new_persons.json")
# new_areas_json.toPandas().to_json(r"C:\Users\rajar\Downloads\Files\New_Folder\new_areas.json")
# new_events_json.toPandas().to_json(r"C:\Users\rajar\Downloads\Files\New_Folder\new_events.json")


# new_persons_json.select(explode_outer("identifiers")).printSchema()
persons_json.printSchema()
persons_json.show(10)

new_df = flatten_df(persons_json)
new_df.printSchema()


new_df = column_assign(new_df)
for k, v in new_df.items():
    print(k, "\t", v, "\n")
