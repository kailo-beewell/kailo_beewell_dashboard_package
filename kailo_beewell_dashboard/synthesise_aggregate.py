'''
Functions which aggregate pupil-level data - as part of several files
which provide functions for synthesis (creation and aggregation) of data
for the dashboard.
'''
import numpy as np
import pandas as pd
import re


def results_by_site_and_group(
        data, agg_func, no_pupils, response_col=None, labels=None,
        group_type='standard', site_col='school_lab'):
    '''
    Aggregate results for all possible sites (schools or areas) and groups
    (setting result to 0 or NaN if no pupils from a particular group are
    present).

    Parameters
    ----------
    data : pandas dataframe
        Pupil-level survey responses, with their school and demographics
    agg_func : function
        Method for aggregating the dataset
    no_pupils: pandas dataframe
        Output of agg_func() where all counts are set to 0 and other results
        set to NaN, to be used in cases where there are no pupils of a
        particular group (e.g. no FSM / SEN / Year 8)
    response_col : list
        Optional argument used when agg_func is aggregate_proportions(). It is
        the list of columns that we want to aggregate.
    labels : dictionary
        Optional argument used when agg_func is aggregate_proportions(). It is
        a dictionary with all possible questions as keys, then values are
        another dictionary where keys are all the possible numeric (or nan)
        answers to the question, and values are relevant label for each answer.
    group_type : string
        Links to the type of demographic groupings performed. Either
        'standard', 'symbol' or 'none' - default is standard.
    site_col: string
        Name of column with site - e.g. 'school_lab' (default), 'msoa'.

    Returns
    -------
    result : pandas DataFrame
        Dataframe where each row has the aggregation results, along with
        the relevant school and pupil groups used in that calculation
    '''

    # Initialise list to store results
    result_list = list()

    # Define the groups that we want to aggregate by - when providing a filter,
    # first value is the name of the category and the second is the variable
    if group_type == 'standard':
        groups = [
            'All',
            ['Year 8', 'year_group_lab'],
            ['Year 10', 'year_group_lab'],
            ['Girl', 'gender_lab'],
            ['Boy', 'gender_lab'],
            ['FSM', 'fsm_lab'],
            ['Non-FSM', 'fsm_lab'],
            ['SEN', 'sen_lab'],
            ['Non-SEN', 'sen_lab']]
    elif group_type == 'symbol':
        groups = [
            'All',
            ['Year 7', 'year_group_lab'],
            ['Year 8', 'year_group_lab'],
            ['Year 9', 'year_group_lab'],
            ['Year 10', 'year_group_lab'],
            ['Year 11', 'year_group_lab'],
            ['Girl', 'gender_lab'],
            ['Boy', 'gender_lab'],
            ['FSM', 'fsm_lab'],
            ['Non-FSM', 'fsm_lab']]
    elif group_type == 'none':
        groups = ['All']

    # For each of the sites (which we know will all be present at least once
    # as we base the site list on the dataset itself)
    sites = data[site_col].dropna().drop_duplicates().sort_values()
    for site in sites:

        # For each the groupings
        for group in groups:

            # Find results for that site. If group is not equal to all,
            # then apply additional filters
            to_agg = data[data[site_col] == site]
            if group != 'All':
                to_agg = to_agg[to_agg[group[1]] == group[0]]

            # If the dataframe is empty (i.e. you applied a filter but there
            # were no students matching that filter) then set to the no_pupils
            # df. Otherwise, aggregate the data using the provided function
            if len(to_agg.index) == 0:
                res = no_pupils.copy()
            else:
                if response_col is None:
                    res = agg_func(to_agg)
                else:
                    res = agg_func(
                        data=to_agg, response_col=response_col, labels=labels)

            # Specify what site it was
            res[site_col] = site

            # Set each group as all, replacing one if filter used
            if group_type != 'none':
                res['year_group_lab'] = 'All'
                res['gender_lab'] = 'All'
                res['fsm_lab'] = 'All'
                if group_type == 'standard':
                    res['sen_lab'] = 'All'
                if group != 'All':
                    res[group[1]] = group[0]

            # Append results to list
            result_list.append(res)

    # Combine all the results into a single dataframe
    result = pd.concat(result_list)
    return result


def aggregate_scores(df):
    '''
    Aggregate the score columns in the provided dataset, finding the mean and
    count of non-NaN

    Parameters:
    -----------
    df : dataframe
        Dataframe with rows for each pupils and containing the score columns

    Returns:
    -------
    res : dataframe
        Dataframe with mean and count for each score
    '''
    # Make a list of the columns that provide a score
    score_col = [col for col in df.columns if col.endswith('_score')]

    res = pd.DataFrame({
        # Find mean for each score column, ignoring NaN
        'mean': df[score_col].mean(),
        # Count non-NaN so we know the number of pupils used in the mea
        'count': df[score_col].count()}).rename_axis('variable').reset_index()
    return res


def convert_boolean(true_list, false_list, mask):
    '''
    Conditionally replace values of boolean list from one list when True and
    another when False.

    Parameters
    ----------
    true_list : list
        Contains values to use if True
    false_list : list
        Contains values to use if False
    mask : list
        Boolean list
    '''
    iter_true = iter(true_list)
    iter_false = iter(false_list)
    return [next(iter_true) if item else next(iter_false) for item in mask]


def aggregate_proportions(data, response_col, labels, hide_low_response=False):
    '''
    Aggregates each of the columns provided by response_col, for the chosen
    dataset.

    This function uses the known possible values for each column, it counts
    occurences of each (inc. number missing) and makes the answer as a single
    dataframe row, where counts and percentages and categories are stored as
    lists within cells of that row. The function returns a dataframe containing
    all of those rows. It is designed to based on all possible values rather
    than only on values present - else e.g. if no-one responded 3, you could
    have a function that just returns counts of responses to 1, 2 and 4, which
    would then create issues when we try and plot the data.

    For the branching question (talking about feelings), the value counts are
    calculated from a subset of the data (as the no response should only be
    from those who branched onto that question, and not those who branched onto
    the other question (or never answered the first branching question)).

    Parameters
    ----------
    data : dataframe
        Dataframe with rows for each pupil and including all the response_col
    response_col : list
        List of columns that we want to aggregate
    labels : dictionary
        Dictionary with all possible questions as keys, then values are another
        dictionary where keys are all the possible numeric (or nan) answers to
        the question, and values are the relevant label for each answer.
    hide_low_response : boolean
        Whether to hide responses when a response option gets less than 10
        responses (rather than norm elsewhere, which is just requiring 10
        responses to the entire item rather than to each response option)

    Returns
    -------
    pd.concat(rows): dataframe
        Dataframe with the aggregate responses to each of the response_col
    '''
    # Initialise list to store rows of the dataframe
    rows = list()

    # Loop through the columns of interest
    for col_lab in response_col:

        # Find the name of the numeric version of the column
        col = col_lab.replace('_lab', '')

        # Identify if column is branching from "yes" to talking with someone
        if any([substring in col for substring in ['talk_listen',
                                                   'talk_helpful']]):
            # Get the prefix (staff, home or peer)
            prefix = re.sub('_talk_listen|_talk_helpful', '', col)
            # Filter the data to only those who said they talked with them
            # (branch)
            data_subset = data[data[f'{prefix}_talk'] == 1]
            # Find value counts
            value_counts = data_subset[col].value_counts(dropna=False)

        # Identify if the column is branching from "no" to talking with someone
        elif 'talk_if' in col:
            # Get the prefix (staff, home or peer)
            prefix = re.sub('_talk_if', '', col)
            # Filter the data to only those who said they didn't talk to them
            # (branch)
            data_subset = data[data[f'{prefix}_talk'] == 0]
            # Find value counts
            value_counts = data_subset[col].value_counts(dropna=False)

        # For any other columns, no subsetting of the data is required
        else:
            # Find value counts
            value_counts = data[col].value_counts(dropna=False)

        # Get all possible category values and labels from dictionary
        cat = list(labels[col].keys())
        cat_lab = list(labels[col].values())

        # Initalise list for storing counts
        counts = []
        # For each of the possible values in labels - if the value was present,
        # extract from the counts series, but if not, set count to 0
        for value in labels[col].keys():
            if value in value_counts.index:
                counts.append(value_counts[value])
            else:
                counts.append(0)

        # Convert list of counts to list of percentages, and create rounded
        # version
        percentages = [(x/sum(counts))*100 for x in counts]

        # If True to hide when individual response options are n<10
        if hide_low_response:
            # Create mask which is TRUE when responses where n>=10 (ignoring
            # final option (non-response) which we don't mind being n<10)
            mask = [x >= 10 for x in counts[:-1]]

            # If all >=10, keep non-response
            if all(mask):
                mask += [True]
            # If any option is <10, also hide non-response (else could deduce)
            else:
                mask += [False]

            # Use mask to set values to NaN
            counts = convert_boolean(
                counts, np.full(len(counts), np.nan), mask)
            percentages = convert_boolean(
                percentages, np.full(len(percentages), np.nan), mask)

        # Create dataframe row using the calculated data
        # Use np.nansum() so it ignores NaN when calculating sum
        df_row = pd.DataFrame({
            'cat': [cat],
            'cat_lab': [cat_lab],
            'count': [counts],
            'percentage': [percentages],
            'measure': col,
            'n_responses': np.nansum(counts)
        })
        # Append to list
        rows.append(df_row)

    # Combine into a single dataframe and return
    return pd.concat(rows)


def aggregate_counts(df):
    '''
    Aggregates the provided dataframe by finding the total people in it.

    Parameters
    ----------
    df : Dataframe
        Dataframe with row for each pupil and columns that include the school
        and groups needed by results_by_site_and_group()

    Returns
    -------
    res : Dataframe
        Dataframe with the count of pupils in each school and group
    '''
    res = pd.DataFrame({
        'count': [len(df.index)]
    })
    return res


def aggregate_demographic(data, response_col, labels):
    '''
    Aggregates the demographic data by school and group (seperate to
    results_by_school_and_group() as we want to aggregate by school v.s. all
    others rather than for each school, and as we don't want to break down
    results any further by any demographic characteristics)

    Parameters
    ----------
    data : dataframe
        Dataframe containing pupil-level demographic data
    response_col : array
        List of demographic columns to be aggregated
    labels : dictionary
        Dictionary with response options for each variable

    Returns
    -------
    result : dataframe
        Dataframe with % responses to demographic questions, for each school,
        compared with all other schools
    '''
    # Initialise list to store results
    result_list = list()

    # For each of the schools (which we know will all be present at least once
    # as we base the school list on the dataset itself)
    schools = data['school_lab'].dropna().drop_duplicates().sort_values()
    for school in schools:

        # Add label identifying the school as being the current one or now
        data['school_group'] = np.where(data['school_lab'] == school, 1, 0)

        # Loop through each of those groups (current school vs. other schools)
        for group in [1, 0]:

            # Filter to the group and then aggregate the data
            to_agg = data[data['school_group'] == group]
            res = aggregate_proportions(
                data=to_agg, response_col=response_col, labels=labels,
                hide_low_response=True)

            # Label with the group
            res['school_lab'] = school
            res['school_group'] = group

            # Append results to list
            result_list.append(res)

    # Combine all the results into a single dataframe
    result = pd.concat(result_list)

    # Hide results where n<10 overall (in addition to item-level already done)
    result.loc[result['n_responses'] < 10,
               ['count', 'percentage', 'n_responses']] = np.nan

    # Add labels that can use in figures
    result['school_group_lab'] = np.where(
        result['school_group'] == 1, 'Your school', 'Other schools')

    return result
