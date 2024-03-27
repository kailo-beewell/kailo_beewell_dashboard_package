'''
Functions analysing responses to each question - as part of several files
which provide functions for synthesis (creation and aggregation) of data
for the dashboard.
'''
from collections import defaultdict
import numpy as np
from .response_labels import (
    create_response_label_dict, create_symbol_response_label_dict)
from .synthesise_aggregate import (
    aggregate_proportions, results_by_site_and_group)


def aggregate_standard_responses(df, site_col):
    '''
    Aggregate responses to standard survey (non-demographic), using functions
    including aggregate_proportions() and results_by_site_and_group().

    Parameters
    ----------
    df : dataframe
        Pupil-level survey responses
    site_col : string
        Name of column with site to group by (e.g. 'school_lab', 'site')
    '''
    # Make list of columns that we want to count responses for
    # These are lab columns, but with demographic items removed
    response_col = [col for col in df.columns if (
        col.endswith('_lab') and col not in [
            'school_lab', 'gender_lab', 'transgender_lab',
            'sexual_orientation_lab', 'neurodivergent_lab',
            'birth_parent1_lab', 'birth_parent2_lab', 'birth_you_lab',
            'birth_you_age_lab', 'young_carer_lab', 'care_experience_lab',
            'year_group_lab', 'fsm_lab', 'sen_lab', 'ethnicity_lab',
            'english_additional_lab'])]

    # Import dictionary which contains the response options for each question,
    # for which we want to know the answers to
    labels = create_response_label_dict()

    # Add 'NaN': 'No response' to each of the dictionaries
    # They are stored as dictionary of dictionaries, so we loop through and
    # update each one
    for key, value in labels.items():
        value.update({np.nan: 'No response'})

    # Create version where every question has count 0, to use when there is no
    # pupils of a particular group (ie. no-one in certain FSM/SEN/gender/year)
    no_pupils = aggregate_proportions(
        data=df, response_col=response_col, labels=labels)
    no_pupils[['count', 'percentage', 'n_responses']] = 0

    # Find results of aggregation for each pupil group
    result = results_by_site_and_group(
        data=df, agg_func=aggregate_proportions, no_pupils=no_pupils,
        response_col=response_col, labels=labels, group_type='standard',
        site_col=site_col)

    # Hide results where n<10
    result.loc[result['n_responses'] < 10,
               ['count', 'percentage', 'n_responses']] = np.nan

    return result


def aggregate_symbol_responses(df, site_col):
    '''
    Aggregate responses to symbol survey (non-demographic), using functions
    including aggregate_proportions() and results_by_site_and_group().

    Parameters
    ----------
    df : dataframe
        Pupil-level survey responses
    site_col : string
        Name of column with site to group by (e.g. 'school_lab', 'site')
    '''
    # Make list of columns that we want to count responses for
    # These are lab columns, but with demographic items removed
    response_col = [col for col in df.columns if (
        col.endswith('_lab') and col not in [
            'gender_lab', 'year_group_lab', 'fsm_lab', 'sen_lab',
            'ethnicity_lab', 'english_additional_lab', 'school_lab'])]

    # Import dictionary which contains the response options for each question,
    # for which we want to know the answers to
    labels = create_symbol_response_label_dict()

    # Add 'NaN': 'No response' to each of the dictionaries
    # They are stored as dictionary of dictionaries, so we loop through and
    # update each one
    for key, value in labels.items():
        value.update({np.nan: 'No response'})

    # Create version where every question has count 0, to use when a school has
    # no pupils of a particular subgroup (i.e. no-one in certain
    # FSM/SEN/gender/year)
    no_pupils = aggregate_proportions(
        data=df, response_col=response_col, labels=labels)
    no_pupils[['count', 'percentage', 'n_responses']] = 0

    # Find results of aggregation for each pupil group
    result = results_by_site_and_group(
        data=df, agg_func=aggregate_proportions, no_pupils=no_pupils,
        response_col=response_col, labels=labels, group_type='symbol',
        site_col=site_col)

    # Hide results where n<10
    result.loc[result['n_responses'] < 10,
               ['count', 'percentage', 'n_responses']] = np.nan

    return result


def add_keys(groups, value, keys):
    '''
    Add multiple keys with the same value to the dictionary

    Parameters
    ----------
    groups: defaultdict
        Dictionary with measure as key and group as value
    value : string
        Value for all the keys
    keys : array
        Array with the keys
    '''
    groups.update(dict.fromkeys(keys, value))


def add_standard_topic_groups(df):
    '''
    Adds a 'group' column providing topic group for each item in 'measure',
    for the standard survey responses

    Parameters
    ----------
    df : Dataframe
        Dataframe containing 'measure' column, which we want to add 'group'
        column to
    '''
    # Initialise dictionary of groups
    groups = defaultdict(str)

    # Specify group for each measure, adding to the groups dictionary
    add_keys(groups, 'autonomy', [
        'autonomy_pressure',
        'autonomy_express',
        'autonomy_decide',
        'autonomy_told',
        'autonomy_myself',
        'autonomy_choice'])
    add_keys(groups, 'life_satisfaction', ['life_satisfaction'])
    add_keys(groups, 'optimism', [
        'optimism_future',
        'optimism_best',
        'optimism_good',
        'optimism_work'])
    add_keys(groups, 'wellbeing', [
        'wellbeing_optimistic',
        'wellbeing_useful',
        'wellbeing_relaxed',
        'wellbeing_problems',
        'wellbeing_thinking',
        'wellbeing_close',
        'wellbeing_mind'])
    add_keys(groups, 'esteem', [
        'esteem_satisfied',
        'esteem_qualities',
        'esteem_well',
        'esteem_value',
        'esteem_good'])
    add_keys(groups, 'stress', [
        'stress_control',
        'stress_overcome',
        'stress_confident',
        'stress_way'])
    add_keys(groups, 'appearance', ['appearance_happy', 'appearance_feel'])
    add_keys(groups, 'negative', [
        'negative_lonely',
        'negative_unhappy',
        'negative_like',
        'negative_cry',
        'negative_school',
        'negative_worry',
        'negative_sleep',
        'negative_wake',
        'negative_shy',
        'negative_scared'])
    add_keys(groups, 'lonely', ['lonely'])
    add_keys(groups, 'support', ['support_ways', 'support_look'])

    add_keys(groups, 'sleep', ['sleep'])
    add_keys(groups, 'physical', ['physical_days', 'physical_hours'])
    add_keys(groups, 'free_like', ['free_like'])
    add_keys(groups, 'media', ['media_hours'])
    add_keys(groups, 'places', [
        'places_freq',
        'places_barriers___1',
        'places_barriers___2',
        'places_barriers___3',
        'places_barriers___4',
        'places_barriers___5',
        'places_barriers___6',
        'places_barriers___7',
        'places_barriers___8',
        'places_barriers___9'])
    add_keys(groups, 'school_belong', ['school_belong'])
    add_keys(groups, 'staff_relationship', [
        'staff_interest', 'staff_believe', 'staff_best', 'staff_listen'])

    add_keys(groups, 'talk', [
        'staff_talk', 'staff_talk_listen',
        'staff_talk_helpful', 'staff_talk_if',
        'home_talk', 'home_talk_listen', 'home_talk_helpful', 'home_talk_if',
        'peer_talk', 'peer_talk_listen', 'peer_talk_helpful', 'peer_talk_if'])
    add_keys(groups, 'accept', [
        'accept_staff', 'accept_home', 'accept_local', 'accept_peer'])

    add_keys(groups, 'home_relationship', [
        'home_interest', 'home_believe', 'home_best', 'home_listen'])
    add_keys(groups, 'home_happy', ['home_happy'])

    add_keys(groups, 'local_env', [
        'local_safe', 'local_support', 'local_trust', 'local_neighbours',
        'local_places'])
    add_keys(groups, 'discrim', [
        'discrim_race', 'discrim_gender', 'discrim_orientation',
        'discrim_disability', 'discrim_faith'])
    add_keys(groups, 'belong_local', ['belong_local'])
    add_keys(groups, 'wealth', ['wealth'])
    add_keys(groups, 'future', ['future_options', 'future_interest',
                                'future_support'])
    add_keys(groups, 'climate', ['climate'])
    add_keys(groups, 'social', [
        'social_along', 'social_time', 'social_support', 'social_hard'])
    add_keys(groups, 'bully', ['bully_physical', 'bully_other', 'bully_cyber'])

    # Add groups to the dataframe
    df['group'] = df['measure'].map(groups)
    return df


def add_standard_response_labels(df):
    '''
    Adds labels for each of the survey questions (non-demographic) in the
    standard survey

    Parameters
    ----------
    df : dataframe
        Dataframe containing 'measure' column which we want to add labels to
    '''
    # Define labels
    labels = {
        'autonomy_pressure': '''
I feel pressured in my life''',
        'autonomy_express': '''
I generally feel free to express my ideas and opinions''',
        'autonomy_decide': '''
I feel like I am free to decide for myself how to live my life''',
        'autonomy_told': '''
In my daily life I often have to do what I am told''',
        'autonomy_myself': '''
I feel I can pretty much be myself in daily situations''',
        'autonomy_choice': '''
I have enough choice about how I spend my time''',
        'life_satisfaction': '''
Overall, how satisfied are you with your life nowadays?''',
        'optimism_future': '''
I am optimistic about my future''',
        'optimism_best': '''
In uncertain times, I expect the best''',
        'optimism_good': '''
I think good things are going to happen to me''',
        'optimism_work': '''
I believe that things will work out, no matter how difficult they seem''',
        'wellbeing_optimistic': '''
I've been feeling optimistic about the future''',
        'wellbeing_useful': '''
I've been feeling useful''',
        'wellbeing_relaxed': '''
I've been feeling relaxed''',
        'wellbeing_problems': '''
I've been dealing with problems well''',
        'wellbeing_thinking': '''
I've been thinking clearly''',
        'wellbeing_close': '''
I've been feeling close to other people''',
        'wellbeing_mind': '''
I've been able to make up my own mind about things''',
        'esteem_satisfied': '''
On the whole, I am satisfied with myself''',
        'esteem_qualities': '''
I feel that I have a number of good qualities''',
        'esteem_well': '''
I am able to do things as well as most other people''',
        'esteem_value': '''
I am a person of value''',
        'esteem_good': '''
I feel good about myself''',
        'stress_control': '''
Felt you were unable to control the important things in your life''',
        'stress_overcome': '''
Felt that difficulties were piling up so high that you could not overcome
them''',
        'stress_confident': '''
Felt confident about your ability to handle your personal problems''',
        'stress_way': '''
Felt that things were going your way''',
        'appearance_happy': '''
How happy are you with your appearance (the way that you look)?''',
        'appearance_feel': '''
My appearance affects how I feel about myself''',
        'negative_lonely': '''
I feel lonely''',
        'negative_unhappy': '''
I am unhappy''',
        'negative_like': '''
Nobody likes me''',
        'negative_cry': '''
I cry a lot''',
        'negative_school': '''
I worry when I am at school''',
        'negative_worry': '''
I worry a lot''',
        'negative_sleep': '''
I have problems sleeping''',
        'negative_wake': '''
I wake up in the night''',
        'negative_shy': '''
I am shy''',
        'negative_scared': '''
I feel scared''',
        'lonely': '''
How often do you feel lonely?''',
        'support_ways': '''
I have ways to support myself (e.g. to cope, or help myself feel better)''',
        'support_look': '''
I know where to look for advice on how to support myself''',
        'sleep': '''
Is the amount of sleep you normally get enough for you to feel awake and
concentrate on your school work during the day?''',
        'physical_days': '''
How many days in a usual week are you physically active?''',
        'physical_hours': '''
How long on average do you spend being physically active?''',
        'free_like': '''
How often can you do things that you like in your free time?''',
        'media_hours': '''
On a normal weekday during term time, how much time do you spend on social
media?''',
        'places_freq': '''
How many activities/places are there in your local area, that you choose to or
would want to go to in your free time?''',
        'places_barriers___1': '''
There's nothing to do''',
        'places_barriers___2': '''
I'm unable to get there and back''',
        'places_barriers___3': '''
It's too expensive (to get there or take part)''',
        'places_barriers___4': '''
Poor weather''',
        'places_barriers___5': '''
I have no-one to go with''',
        'places_barriers___6': '''
It's too busy''',
        'places_barriers___7': '''
I feel uncomfortable/anxious about other people who might be there''',
        'places_barriers___8': '''
My parents/carers don't allow me to go''',
        'places_barriers___9': '''
Other''',
        'school_belong': '''
I feel that I belong/belonged at my school''',
        'staff_interest': '''
At school there is an adult who... is interested in my schoolwork''',
        'staff_believe': '''
At school there is an adult who... believes that I will be a success''',
        'staff_best': '''
At school there is an adult who... wants me to do my best''',
        'staff_listen': '''
At school there is an adult who... listens to me when I have something to
say''',
        'staff_talk': '''
Talked about feeling down with... an adult at school''',
        'staff_talk_listen': '''
Did you feel listened to when you spoke with... an adult at school''',
        'staff_talk_helpful': '''
Did you receive advice that you found helpful from... an adult at school''',
        'staff_talk_if': '''
How would you feel about speaking with... an adult at school''',
        'accept_staff': '''
Adults at your school''',
        'home_interest': '''
At home there is an adult who... is interested in my schoolwork''',
        'home_believe': '''
At home there is an adult who... believes that I will be a success''',
        'home_best': '''
At home there is an adult who... wants me to do my best''',
        'home_listen': '''
At home there is an adult who... listens to me when I have something to say''',
        'home_talk': '''
Talked about feeling down with... one of your parents/carers''',
        'home_talk_listen': '''
Did you feel listened to when you spoke with... one of your parents/carers''',
        'home_talk_helpful': '''
Did you receive advice that you found helpful from... one of your
parents/carers''',
        'home_talk_if': '''
How would you feel about speaking with... one of your parents/carers''',
        'accept_home': '''
Your parents/carers''',
        'home_happy': '''
How happy are you with the home that you live in?''',
        'local_safe': '''
How safe do you feel when in your local area?''',
        'local_support': '''
People around here support each other with their wellbeing''',
        'local_trust': '''
You can trust people around here''',
        'local_neighbours': '''
I could ask for help or a favour from neighbours''',
        'local_places': '''
There are good places to spend your free time (e.g., leisure centres, parks,
shops)''',
        'discrim_race': '''
How often do people make you feel bad because of... your race, skin colour or
where you were born?''',
        'discrim_gender': '''
How often do people make you feel bad because of... your gender?''',
        'discrim_orientation': '''
How often do people make you feel bad because of... your sexual
orientation?''',
        'discrim_disability': '''
How often do people make you feel bad because of... disability?''',
        'discrim_faith': '''
How often do people make you feel bad because of... your religion/faith?''',
        'belong_local': '''
I feel like I belong in my local area''',
        'accept_local': '''
People in your local area''',
        'wealth': '''
Compared to your friends, is your family richer, poorer or about the same?''',
        'future_options': '''
How many options are available?''',
        'future_interest': '''
How do you feel about the options available?''',
        'future_support': '''
Do you feel (or think you would feel) supported to explore options that
interest you, even if no-one else around you has done them before?''',
        'climate': '''
How often do you worry about the impact of climate change on your future?''',
        'social_along': '''
I get along with people around me''',
        'social_time': '''
People like to spend time with me''',
        'social_support': '''
I feel supported by my friends''',
        'social_hard': '''
My friends care about me when times are hard (for example if I am sick or have
done something wrong)''',
        'bully_physical': '''
How often do you get physically bullied at school? By this we mean getting hit,
pushed around, threatened, or having belongings stolen.''',
        'bully_other': '''
How often do you get bullied in other ways at school? By this we mean insults,
slurs, name calling, threats, getting left out or excluded by others, or having
rumours spread about you on purpose.''',
        'bully_cyber': '''
How often do you get cyber-bullied? By this we mean someone sending mean text
or online messages about you, creating a website making fun of you, posting
pictures that make you look bad online, or sharing them with others.''',
        'peer_talk': '''
Talked about feeling down with... another person your age''',
        'peer_talk_listen': '''
Did you feel listened to when you spoke with... another person your age''',
        'peer_talk_helpful': '''
Did you receive advice that you found helpful from... another person your
age''',
        'peer_talk_if': '''
How would you feel about speaking with... another person your age''',
        'accept_peer': '''
Other people your age'''}

    # Add labels to the dataframe
    df['measure_lab'] = df['measure'].map(labels)
    return df


def add_symbol_response_labels(df):
    '''
    Adds labels for each of the survey questions (non-demographic) in the
    symbol survey

    Parameters
    ----------
    df : dataframe
        Dataframe containing 'measure' column which we want to add labels to
    '''
    # Define labels
    labels = {
        'symbol_family': 'How do you feel about your family?',
        'symbol_home': 'How do you feel about your home?',
        'symbol_friends': 'How do you feel about your friends?',
        'symbol_choice': (
            'How do you feel about how much choice you have in life?'),
        'symbol_things': 'How do you feel about the things that you have?',
        'symbol_health': 'How do you feel about your health?',
        'symbol_future': 'How do you feel about your future?',
        'symbol_school': 'How do you feel about your school?',
        'symbol_free': 'How do you feel about your free time?',
        'symbol_life': 'How do you feel about your life?'}
    # Add labels to the dataframe
    df['measure_lab'] = df['measure'].map(labels)
    return df
