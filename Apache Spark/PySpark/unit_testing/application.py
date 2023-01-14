from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
import logging
from typing import Any

spark = SparkSession.builder \
    .master("local[4]") \
    .appName("application") \
    .getOrCreate()


def create_dataframe(data: Any, schema: StructType) -> None:
    data = spark.createDataFrame(data=data, schema=schema)

    if data.isEmpty():
        logging.warning("Empty dataframe")
        return

    data.show()
