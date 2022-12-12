import pyspark

spark_cores_max = 1
spark_exec_cores = 1
spark_exec_memo = '1gb'


def set_spark_cfg():
    cfg = [
        ("spark.cores.max", spark_cores_max),
        ('spark.executor.cores', spark_exec_cores),
        ('spark.executor.memory', spark_exec_memo),
    ]
    return cfg


class SparkBase:
    def __init__(self, app_name):
        host = 'spark://spark-master:7077'
        conf = pyspark.SparkConf().setAll(set_spark_cfg())
        self.spark = pyspark.sql.SparkSession.builder \
            .appName(app_name) \
            .config(conf=conf) \
            .master(host) \
            .getOrCreate()

    def read_table(self, data, schema):
        df = self.spark.createDataFrame(data=data, schema=schema)
        df.show()
