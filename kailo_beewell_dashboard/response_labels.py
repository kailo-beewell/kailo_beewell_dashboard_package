'''
Function to create a dictionary of labels for the responses to each question
in the survey
'''


def add_keys(keys, value, dictionary):
    '''
    Add multiple keys with the same value to the dictionary

    Parameters
    -----------
    keys: array
        Array with strings that are keys for the dictionary
    value: string
        Value of each key
    dictionary: dictionary
        To add the keys and values to, and to source them from too
    '''
    dictionary.update(dict.fromkeys(keys, dictionary[value]))


def create_response_label_dict():
    '''
    Creates dictionary with labels for each response in each question in the
    standard #BeeWell survey and council data.

    Returns
    -------
    labels : dictionary
        Dictionary where key is a topic name or group, and then key is another
        dictionary where key is numeric answer and value is the label.
    '''
    # Define the labels to use for different columns
    labels = {
        'year_group': {
            8: 'Year 8',
            10: 'Year 10'
        },
        'fsm': {
            0: 'Non-FSM',
            1: 'FSM'
        },
        'sen': {
            0: 'Non-SEN',
            1: 'SEN'
        },
        'ethnicity': {
            1: 'Ethnic minority',
            2: 'White British'
        },
        'english_additional': {
            0: 'No',
            1: 'Yes'
        },
        'school': {
            1: 'School A',
            2: 'School B',
            3: 'School C',
            4: 'School D',
            5: 'School E',
            6: 'School F',
            7: 'School G'
        },
        'gender': {
            1: 'Girl',
            2: 'Boy',
            3: 'Non-binary',
            4: 'I describe myself in another way',
            5: 'Currently unsure',
            6: 'Prefer not to say'
        },
        'transgender': {
            1: 'Yes',
            2: 'No',
            3: 'Prefer not to say',
            4: 'I describe myself in another way',
            5: 'Not sure',
        },
        'sexual_orientation': {
            1: 'Bi/pansexual',
            2: 'Gay/lesbian',
            3: 'Heterosexual/straight',
            4: 'I describe myself in another way',
            5: 'Currently unsure',
            6: 'Prefer not to say'
        },
        'neurodivergent': {
            1: 'Yes',
            2: 'No',
            3: 'Unsure'
        },
        'birth': {
            1: 'Yes',
            2: 'No',
            3: '''I don't know'''
        },
        'birth_you_age': {
            1: 'Under 1 year old',
            2: '1 year old',
            3: '2 years old',
            4: '3 years old',
            5: '4 years old',
            6: '5 years old',
            7: '6 years old',
            8: '7 years old',
            9: '8 years old',
            10: '9 years old',
            11: '10 years old',
            12: '11 years old',
            13: '12 years old',
            14: '13 years old',
            15: '14 years old',
            16: '15 years old'
        },
        'autonomy': {
            1: '1 - Completely not true',
            2: '2',
            3: '3',
            4: '4',
            5: '5 - Completely true'
        },
        'life_satisfaction': {
            0: '0 - not at all',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10 - completely'
        },
        'optimism_future': {
            1: 'Almost never',
            2: 'Sometimes',
            3: 'Often',
            4: 'Very often',
            5: 'Always'
        },
        'optimism_other': {
            1: 'Not at all like me',
            2: 'A little like me',
            3: 'Somewhat like me',
            4: 'Mostly like me',
            5: 'Very much like me'
        },
        'wellbeing': {
            1: 'None of the time',
            2: 'Rarely',
            3: 'Some of the time',
            4: 'Often',
            5: 'All of the time'
        },
        'esteem': {
            1: 'Strongly agree',
            2: 'Agree',
            3: 'Disagree',
            4: 'Strongly disagree'
        },
        'stress': {
            1: 'Never',
            2: 'Almost Never',
            3: 'Sometimes',
            4: 'Fairly Often',
            5: 'Very Often'
        },
        'appearance_happy': {
            0: '0 - Very unhappy',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5 - Not happy or unhappy',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10 - Very happy',
            11: 'Prefer not to say'
        },
        'appearance_feel': {
            1: 'Strongly agree',
            2: 'Agree',
            3: 'Disagree',
            4: 'Strongly disagree',
            5: 'Prefer not to say'
        },
        'negative': {
            1: 'Never',
            2: 'Sometimes',
            3: 'Always'
        },
        'lonely': {
            1: 'Often or always',
            2: 'Some of the time',
            3: 'Occasionally',
            4: 'Hardly ever',
            5: 'Never'
        },
        'support': {
            1: 'Strongly agree',
            2: 'Agree',
            3: 'Disagree',
            4: 'Strongly disagree'
        },
        'physical_days': {
            0: '0 days',
            1: '1 day',
            2: '2 days',
            3: '3 days',
            4: '4 days',
            5: '5 days',
            6: '6 days',
            7: '7 days'
        },
        'physical_hours': {
            30: 'Around 30 minutes',
            60: 'Around 1 hour',
            90: 'Around 1.5 hours',
            120: 'Around 2 hours or more'
        },
        'free_like': {
            1: 'Almost always',
            2: 'Often',
            3: 'Sometimes',
            4: 'Not often',
            5: 'Almost never'
        },
        # These have been simplified from the actual responses, which were
        # e.g. 1 to less than 2 hours
        'media_hours': {
            1: 'None',
            2: 'Less than 1 hour',
            3: '1 to 2 hours',
            4: '2 to 3 hours',
            5: '3 to 4 hours',
            6: '4 to 5 hours',
            7: '5 to 6 hours',
            8: '6 to 7 hours',
            9: '7 hours or more'
        },
        'sleep': {
            0: 'No',
            1: 'Yes'
        },
        # Space after None else defaults to treat as NaN upon import
        'places_freq': {
            1: 'None ',
            2: 'Limited',
            3: 'Several',
            4: 'Lots'
        },
        'places_barriers': {
            0: 'No',
            1: 'Yes'
        },
        'school_belong': {
            1: 'Not at all',
            2: 'A little',
            3: 'Somewhat',
            4: 'Quite a bit',
            5: 'A lot'
        },
        'relationships': {
            1: '1 - Never',
            2: '2',
            3: '3',
            4: '4',
            5: '5 - Always'
        },
        'talk': {
            0: 'No',
            1: 'Yes'
        },
        'talk_listen': {
            1: 'Not at all',
            2: 'Slightly',
            3: 'Mostly',
            4: 'Fully'
        },
        'talk_helpful': {
            1: 'Not helpful',
            2: 'Somewhat helpful',
            3: 'Very helpful'
        },
        'talk_if': {
            1: 'Very uncomfortable',
            2: 'Uncomfortable',
            3: 'Comfortable',
            4: 'Very comfortable'
        },
        'accept': {
            1: 'Not at all',
            2: 'Slightly',
            3: 'Mostly',
            4: 'Fully'
        },
        'home_happy': {
            0: '0 - Very unhappy',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5 - Not happy or unhappy',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10 - Very happy'
        },
        'care_experience': {
            1: 'Yes',
            0: 'No',
            2: 'Unsure'
        },
        'young_carer': {
            0: 'No',
            1: 'Yes'
        },
        'local_safe': {
            1: 'Very safe',
            2: 'Fairly safe',
            3: 'Fairly unsafe',
            4: 'Very unsafe',
            5: '''Don't know'''
        },
        'local_other': {
            1: 'Strongly agree',
            2: 'Agree',
            3: 'Neither agree nor disagree',
            4: 'Disagree',
            5: 'Strongly disagree'
        },
        'discrim': {
            1: 'Often or always',
            2: 'Some of the time',
            3: 'Occasionally',
            4: 'Hardly ever',
            5: 'Never'
        },
        'belong_local': {
            1: 'Strongly agree',
            2: 'Agree',
            3: 'Disagree',
            4: 'Strongly disagree'
        },
        'wealth': {
            1: 'Richer',
            2: 'Poorer',
            3: 'About the same',
            4: "Don't know"
        },
        'future_options': {
            1: 'Not many',
            2: 'Quite a few',
            3: 'A lot',
            4: 'Unsure'
        },
        'future_interest': {
            1: 'Not interested',
            2: 'A little interested',
            3: 'Quite interested',
            4: 'Very interested',
            5: 'Unsure'
        },
        'future_support': {
            1: 'Not at all',
            2: 'Slightly',
            3: 'Mostly',
            4: 'Fully',
            5: 'Unsure'
        },
        'climate': {
            1: 'Often',
            2: 'Sometimes',
            3: 'Rarely',
            4: 'Never'
        },
        'social': {
            1: 'Not at all',
            2: 'A little',
            3: 'Somewhat',
            4: 'Quite a bit',
            5: 'A lot'
        },
        'bully': {
            1: 'Not at all',
            2: '1-3 times in last 6 months',
            3: '4+ times in last 6 months',
            4: 'A few times a week'
        }
    }

    # Add values for the keys below, so each key has the same set of values
    # (Rather than repeatedly defining them all above)
    add_keys(['birth_parent1', 'birth_parent2', 'birth_you'], 'birth', labels)
    add_keys(['autonomy_pressure', 'autonomy_express', 'autonomy_decide',
              'autonomy_told', 'autonomy_myself', 'autonomy_choice'],
             'autonomy', labels)
    add_keys(['optimism_best', 'optimism_good', 'optimism_work'],
             'optimism_other', labels)
    add_keys(['wellbeing_optimistic', 'wellbeing_useful', 'wellbeing_relaxed',
              'wellbeing_problems', 'wellbeing_thinking', 'wellbeing_close',
              'wellbeing_mind'], 'wellbeing', labels)
    add_keys(['esteem_satisfied', 'esteem_qualities', 'esteem_well',
              'esteem_value', 'esteem_good'], 'esteem', labels)
    add_keys(['stress_control', 'stress_overcome', 'stress_confident',
              'stress_way'], 'stress', labels)
    add_keys(['negative_lonely', 'negative_unhappy', 'negative_like',
              'negative_cry', 'negative_school', 'negative_worry',
              'negative_sleep', 'negative_wake', 'negative_shy',
              'negative_scared'], 'negative', labels)
    add_keys(['support_ways', 'support_look'], 'support', labels)
    add_keys(['places_barriers___1', 'places_barriers___2',
              'places_barriers___3', 'places_barriers___4',
              'places_barriers___5', 'places_barriers___6',
              'places_barriers___7', 'places_barriers___8',
              'places_barriers___9'], 'places_barriers', labels)
    add_keys(['staff_interest', 'staff_believe', 'staff_best', 'staff_listen',
              'home_interest', 'home_believe', 'home_best', 'home_listen'],
             'relationships', labels)
    add_keys(['staff_talk', 'home_talk', 'peer_talk'], 'talk', labels)
    add_keys(['staff_talk_listen', 'home_talk_listen', 'peer_talk_listen'],
             'talk_listen', labels)
    add_keys(['staff_talk_helpful', 'home_talk_helpful', 'peer_talk_helpful'],
             'talk_helpful', labels)
    add_keys(['staff_talk_if', 'home_talk_if', 'peer_talk_if'],
             'talk_if', labels)
    add_keys(['accept_staff', 'accept_home', 'accept_local',
              'accept_peer'], 'accept', labels)
    add_keys(['local_support', 'local_trust', 'local_neighbours',
              'local_places'], 'local_other', labels)
    add_keys(['discrim_race', 'discrim_gender', 'discrim_orientation',
              'discrim_disability', 'discrim_faith'], 'discrim', labels)
    add_keys(['social_along', 'social_time', 'social_support', 'social_hard'],
             'social', labels)
    add_keys(['bully_physical', 'bully_other', 'bully_cyber'], 'bully', labels)

    return labels


def create_symbol_response_label_dict():
    '''
    Creates dictionary with labels for each response in each question in the
    symbol #BeeWell survey and council data.

    Returns
    -------
    labels : dictionary
        Dictionary where key is a topic name or group, and then key is another
        dictionary where key is numeric answer and value is the label.
    '''
    # Define the labels to use for different columns
    labels = {
        'symbol': {
            1: 'Happy',
            2: 'Ok',
            3: 'Sad'
        },
        'gender': {
            0: 'Male',
            1: 'Female'
        },
        'year_group': {
            7: 'Year 7',
            8: 'Year 8',
            9: 'Year 9',
            10: 'Year 10',
            11: 'Year 11'
        },
        'fsm': {
            0: 'Non-FSM',
            1: 'FSM'
        },
        'sen': {
            0: 'Non-SEN',
            1: 'SEN'
        },
        'ethnicity': {
            1: 'Ethnic minority',
            2: 'White British'
        },
        'english_additional': {
            0: 'No',
            1: 'Yes'
        },
        'school': {
            1: 'School A',
            2: 'School B'
        }
    }

    # Add values for the keys below, so each key has the same set of values
    # (Rather than repeatedly defining them all above)
    add_keys(['symbol_family', 'symbol_home', 'symbol_friends',
              'symbol_choice', 'symbol_things', 'symbol_health',
              'symbol_future', 'symbol_school', 'symbol_free',
              'symbol_life'], 'symbol', labels)

    return labels
