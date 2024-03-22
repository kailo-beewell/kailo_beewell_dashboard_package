'''
Functions to support mapping and the exploration of results by area page
'''
from kailo_beewell_dashboard.explore_results import (
    create_topic_dict)
from kailo_beewell_dashboard.page_setup import blank_lines
from kailo_beewell_dashboard.stylable_container import stylable_container
from kailo_beewell_dashboard.summary_rag import rag_intro_column
import streamlit as st


def area_intro():
    '''
    Produce title, introduction, and RAG key for area results page
    '''
    st.title('Standard survey')

    blank_lines(1)
    # view = st.selectbox('What would you like to view?', [
    #     'Explore results by area',
    #     'Explore results by characteristics',
    #     'Who took part?'])
    # blank_lines(2)

    st.subheader('Introduction')
    st.markdown('''
This page shows how the results from young people varied across Northern Devon
by Middle Layer Super Output Area (MSOA).''')

    # Write interpretation of each of the RAG boxes
    rag_descrip_below = '''
This means that the average scores for young people in that MSOA are **worse**
than average scores for young people in other MSOAs.'''
    rag_descrip_average = '''
This means that the average scores for young people in that MSOA are
**similar** than average scores for young people in other MSOAs.'''
    rag_descrip_above = '''
This means that the average scores for young people in that MSOA are **better**
than average scores for young people in other MSOAs.'''
    rag_descrip_small = '''
This means that **less than ten** young people in an MSOA that completed the
questions for this topic, so the results cannot be shown.'''

    rag_intro_column('below', rag_descrip_below)
    rag_intro_column('average', rag_descrip_average)
    rag_intro_column('above', rag_descrip_above)

    # Custom for n<10 as uses different colour to summary
    cols = st.columns(2)
    with cols[0]:
        with stylable_container(
            key='small',
            css_styles=f'''
        {{
            background-color: {'#f6faff'};
            border-radius: 0.5rem;
            padding: 0px
        }}''',):
            blank_lines(1)
            st.markdown(
                '''<p style='text-align: center; color: #6B7787;'>n<10 </p>''',
                unsafe_allow_html=True)
            blank_lines(1)
    with cols[1]:
        st.markdown(rag_descrip_small)


# INTEGRATE THIS WITH STANDARD SURVEY AND PUBLIC BY CHARACTERISTIC AS BOTH
# USING SIMILAR CODE TO THIS
def choose_topic(df):
    '''
    Create topic dictionary and produce selectbox for users to choose a topic

    Parameters
    ----------
    df : Dataframe
        Dataframe which includes oclumns with topic names

    Returns
    -------
    chosen_variable_lab : String
        Full and capitalised topic name
    '''
    # Create dictionary of topics
    topic_dict = create_topic_dict(df)

    # If session state doesn't contain chosen variable, default to Autonomy
    # If it does (i.e. set from Summary page), use that
    if 'chosen_variable_lab' not in st.session_state:
        st.session_state['chosen_variable_lab'] = 'Autonomy'

    # Convert topics to list and find index of the session state variable
    topic_list = list(topic_dict.keys())
    default = topic_list.index(st.session_state['chosen_variable_lab'])

    # Select topic
    chosen_variable_lab = st.selectbox(
        '**Topic:**', topic_dict.keys(), index=default)

    # Convert from variable_lab to variable
    # chosen_variable = topic_dict[chosen_variable_lab]

    return chosen_variable_lab
