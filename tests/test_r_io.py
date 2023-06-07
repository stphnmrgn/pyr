# Using pytest framework
# For VSCode implementation tips, see
#   https://code.visualstudio.com/docs/python/testing

# Dummy dataframes info (in ./test_data):
# dummy_training_data_0x: contains 1-2 tables, generally of type data.frame:
#                 ..._01: table_one
#                 ..._02: table_one, table_two
#                 ..._03: table_two
#                 ..._04: table_one (but saved as a tibble)
#   with tables:
#     - table_one - 3 columns of R types "numeric", "factor", "character"
#     - table_two - 4 columns of R types "numeric", "factor", "character", "logical"'
#       (fourth column is entirely of value NA)

import pytest
import pandas as pd

import pyr.r_io as rio


def helper_check_integrity_dummy_training_data_0x_table_one(loaded_df):
    # check integrity of dataframe "table_one" with 3 columns
    assert list(loaded_df) == ["col_ints", "col_factors", "col_strings"]
    # TODO: check for proper types
    assert isinstance(loaded_df.col_factors.dtype, pd.api.types.CategoricalDtype)


def helper_check_integrity_dummy_training_data_0x_table_two(loaded_df):
    # check integrity of dataframe "table_two" with 4 columns
    assert list(loaded_df) == ["col_ints", "col_factors", "col_strings", "col_na"]
    # TODO: check for proper types


def test_rdata_extract_lone_dataframe():
    # lone table "table_one"
    rdata_df = rio.rdata_extract_lone_dataframe(
        "./test_data/dummy_training_data_01.Rdata"
    )
    helper_check_integrity_dummy_training_data_0x_table_one(rdata_df)

    # make sure exception is thrown when more than one table exists
    with pytest.raises(TypeError):
        rio.rdata_extract_lone_dataframe("./test_data/dummy_training_data_02.Rdata")

    # lone table "table_two"
    rdata_df = rio.rdata_extract_lone_dataframe(
        "./test_data/dummy_training_data_03.Rdata"
    )
    helper_check_integrity_dummy_training_data_0x_table_two(rdata_df)

    # Make sure a tibble is loaded in okay
    rdata_df = rio.rdata_extract_lone_dataframe(
        "./test_data/dummy_training_data_04.Rdata"
    )
    helper_check_integrity_dummy_training_data_0x_table_one(rdata_df)


def test_rdata_extract_named_dataframe():
    # lone table "table_one"
    rdata_df = rio.rdata_extract_named_dataframe(
        "./test_data/dummy_training_data_01.Rdata", "table_one"
    )
    helper_check_integrity_dummy_training_data_0x_table_one(rdata_df)

    # table "table_two" from .Rdata with two tables
    rdata_df = rio.rdata_extract_named_dataframe(
        "./test_data/dummy_training_data_02.Rdata", "table_two"
    )
    helper_check_integrity_dummy_training_data_0x_table_two(rdata_df)

    # make sure exception is thrown when table doesn't exist
    with pytest.raises(KeyError):
        rio.rdata_extract_named_dataframe(
            "./test_data/dummy_training_data_03.Rdata", "table_one"
        )
