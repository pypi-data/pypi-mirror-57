import sys
import logging
import pandas as pd
from os import path as opath


def reduce_memory_usage(df):
    """reduce memory usage of the dataframe

    - convert runIDs to categorical
    - downcast ints and floats
    """
    usage_pre = df.memory_usage(deep=True).sum()
    if "runIDs" in df:
        df.loc[:, "runIDs"] = df.loc[:, "runIDs"].astype("category")
    df_int = df.select_dtypes(include=['int'])
    df_float = df.select_dtypes(include=['float'])
    df.loc[:, df_int.columns] = df_int.apply(pd.to_numeric, downcast='integer')
    df.loc[:, df_float.columns] = df_float.apply(pd.to_numeric, downcast='float')
    usage_post = df.memory_usage(deep=True).sum()
    logging.info("Reduced DataFrame memory usage from {}Mb to {}Mb".format(
        usage_pre / 1024**2, usage_post / 1024**2))
    if usage_post > 4e9 and "readIDs" in df:
        logging.info("DataFrame of features is too big, dropping read identifiers.")
        return df.drop(["readIDs"], axis=1, errors="ignore")
    else:
        return df


def check_existance(f):
    """Check if the file supplied as input exists."""
    if not opath.isfile(f):
        logging.error("Nanoget: File provided doesn't exist or the path is incorrect: {}".format(f))
        sys.exit("File provided doesn't exist or the path is incorrect: {}".format(f))
