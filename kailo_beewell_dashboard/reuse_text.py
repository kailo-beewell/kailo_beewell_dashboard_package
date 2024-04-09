'''
Dictionary with large sections of descriptive text - mainly text that is from
the About page (some of which goes on PDF report introduction) - but also
includes caveat about comparisons (from PDF report introduction and from
various pages of dashboard like summary and explore results). These are also
text that are reused between different versions of the dashboard (e.g. standard
and symbol).
'''

reuse_text = {

    # Introduction for the About page
    'about_intro': '''
This page has lots of helpful information about the research projects (Kailo
and #BeeWell), as well as advice on using and accessing this dashboard, and
some background information around young people's wellbeing.''',

    # Description of the Kailo project
    'kailo': '''
Our aim is to help local communities, young people and public service
partnerships better understand and address the root causes (and wider
determinants) of young people's mental health.

We're made up of leading academics, designers and practitioners, dedicated to
working alongside communities in specific localities. Together, we will test
and co-design evidence-based responses (in a 'framework') to these root causes,
over the next four years.

Our model is formed of three key stages:
* **Early Discovery** - here, we build strong and trusted relationships with
local partners with an aim to understand what matters locally thus, forming
communities around youth- and community-centred priorities
* **Deeper Discovery and Codesign** - this stage, which we're in currently,
sees us codesign systemic responses to social determinants.
* **Prototyping, Implementation and Testing** - this is where the learning is
applied, integrating the codesigned responses with the local system,
prototyping them and making iterative refinements along the way.

To find out more about Kailo, check out our site: https://kailo.community/''',

    # Sample (used for public and standard school dashboard)
    'sample': '''
This year, pupils in Years 8 and 10 at **seven secondary schools** from across
North Devon and Torridge completed the standard version of the #BeeWell survey.
A symbol version of the survey was also completed by pupils in Years 7 to 11
from **two non-mainstream schools** in Northern Devon.''',

    # Sample (used for symbol school dashboard)
    'sample_symbol': '''
This years, pupils in Years 7 to 11 at **two non-mainstream schools** in North
Devon and Torridge completed the symbol version of the #BeeWell survey. A
longer, standard version of the survey was also completed by pupils in Years
8 and 10 at **seven mainstream secondary schools** in Northern Devon.''',

    # Content of the standard survey
    'standard_content': '''
The survey contained questions to measure wellbeing and the factors that might
impact it. Survey topics included:
* 🌱 **Feelings about life** - autonomy, life satisfaction, optimism
* 🧍 **Thoughts and feelings about self** - psychological wellbeing,
self-esteem, stress, feelings around appearance
* 😟 **Feeling down** - negative affect, loneliness, supporting own wellbeing
* 🧘‍♂️ **Health and routines** - sleep, physical activity
* 🕰️ **Free time** - social media use, places to go and things to do
* 🧑‍🤝‍🧑 **Relationships** - talking about feelings, acceptance, school
connection, support from staff, support from parents/carers, experiences of
discrimintation, support from friends, relative wealth and bulllying
* 🏠 **Environment** - feelings about home and local area, including future work
and education opportunities, and climate change
* 👨‍👩‍👧‍👦 **Demographics and experiences** - gender, transgender, sexual
orientation, neurodivergence, family background, care experience and young
carers''',

    # Design of standard survey
    'standard_design': '''
The survey delivered in Northern Devon was adapted from the first #BeeWell
survey in Greater Manchester. That survey was developed through engagements
with over 150 young people from 15 different schools to understand what
wellbeing means to young people, what influences their wellbeing, and what
makes them thrive.

In Devon, we have adapted the survey to help it reflect the
priorities of young people in this area. Topics were based on conversations
across North Devon and Torridge with 195 young people and over 100 local actors
including: system leaders, practitioners, and people at 45 organisations
working with young people and broader communities. We have spoken with young
people and school staff in Northern Devon, as well as researchers and public
health professionals, amongst others, to choose, adapt and/or develop
appropriate questions for the survey. We'd like to extend our thanks to
everyone who supported this process.''',

    # Design of the symbol survey
    'symbol_design': '''
The survey delivered in Northern Devon is the same as that first designed and
delivered by the #BeeWell team in Greater Manchester. They worked with staff
in special school settings to co-design a symbol version of the #BeeWell survey
that would be accessible to young people with severe learning difficulties or
profound and multiple learning disabilities. Using The Children's Society's
'Good Childhood Index' for inspiration, they created a 10-item survey using the
Widgit symbol system with simplified response options.''',

    # Other #BeeWell sites
    'other_beewell_sites': '''
#BeeWell surveys have also been completed by pupils at schools in Hampshire,
Greater Manchester, the London borough of Havering, and Milton Keynes.

In 2023-24, **over 38,000 young people** completed a survey, with **nearly 300
schools** having now taken part in #BeeWell.

You can find out more about other sites at https://beewellprogramme.org/.''',

    # Data used to create the dashboard (standard dashboard)
    'standard_data': '''
This dashboard presents the results from pupils at your school who completed
the survey. To give context to these results, we've added comparisons against
pupils from schools across Northern Devon.

The survey responses were combined with data shared by the local authority such
as free school meal eligibility and special education needs to give further
insight into responses.''',

    # Data used to create the dashboard (symbol dashboard)
    'symbol_data': '''
This dashboard presents the results from pupils at your school who completed
the survey.

The survey responses were combined with data shared by the local authority such
as free school meal eligibility and special education needs to give further
insight into responses.''',

    # Data used to create the dashboard (public dashboard)
    'public_data': '''
This dashboard presents results from pupils at mainstream and non-mainstream
schools who completed the survey.

The survey responses were combined with data shared by the local authority such
as free school meal eligibility and special education needs to give further
insight into responses.''',

    # How to use the results from this report
    'how_to_use_results': '''
These data can provide a useful starting point for discussions about the needs
of your school population and priority areas for development and improvement.
It can also be useful in considering areas of strengths and/or helping pupils
reflect on their positive qualities.

Data in your #BeeWell report may be useful in indicating progress against
targets in your School Improvement Plan or help to identify future target
areas. It may help to identify areas of priority for staff training or be used
as context when considering academic data for participating year groups. It can
also be used as independent evidence in the context of an Ofsted inspection.

Finally, young people consulted during the set-up of #BeeWell in Greater
Manchester felt strongly that pupils should be included in discussions around
feedback, particularly to plan activities and approaches to raise awareness of
strengths or difficulties the #BeeWell survey may highlight. They suggested
involving a range of students (not just those involved in school councils) in
planning how to raise awareness about wellbeing and to support the needs of
young people.''',

    # Viewing dashboard on different devices
    'view_devices': '''
Yes - this dashboard will resize so you should be able to access it on a range
of devices (computer/laptop, tablet, phone, etc).''',

    # Will there be support for interpreting and actioning on results?
    'dashboard_support': '''
Yes - Child Outcomes Research Consortium (CORC) has been funded to provide
seminars and 1:1 support to schools in Northern Devon, to help you understand
how to navigate the dashboard, interpret results, and suggest feedback in the
development of action plans. You should receive information about this via
email, but if you have not or have any questions, please contact us at
kailobeewell@dartington.org.uk.''',

    # Context of what already know about YP wellbeing
    'wellbeing_context': '''
* The peak age of onset of mental health difficulties is 14.5 years.<sup>[1]
</sup>
* Mental health and wellbeing in adolescence predicts adult health, labour
market and other important outcomes.<sup>[2]</sup>
* The wellbeing of adolescents has decreased in the last two decades, while the
prevalence of mental health difficulties among them has increased.<sup>[3,4]
</sup>
* A recent international study ranked the UK’s young people fourth from bottom
across nearly 80 countries in terms of life satisfaction.<sup>[5,6]</sup>
* Young people’s mental health and wellbeing can be influenced by multiple
drivers, including their health and routines, hobbies and entertainment,
relationships, school, environment and society, and how they feel about their
future.<sup>[7]</sup>

<p style='font-size: 12px;'>
References:<br>
[1] Solmi, M. et al (2021). Age at onset of mental disorders worldwide:
large-scale meta-analysis of 192 epidemiological studies. Molecular Psychiatry,
Online First. Available at: https://www.nature.com/articles/s41380-021-01161-7
<br>
[2] Goodman A, Joshi H, Nasim B, Tyler C (2015). Social and emotional skills in
childhood and their long-term effects on adult life. London: EIF. Available at:
https://www.eif.org.uk/report/social-and-emotional-skills-in-childhood-and-thei
r-long-term-effects-on-adult-life.<br>
[3] Children’s Society (2021). The Good Childhood Report 2021. London:
Children's Society. Available at: https://www.childrenssociety.org.uk/informati
on/professionals/resources/good-childhood-report-2021<br>
[4] NHS Digital (2021). Mental health of children and young people in England,
2021 – wave 2 follow up to the 2017 survey. London: NHS Digital. Available at:
https://digital.nhs.uk/data-and-information/publications/statistical/mental-hea
lth-of-children-and-young-people-in-england/2021-follow-up-to-the-2017-survey
<br>
[5] Office for Economic Cooperation and Development (2019). Programme for
International Student Assessment (PISA) results. Paris: OECD. Available at:
https://www.oecd.org/publications/pisa-2018-results-volume-iii-acd78851-en.htm
<br>
[6] Marquez J, Long, E (2021). A Global Decline in Adolescents' Subjective
Well-Being: a Comparative Study Exploring Patterns of Change in the Life
Satisfaction of 15-Year-Old Students in 46 Countries. Child Ind Res 14,
1251–1292 (2021). Available at: https://doi.org/10.1007/s12187-020-09788-8<br>
[7] #BeeWell Programme Team (2021). #BeeWell survey. Manchester: University of
Manchester. Available at: https://gmbeewell.org/wp-content/uploads/2021/09/BeeW
ell-Questionnaires-Booklet.pdf</p>'''
}


def caution_comparing(type):
    '''
    Produce section of text providing caution for when making comparisons
    between schools.

    Parameters
    ----------
    type : string
        Whether this is for 'school' or 'area' dashboard

    Returns
    -------
    statement : string
        Text on caution when comparing
    '''
    if type == 'school':
        unit = 'schools'
        participants = 'pupils'
    elif type == 'area':
        unit = 'areas'
        participants = 'young people'
    statement = f'''
Always be mindful when making comparisons between different {unit}. There are
a number of factors that could explain differences in scores (whether you are
above average, average, or below average). These include:

* Random chance ('one-off' findings).
* Differences in the socio-economic characteristics of {participants} and the
areas where they live (e.g. income, education, ethnicity, access to services
and amenities).
* The number of {participants} taking part - {unit} that are much smaller are
more likely to have more "extreme" results (i.e. above or below average),
whilst {unit} with a larger number of {participants} who took part are more
likely to see average results.

It's also worth noting that the score will only include results from
{participants} who completed each of the questions used to calculate that
topic, and so does not include any reflection of results from {participants}
who did not complete some or all of the questions for that topic.
'''
    return statement
