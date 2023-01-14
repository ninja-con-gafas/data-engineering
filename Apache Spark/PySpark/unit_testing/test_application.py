from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from pyspark.sql.types import StructType, StructField, StringType
from application import create_dataframe


class Test(TestCase):

    @patch("application.spark")
    def test_can_create_dataframe_with_data_and_schema(self,
                                                       mock_spark):
        # arrange
        data = {"key": "value"}
        schema = StructType([StructField(name="key",
                                         dataType=StringType(),
                                         nullable=True)])

        mock_dataframe = MagicMock()
        mock_spark.createDataFrame.return_value = mock_dataframe

        # act
        create_dataframe(data, schema)

        # assert
        mock_spark.createDataFrame.assert_called_once_with(data=data,
                                                           schema=schema)

    @patch("application.logging")
    def test_can_detect_empty_dataframe(self, mock_logging):
        # arrange
        data = {}
        schema = StructType()

        mock_logging.warning.return_value = None

        # act
        create_dataframe(data, schema)

        # assert
        mock_logging.warning.assert_called_once_with("Empty dataframe")


if __name__ == '__main__':
    main()
