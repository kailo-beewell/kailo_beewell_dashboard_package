'''
Helper function for importing the data from TiDB Cloud
'''
import numpy as np
import pandas as pd
import streamlit as st
from tempfile import NamedTemporaryFile
import pymysql


def get_df(query, conn):
    '''
    Get data from the connected SQL database

    Parameters:
    -----------
    query : string
        SQL query
    conn : connection object
        Connection to the SQL database

    Returns:
    --------
    df : pandas DataFrame
        Dataframe produced from the query
    '''
    cursor = conn.cursor()
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    return df


def import_tidb_data(survey_type):
    '''
    Imports all the datasets from TiDB Cloud, fixes any data type issues, and
    saves the datasets to the session state.

    Parameters
    ----------
    survey_type : string
        Designates whether to import for 'standard' or 'symbol' survey
    '''
    # Define the session state variables (keys) and TIDB datasets (values)
    if survey_type == 'standard':
        items = {'scores_rag': 'standard_school_aggregate_scores_rag',
                 'responses': 'standard_school_aggregate_responses',
                 'counts': 'standard_school_overall_counts',
                 'demographic': 'standard_school_aggregate_demographic'}
    elif survey_type == 'symbol':
        items = {'responses': 'symbol_school_aggregate_responses',
                 'counts': 'symbol_school_overall_counts',
                 'demographic': 'symbol_school_aggregate_demographic'}

    # First, check if everything is in the session state - if so, don't need to
    # connect, but if missing stuff, will want to connect
    if not all([x in st.session_state for x in items.keys()]):

        # Create temporary PEM file for setting up the connection
        with NamedTemporaryFile(suffix='.pem') as temp:

            # Write the temporary file
            temp.write(st.secrets.tidb.root_cert.encode('utf-8'))

            # Temporary file have pointer to current position in file - as we
            # have just written, the pointer is at the end of the last write,
            # so if you don't seek, you would read from the end of the file and
            # find nothing
            temp.seek(0)

            # Set up connection manually, providing the temporary PEM file
            # (as cannot use st.connection() without providing tempfile name
            # in secrets)
            conn = pymysql.connect(
                host=st.secrets.tidb.host,
                user=st.secrets.tidb.username,
                password=st.secrets.tidb.password,
                database=st.secrets.tidb.database,
                port=st.secrets.tidb.port,
                ssl_verify_cert=False,
                ssl_verify_identity=False,
                ssl_ca=temp.name
            )

            # Loop through each of the items
            for key, value in items.items():

                # Check if it is in the session state, and if not...
                if key not in st.session_state:

                    # Import data from TIDB cloud
                    df = get_df(f'SELECT * FROM {value}', conn)

                    # If dataset is scores with RAG ratings, convert
                    # columns to numeric, and string 'nan' to actual np.nan
                    if key == 'scores_rag':
                        to_fix = ['mean', 'count', 'total_pupils',
                                  'group_n', 'group_wt_mean', 'group_wt_std',
                                  'lower', 'upper']
                        for col in to_fix:
                            df[col] = pd.to_numeric(df[col], errors='ignore')
                        df['rag'] = df['rag'].replace('nan', np.nan)

                    # If dataset is demographic, convert n_responses to numeric
                    if key == 'demographic':
                        df['n_responses'] = pd.to_numeric(df['n_responses'],
                                                          errors='ignore')

                    # If dataset is counts, convert counts to numeric
                    if key == 'counts':
                        df['count'] = pd.to_numeric(df['count'],
                                                    errors='ignore')
                    # Save into the session state
                    st.session_state[key] = df
