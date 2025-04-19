import pandas as pd
import pytest
from sqlalchemy import create_engine
import cx_Oracle

engine = create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe")

def test_data_type_validation():
    query = """select * from city"""
    df = pd.read_sql(query,engine)
    print("actual data :",df)
    actual_datatype = df.dtypes.to_dict()
    print("data type of actual  : ",actual_datatype)
    expected_datatype = {"id":"int64","name":"object"}
    print("data type of expected  : ", expected_datatype)

    assert actual_datatype == expected_datatype,"actual datatype doesn not expected"





