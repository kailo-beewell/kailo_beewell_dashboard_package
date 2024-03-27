'''
Helper functions for the 'Who took part' section of the dashboard and report
'''
from markdown import markdown
import streamlit as st
from .reshape_data import extract_nested_results
from .bar_charts import survey_responses
from .bar_charts_text import create_response_description


def create_demographic_page_intro(school_size, output='streamlit'):
    '''
    Creates the title and introductory paragraph for the 'Who took part'
    demographic section of the dashboard/report

    Parameters
    ----------
    school_size : integer
        Total number of pupils who completed at least one question at school
    output : string
        Specifies whether to write for 'streamlit' (default) or 'pdf'.

    Returns
    -------
    html_string : string
        Optional return, used when output=='pdf', contains HTML for report.
    '''
    # Title
    title = 'Who took part?'

    # Introductory paragraph
    if output == 'streamlit':
        type = 'page'
    elif output == 'pdf':
        type = 'section'
    description = f'''
There were {school_size} pupils at your school who took part in the #BeeWell
survey. This {type} describes the sample of pupils who completed the survey.'''

    # Write to streamlit dashboard
    if output == 'streamlit':
        st.title(title)
        st.markdown(description)
    # Write to PDF report
    elif output == 'pdf':
        html_string = f'''
<div class='page'>
    <div class='section_container'>
        <h1 style='page-break-before:always;' id='who_took_part'>{title}</h1>
        <p>{description}</p>
    </div>
</div>'''
        return html_string


def demographic_headers(survey_type='standard'):
    '''
    Creates dictionary of headers for the demographic section

    Parameters
    ----------
    survey_type : string
        Specifies whether this is for standard or symbol survey dashboard

    Returns
    -------
    header_dict : dictionary
        Dictionary where key is a variable name, and value is the header
    '''
    if survey_type == 'standard':
        header_dict = {
            'year_group': 'Year group',
            'fsm': 'Eligible for free school meals (FSM)',
            'gender': 'Gender and transgender',
            'sexual_orientation': 'Sexual orientation',
            'care_experience': 'Care experience',
            'young_carer': 'Young carers',
            'neuro': 'Special educational needs and neurodivergence',
            'ethnicity': 'Ethnicity',
            'english_additional': 'English as an additional language',
            'birth': 'Background'}
    elif survey_type == 'symbol':
        header_dict = {
            'gender': 'Gender',
            'year_group': 'Year group',
            'fsm': 'Eligible for free school meals (FSM)',
            'ethnicity': 'Ethnicity',
            'english_additional': 'English as an additional language'}
    return header_dict


def demographic_plots(
        dem_prop, chosen_school=None, chosen_group=None,
        group_lab='school_group_lab', output='streamlit', content=None,
        survey_type='standard', dashboard_type='school'):
    '''
    Creates the plots for the Who Took Part page/section, with the relevant
    headers and descriptions, for the streamlit dashboard or PDF report.

    Parameters
    ----------
    dem_prop : dataframe
        Dataframe with proportion of each responses to demographic questions
    chosen_school : string
        Optional input for school dashboard - name of the chosen school
    chosen_group : string
        Optional input for school dashboard - specifies whether to make plots
        'For your school' or 'Compared with other schools in Northern Devon'.
        Will do the latter unless you input 'For your school'.
    group_lab : string
        Name of chosen group  - default is school_group_lab.
    output : string
        Specifies whether to write for 'streamlit' (default) or 'pdf'.
    content : list
        Optional input used when output=='pdf', contains HTML for report.
    survey_type : string
        Specifies whether this is for 'standard' (default) or 'symbol'
        survey dashboard.
    dashboard_type : string
        Specifies whether this is for 'school' (default) or 'area' dashboard.

    Returns
    -------
    content : list
        Optional return, used when output=='pdf', contains HTML for report.
    '''
    # If its for a school dashboard
    if dashboard_type == 'school':
        # Filter to results from current school
        chosen = dem_prop[dem_prop['school_lab'] == chosen_school]
        # If only looking at that school, drop the comparator school group data
        if chosen_group == 'For your school':
            chosen = chosen[chosen['school_group'] == 1]
        # Extract the nested lists in the dataframe
        chosen_result = extract_nested_results(
            chosen=chosen, group_lab=group_lab, plot_group=True)
    # For area dashboard, less pre-processing required...
    else:
        # Extract the nested lists in the dataframe
        chosen_result = extract_nested_results(
            chosen=dem_prop, group_lab=group_lab, plot_group=True)

    # Generate titles and descriptions for the standard survey, and list of
    # header sections
    if survey_type == 'standard':
        # Import descriptions for the charts
        response_descrip = create_response_description()
        # Import headers
        dem_header_dict = demographic_headers(survey_type)
        header_list = dem_header_dict.keys()
    # We don't want section titles and descriptions for the symbol survey
    # so just create list to loop through based on measure names
    elif survey_type == 'symbol':
        header_list = chosen_result['measure'].unique()

    # Loop through each of the groups of plots
    # This plots measures in loops, basing printed text on the measure names
    # and basing the titles of groups on the group names (which differs to the
    # survey responses page, which bases printed text on group names)
    for plot_group in header_list:

        # Add the title for that group for standard survey
        if survey_type == 'standard':
            if output == 'streamlit':
                st.header(dem_header_dict[plot_group])
            elif output == 'pdf':
                content.append(f'''<h1 style='page-break-before:always;'
                            id='{plot_group}'>
                            {dem_header_dict[plot_group]}</h1>''')

        # Find the measures in that group
        measures = chosen_result.loc[
            chosen_result['plot_group'] == plot_group,
            'measure'].drop_duplicates()

        # Loop through the measures
        # Include a counter used for PDF report, as in report we want to
        # break page before description, unless it is the first description
        i = -1
        for measure in measures:
            i += 1

            # Add descriptive text if there is any for standard survey
            if survey_type == 'standard':
                if measure in response_descrip.keys():
                    if output == 'streamlit':
                        st.markdown(response_descrip[measure])
                    elif output == 'pdf':
                        if i > 0:
                            content.append(f'''
    <p style='page-break-before:always;'>{markdown(response_descrip[measure])}
    </p>''')
                        else:
                            content.append(f'''
    <p>{markdown(response_descrip[measure])}</p>''')

            # Filter data for that measure and produce plot
            to_plot = chosen_result[chosen_result['measure'] == measure]
            if output == 'streamlit':
                survey_responses(to_plot, page='demographic')
            elif output == 'pdf':
                content = survey_responses(to_plot, font_size=14, output='pdf',
                                           content=content, page='demographic')

    if output == 'pdf':
        return content
