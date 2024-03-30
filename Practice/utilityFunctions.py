import pyspark.sql
from pyspark.sql.functions import col, explode_outer
from pyspark.sql.types import StructType, ArrayType


# sample in pyspark6.py
def flatten_df(df: pyspark.sql.dataframe.DataFrame):
    nested_df = dict([(field.name, field.dataType) for field in df.schema.fields if
                      type(field.dataType) == ArrayType or type(field.dataType) == StructType])

    while len(nested_df) > 0:
        col_name = list(nested_df.keys())[0]

        if type(nested_df[col_name]) == StructType:
            expanded = [col(col_name + "." + k).alias(col_name + "." + k) for k in
                        [n.name for n in nested_df[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        elif type(nested_df[col_name]) == ArrayType:
            df = df.withColumn(col_name, explode_outer(col_name))

        nested_df = dict([(field.name, field.dataType) for field in df.schema.fields if
                          type(field.dataType) == ArrayType or type(field.dataType) == StructType])

    return df


def column_assign(df: pyspark.sql.dataframe.DataFrame):
    # cols = [tup[::-1] for tup in df.dtypes]

    cols = {field.name: field.dataType for field in df.schema.fields}
    cols_dict = {}
    for v, k in cols.items():
        cols_dict[k] = cols_dict.get(k, []) + [v]

    return cols_dict
