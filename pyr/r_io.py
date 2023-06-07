import pandas as pd
from pyreadr import read_r


def rdata_extract_lone_dataframe(filename: str) -> pd.DataFrame:
    """
    Creates a pandas DataFrame object from the given .Rdata file

    Expects the filename (or filepath if necessary) of a .Rdata file
    which contains a single data.frame object (or equivalent). This is
    extracted and returned as a pandas DataFrame. Throws a TypeError
    if the .Rdata file contains more than one object.

    Parameters
    ----------
    a : Rdata filename

    Returns
    -------
    r : pandas DataFrame object

    Example
    -------

    TODO: add example to docstring
    """

    rdata_tables = read_r(filename)
    key_list = list(rdata_tables.keys())
    if len(key_list) > 1:
        raise TypeError("Target .Rdata file contains more than one object.")
    lone_key = key_list[0]
    lone_table = rdata_tables[lone_key]
    return lone_table


def rdata_extract_named_dataframe(
    filename: str, target_table_name: str
) -> pd.DataFrame:
    """
    Creates a pandas DataFrame object from the given .Rdata file and table name

    Expects the filename (or filepath if necessary) of a .Rdata file
    which contains the data.frame (or equivalent) specified by
    the "target_table_name" parameter. This is extracted and returned as
    a pandas DataFrame.

    Parameters
    ----------
    a : Rdata filename

    b : name of data.frame (or table, tibble, etc.)

    Returns
    -------
    r : pandas DataFrame object

    Example
    -------

    TODO: add example to docstring
    """

    rdata_tables = read_r(filename)
    target_table = rdata_tables[target_table_name]
    return target_table
