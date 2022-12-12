from pyspark.sql.types import StructField, StructType, StringType, MapType
from spark import SparkBase

test_data = [
    ('Kate', {'dog': 'Jake', 'cat': 'Puss'}),
    ('Adam', {'dog': 'Hug', 'cat': 'Me'}),
]

schema = StructType([
    StructField('owner', StringType(), True),
    StructField('pets', MapType(StringType(), StringType()), True)
])

if __name__ == "__main__":
    client = SparkBase(app_name="test1")
    client.read_table(test_data, schema)
