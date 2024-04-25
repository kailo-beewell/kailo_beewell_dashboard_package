"""
Helper functions to produce the About page for each version of the dashboard
"""

from kailo_beewell_dashboard.images import get_image_path
from kailo_beewell_dashboard.reuse_text import reuse_text
from kailo_beewell_dashboard.stylable_container import header_container
import streamlit as st


def symbol_content():
    """
    Descriptions content of symbol survey using combination of text and images
    (hence provided as function, rather than using reuse_text like all the
    other About page sections)
    """
    st.markdown("""The survey contained ten questions which use the Widgit
                symbol system. These were:""")
    # Add the images (they are the same as those used for the survey, but
    # cropped to height of 340 to remove the 'choose one' from each)
    st.image(get_image_path("symbol_survey/family_crop.png"))
    st.image(get_image_path("symbol_survey/home_crop.png"))
    st.image(get_image_path("symbol_survey/friends_crop.png"))
    st.image(get_image_path("symbol_survey/choice_crop.png"))
    st.image(get_image_path("symbol_survey/things_crop.png"))
    st.image(get_image_path("symbol_survey/health_crop.png"))
    st.image(get_image_path("symbol_survey/future_crop.png"))
    st.image(get_image_path("symbol_survey/school_crop.png"))
    st.image(get_image_path("symbol_survey/free_time_crop.png"))
    st.image(get_image_path("symbol_survey/life_crop.png"))
    st.markdown("For each questions, pupils had three response options:")
    st.image(get_image_path("symbol_survey/choose_one.png"))
    cols = st.columns(3)
    with cols[0]:
        st.image(get_image_path("symbol_survey/happy.png"))
    with cols[1]:
        st.image(get_image_path("symbol_survey/ok.png"))
    with cols[2]:
        st.image(get_image_path("symbol_survey/sad.png"))


def create_about_page(dashboard_type):
    """
    Creates the 'About' page on the streamlit dashboard

    Parameters
    ----------
    dashboard_type : string
        Specifies whether this is for 'standard' or 'symbol' school
        dashboard, or for the 'public' area-level dashboard
    """
    # Page title
    st.title("About")
    st.markdown("Test Ellen")
    st.markdown("Test Annalise")

    # Introduction
    st.markdown(reuse_text["about_intro"])

    # Expand toggle
    expand = st.toggle("Toggle to expand all the boxes below", value=False)

    # FAQs about Kailo
    header_container("green_container", "🌿 Kailo", "#D9ECCA")

    # Description of the Kailo project
    with st.expander("What is Kailo?", expanded=expand):
        st.markdown(reuse_text["kailo"])
        st.image(get_image_path("kailo_systems_adapted.png"), use_column_width=True)

    # FAQs about the #BeeWell survey
    header_container("orange_container", "🐝 The #BeeWell survey", "#F7DCC8")

    # Survey sample
    with st.expander("Who took part in the #BeeWell survey in Devon?", expanded=expand):
        if dashboard_type == "symbol":
            st.markdown(reuse_text["sample_symbol"])
        else:
            st.markdown(reuse_text["sample"])
        st.image(get_image_path("northern_devon.png"), use_column_width=True)

    # Survey content, and design of the survey
    if dashboard_type == "public":
        # Public dashboard - survey content
        with st.expander("What topics did the standard survey cover?", expanded=expand):
            st.markdown(reuse_text["standard_content"])
        with st.expander("What topics did the symbol survey cover?", expanded=expand):
            symbol_content()
        # Public dashboard - survey design
        with st.expander("How was the standard survey designed?", expanded=expand):
            st.markdown(reuse_text["standard_design"])
            st.image(get_image_path("canva_people.png"), use_column_width=True)
        with st.expander("How was the symbol survey designed?", expanded=expand):
            st.markdown(reuse_text["symbol_design"])
    else:
        # School dashboards - survey content
        with st.expander("What topics did the survey cover?", expanded=expand):
            if dashboard_type == "standard":
                st.markdown(reuse_text["standard_content"])
            elif dashboard_type == "symbol":
                symbol_content()
        # School dashboards - survey design
        with st.expander("How was the survey designed?", expanded=expand):
            if dashboard_type == "standard":
                st.markdown(reuse_text["standard_design"])
            elif dashboard_type == "symbol":
                st.markdown(reuse_text["symbol_design"])
            st.image(get_image_path("canva_people.png"), use_column_width=True)

    # Other #BeeWell sites
    with st.expander("Where else have these surveys been completed?", expanded=expand):
        st.markdown(reuse_text["other_beewell_sites"])
        st.image(get_image_path("beewell_map.png"), use_column_width=True)

    # FAQs about the dashboard
    header_container("blue_container", "📊 Dashboard", "#D0C9FF")

    # Data used to create the dashboard
    with st.expander("What data has been used in this dashboard?", expanded=expand):
        if dashboard_type == "standard":
            st.markdown(reuse_text["standard_data"])
        elif dashboard_type == "symbol":
            st.markdown(reuse_text["symbol_data"])
        elif dashboard_type == "public":
            st.markdown(reuse_text["public_data"])

    # How to use the results
    with st.expander("How should we use these results?", expanded=expand):
        st.markdown(reuse_text["how_to_use_results"])
        st.image(get_image_path("thinking.png"), use_column_width=True)

    # Accessing the dashboard on different devices
    with st.expander(
        "Can I access this dashboard on different devices?", expanded=expand
    ):
        st.markdown(reuse_text["view_devices"])
        st.image(get_image_path("devices.png"), use_column_width=True)

    # Support with dashboards (for school dashboards only)
    if dashboard_type != "public":
        with st.expander(
            """
Will there be support available for interpreting and actioning on the dashboard
results?""",
            expanded=expand,
        ):
            st.markdown(reuse_text["dashboard_support"])

    # FAQs about wellbeing
    header_container("yellow_container", "😌 Wellbeing", "#FFF3B3")

    # What do we already know?
    with st.expander(
        """
What do we already know about young people's wellbeing?""",
        expanded=expand,
    ):
        st.markdown(reuse_text["wellbeing_context"], unsafe_allow_html=True)
