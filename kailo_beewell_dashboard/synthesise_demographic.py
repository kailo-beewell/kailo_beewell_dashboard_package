'''
Functions which focus on demographic data - as part of several files
which provide functions for synthesis (creation and aggregation) of data
for the dashboard.
'''
from collections import defaultdict
from .synthesise_responses import add_keys


def add_standard_demographic_groups(df):
    '''
    Adds a 'plot_group' column providing demographic topic group for each item
    in 'measure', for the standard survey demographic responses / data.

    Parameters
    ----------
    df : Dataframe
        Dataframe containing 'measure' column, which we want to add
        'plot_group' column to.
    '''
    # Initialise dictionary of groups
    groups = defaultdict(str)

    # Specify group for each measure, adding to the groups dictionary
    add_keys(groups, 'year_group', ['year_group'])
    add_keys(groups, 'fsm', ['fsm'])
    add_keys(groups, 'ethnicity', ['ethnicity'])
    add_keys(groups, 'english_additional', ['english_additional'])
    add_keys(groups, 'gender', ['gender', 'transgender'])
    add_keys(groups, 'care_experience', ['care_experience'])
    add_keys(groups, 'young_carer', ['young_carer'])
    add_keys(groups, 'neuro', ['sen', 'neurodivergent'])
    add_keys(groups, 'birth', ['birth_parent1', 'birth_parent2',
                               'birth_you', 'birth_you_age'])
    add_keys(groups, 'sexual_orientation', ['sexual_orientation'])

    # Add groups to the dataframe
    df['plot_group'] = df['measure'].map(groups)
    return df


def add_standard_demographic_response_labels(df):
    '''
    Adds labels for each of the demographic survey questions / data in the
    standard survey

    Parameters
    ----------
    df : dataframe
        Dataframe containing 'measure' column which we want to add labels to
    '''
    # Define labels
    labels = {
        'gender': 'Gender',
        'transgender': 'Do you consider yourself to be transgender?',
        'sexual_orientation': 'Sexual orientation',
        'neurodivergent': 'Do you identify as neurodivergent?',
        'young_carer': '''In the last year, have you regularly taken on caring
    responsibilities for a family member - e.g. due to illness, disability,
    mental health condition or drug/alcohol dependency?''',
        'care_experience': '''Are you or have you ever been in care (living in
    a foster placement, residential placement, or private/kinship care)?''',
        'birth_parent1': 'Was birth parent 1 born outside the UK?',
        'birth_parent2': 'Was birth parent 2 born outside the UK?',
        'birth_you': 'Were you born outside the UK?',
        'year_group': 'Year group',
        'fsm': 'Free school meals',
        'sen': 'Special educational needs',
        'ethnicity': 'Ethnicity',
        'english_additional': 'English as an additional language'}

    # Add labels to the dataframe
    df['measure_lab'] = df['measure'].map(labels)
    return df
