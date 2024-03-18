'''
Function to generate a non-interactive PDF version of the dashboard as a
temporary file that can then be downloaded from the dashboard
'''
import base64
from .images import get_image_path
from importlib.resources import files
from markdown import markdown
import os
from .reshape_data import get_school_size
from .reuse_text import reuse_text
from .summary_rag import summary_intro, summary_table
from .explore_results import (
    create_bar_charts,
    create_explore_topic_page,
    create_topic_dict,
    get_chosen_result,
    write_page_title)
from .who_took_part import (
    create_demographic_page_intro,
    demographic_headers,
    demographic_plots)


def logo_html():
    '''
    Generates HTML string to create logo as displayed on cover page of reports.

    Returns
    -------
    img_tag : string
        HTML to generate the logo
    '''
    # Encode image
    img_path = get_image_path('kailo_beewell_logo_padded.png')
    data_uri = base64.b64encode(open(img_path, 'rb').read()).decode('utf-8')
    # Insert into HTML image tag
    img_tag = f'''
<img src='data:image/png;base64,{data_uri}' alt='Kailo #BeeWell logo'
style='width:300px; height:182px;'>'''
    return img_tag


def illustration_html():
    '''
    Generates DIV element containing illustration as displayed on cover page of
    reports.

    Returns
    -------
    illustration : string
        HTML to generate div containing the illustration
    '''
    # Encode image
    img_path = get_image_path('home_image_3_transparent.png')
    data_uri = base64.b64encode(open(img_path, 'rb').read()).decode('utf-8')
    # Insert into HTML image tag
    img_tag = f'''
<img src='data:image/png;base64,{data_uri}' alt='Kailo illustration'
style='width:650px; height:192px;'>'''
    # Insert into div
    illustration = f'''
<div style='width:100%; position:absolute; bottom:0;'>
    {img_tag}
</div>'''
    return illustration


def structure_report(pdf_title, content):
    '''
    Inserts the provided HTML into the structure of the report - PDF title,
    importing and reading the CSS style, and inserting the content of report

    Parameters
    ----------
    pdf_title : string
        Title for the pdf file
    content : string
        HTML content of the report

    Returns
    -------
    html_content : string
        HTML to produce the styled report
    '''
    # Remove the final temporary image file
    if os.path.exists('report/temp_image.png'):
        os.remove('report/temp_image.png')

    # Import the CSS stylesheet
    css_path = str(files('kailo_beewell_dashboard')
                   .joinpath('css/static_report_style.css'))
    with open(css_path) as css:
        css_style = css.read()

    html_content = f'''
<!DOCTYPE html>
<html>
<head>
    <title>{pdf_title}</title>
    <style>
        {css_style}
    </style>
</head>
<body>
    {''.join(content)}
</body>
</html>
'''
    return html_content


def create_static_report(chosen_school, chosen_group, df_scores, df_prop,
                         counts, dem_prop, pdf_title):
    '''
    Generate a static PDF report for the chosen school and group, with all
    the key information and figures from the dashboard

    Parameters
    ----------
    chosen_school : string
        Name of the chosen school
    chosen_group : string
        Name of the chosen group to view results by - options are
        'For all pupils', 'By year group', 'By gender', 'By FSM' or 'By SEN'
    df_scores : dataframe
        Dataframe with aggregate scores and RAG for each topic
    df_prop : dataframe
        Dataframe with proportion of each response to each survey question
    counts : dataframe
        Dataframe with the counts of pupils at each school
    dem_prop : dataframe
        Dataframe with proportion of each reponse to the demographic questions
    pdf_title : string
        Title for the PDF file
    '''
    ##########
    # Set-up #
    ##########

    # Create empty list to fill with HTML content for PDF report
    content = []

    # Get dictionaries which will use later on and for table of contents
    # Create dictionary of topics
    topic_dict = create_topic_dict(df_scores)
    # Create header dictionary for the demographic section
    dem_header_dict = demographic_headers()

    # Get school size
    school_size = get_school_size(counts, chosen_school)

    ##############
    # Title page #
    ##############

    # Add logo
    content.append(logo_html())

    # Get group name with only first character modified to lower case
    group_lower_first = chosen_group[0].lower() + chosen_group[1:]

    # Title and introduction
    title_page = f'''
<div class='section_container'>
    <h1 style='text-align:center;'>The #BeeWell Survey</h1>
    <p style='text-align:center; font-weight:bold;'>Thank you for taking
    part in the #BeeWell survey delivered by Kailo.</p>
    <p>The results from pupils at your school can be explored using the
    interactive dashboard at
    https://synthetic-beewell-kailo-standard-school-dashboard.streamlit.app/.
    This report has been downloaded from that dashboard.<br><br>
    There are four reports available - these have results: (a) from all
    pupils, (b) by gender, (c) by free school meal (FSM) eligibility, and
    (d) by year group.<br><br>
    This report contains the results <b>{group_lower_first}</b> for
    <b>{chosen_school}</b>.</p>
</div>'''
    content.append(title_page)

    # Add illustration
    content.append(illustration_html())

    ################
    # Introduction #
    ################

    # Heading
    content.append('''<h1 style='page-break-before:always;'>
                   Introduction</h1>''')

    # Using the report (duplicate text with About.py)
    content.append('<h2>How to use this report</h2>')
    content.append(markdown(reuse_text['how_to_use_results']))

    # Comparison warning (duplicate text with Explore results.py)
    content.append('<h2>Comparing between schools</h2>')
    content.append(markdown(reuse_text['caution_comparing']))

    #####################
    # Table of contents #
    #####################

    # Get all of the explore results pages as lines for the table of contents
    explore_results_pages = []
    for key, value in topic_dict.items():
        line = f'''<li><a href='#{value}'>{key}</a></li>'''
        explore_results_pages.append(line)

    # Get the demographic headers as lines for the table of contents
    demographic_pages = []
    for key, value in dem_header_dict.items():
        line = f'''<li><a href='#{key}'>{value}</a></li>'''
        demographic_pages.append(line)

    content.append(f'''
<div>
    <h1 style='page-break-before:always;'>Table of Contents</h1>
    <ul>
        <li><a href='#summary'>Summary</a> - See a simple overview of
            results from pupils at your school, compared with other
            schools</li>
        <br>
        <li><a href='#explore_results'>Explore results</a> - Explore how
            your pupils responded to each survey question, and see further
            information on how the summary page's comparison to other
            schools was generated
            <ul>{''.join(explore_results_pages)}</ul>
        </li>
        <br>
        <li><a href='#who_took_part'>Who took part</a> - See the
            characteristics of the pupils who took part in the survey
            <ul>{''.join(demographic_pages)}</ul>
        </li>
    </ul>
</div>
''')

    ################
    # Summary page #
    ################

    # Summary cover page with guide to RAG ratings
    content.append(summary_intro(school_size, 'pdf'))

    # Summary grid with RAG ratings for each topic
    content = summary_table(
        df_scores, chosen_group, chosen_school, 'pdf', content)

    ###########################
    # Explore results section #
    ###########################

    # Create cover page with title and introduction
    content.append(write_page_title(output='pdf'))

    # Create pages for all of the topics
    for chosen_variable_lab in topic_dict.keys():
        content = create_explore_topic_page(
            chosen_variable_lab, topic_dict, df_scores, chosen_school,
            chosen_group, df_prop, content)

    #########################
    # Who took part section #
    #########################

    # Create cover page with title and introduction
    content.append(create_demographic_page_intro(school_size, 'pdf'))

    # Create pages with plots for each measure
    content = demographic_plots(
        dem_prop=dem_prop, chosen_school=chosen_school,
        chosen_group='Compared with other schools in Northern Devon',
        output='pdf', content=content)

    ######################
    # Create HTML report #
    ######################

    html_content = structure_report(pdf_title, content)

    return html_content


def create_static_symbol_report(
        chosen_school,  df_prop, counts, dem_prop, pdf_title):
    '''
    Generate a static symbol survey PDF report for the chosen school and group,
    with all the key information and figures from the dashboard

    Parameters
    ----------
    chosen_school : string
        Name of the chosen school
    df_prop : dataframe
        Dataframe with proportion of each response to each survey question
    counts : dataframe
        Dataframe with the counts of pupils at each school
    dem_prop : dataframe
        Dataframe with proportion of each reponse to the demographic questions
    pdf_title : string
        Title for the PDF file
    '''
    ##########
    # Set-up #
    ##########
    # Create empty list to fill with HTML content for PDF report
    content = []

    # Create dictionary with groups and labels to use in table of contents
    survey_groups = {'all': 'For all pupils',
                     'year': 'By year group',
                     'gender': 'By gender',
                     'fsm': 'By FSM'}

    # Get school size
    school_size = get_school_size(counts, chosen_school, 'symbol')

    ##############
    # Title page #
    ##############

    # Add logo
    content.append(logo_html())

    # Title and introduction
    title_page = f'''
<div class='section_container'>
    <h1 style='text-align:center;'>The #BeeWell Survey</h1>
    <p style='text-align:center; font-weight:bold;'>Thank you for taking
    part in the #BeeWell survey delivered by Kailo.</p>
    <p>The results from pupils at your school can be explored using the
    interactive dashboard at
    https://synthetic-beewell-kailo-standard-school-dashboard.streamlit.app/.
    This report has been downloaded from that dashboard.<br><br>
    This report contains the results for <b>{chosen_school}</b>.</p>
</div>'''
    content.append(title_page)

    # Add illustration
    content.append(illustration_html())

    ################
    # Introduction #
    ################

    # Heading
    content.append('''<h1 style='page-break-before:always;'>
                   Introduction</h1>''')

    # Using the report (duplicate text with About.py)
    content.append('<h2>How to use this report</h2>')
    content.append(markdown(reuse_text['caution_comparing']))

    #####################
    # Table of contents #
    #####################

    # Get all of the explore results pages as lines for the table of contents
    explore_results_pages = []
    for key, value in survey_groups.items():
        line = f'''<li><a href='#{key}'>{value}</a></li>'''
        explore_results_pages.append(line)

    # Get the demographic headers as lines for the table of contents

    content.append(f'''
<div>
    <h1>Table of Contents</h1>
    <ul>
        <li><a href='#explore_results'>Explore results</a> - Explore how
            your pupils responded to each survey question
            <ul>{''.join(explore_results_pages)}</ul>
        </li>
        <br>
        <li><a href='#who_took_part'>Who took part</a> - See the
            characteristics of the pupils who took part in the survey
        </li>
    </ul>
</div>
''')

    ###########################
    # Explore results section #
    ###########################

    # Create cover page with title and introduction
    content.append(write_page_title(output='pdf', survey_type='symbol'))

    # Create pages with plots for each measure
    chosen_variable = 'symbol'
    df_prop['group'] = chosen_variable
    for key, value in survey_groups.items():
        # Add title for that group
        content.append(f'''
<h2 id='{key}'; style='page-break-before:always;'>Explore
results {value[0].lower() + value[1:]}</h2>''')
        # Get results for that school and group
        chosen_result = get_chosen_result(
            chosen_variable, chosen_group=value, df=df_prop,
            school=chosen_school, survey_type='symbol')
        # Add bar charts to the HTML
        content = create_bar_charts(
            chosen_variable, chosen_result, output='pdf', content=content)

    #########################
    # Who took part section #
    #########################

    # Create cover page with title and introduction
    content.append(create_demographic_page_intro(school_size, 'pdf'))

    # Create pages with plots for each measure
    dem_prop['plot_group'] = dem_prop['measure']
    content = demographic_plots(
        dem_prop=dem_prop, chosen_school=chosen_school,
        chosen_group='For your school', output='pdf', content=content,
        survey_type='symbol')

    ######################
    # Create HTML report #
    ######################

    html_content = structure_report(pdf_title, content)

    return html_content
