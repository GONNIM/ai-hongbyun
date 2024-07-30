# Import streamlit and pandas
import streamlit as st # type: ignore
import pandas as pd

# Import for API calls
import requests

# Import for navbar
from streamlit_option_menu import option_menu # type: ignore

# Import for dynamic tagging
from streamlit_tags import st_tags, st_tags_sidebar # type: ignore

# Imports for aggrid
from st_aggrid import AgGrid # type: ignore
from st_aggrid.grid_options_builder import GridOptionsBuilder # type: ignore
from st_aggrid.shared import JsCode # type: ignore
from st_aggrid import GridUpdateMode, DataReturnMode # type: ignore

# Import for loading interactive keyboard shortcuts into the app
from dashboard_utils.gui import keyboard_to_url # type: ignore
from dashboard_utils.gui import load_keyboard_class # type: ignore

from visitor_counts import get_visitor_counts, get_unique_visitor_counts
from navigator_counts import get_navigator_counts


# CSV 파일 경로 설정
LOG_FILE = 'visitor_log.csv'
NAVIGATE_FILE = "navigator_log.csv"


def app():
    #######################################################

    # The code below is to control the layout width of the app.
    if "widen" not in st.session_state:
        layout = "centered"
    else:
        layout = "wide" if st.session_state.widen else "centered"

    #######################################################

    # The class below is for adding some formatting to the shortcut button on the left sidebar.
    load_keyboard_class()

    #######################################################

    # Set up session state so app interactions don't reset the app.
    if not "valid_inputs_received" in st.session_state:
        st.session_state["valid_inputs_received"] = False

    #######################################################

    # 전체 방문자 수와 오늘 방문자 수 가져오기
    total_visitors, today_visitors = get_visitor_counts()
    unique_visitors = get_unique_visitor_counts()

    # The code below is to display the menu bar.
    with st.sidebar:
        st.title("Administrator")
        st.divider()
        st.header("Visitor")
        st.write(
            '<span class="kbdx">전체</span> &nbsp;' + str(total_visitors),
            unsafe_allow_html=True
        )
        st.write(
            '<span class="kbdx">오늘</span> &nbsp;' + str(today_visitors),
            unsafe_allow_html=True
        )
        st.header("Unique Visitor")
        st.write(
            '<span class="kbdx">전체</span> &nbsp;' + str(unique_visitors),
            unsafe_allow_html=True
        )
        selected = option_menu(
            "",
            ["User Information", "Chatbot Information", "Chatbot Wake Up", "Go to Intro Page"],
            icons=["bi-info-square-fill", "bi-robot", "bi-diagram-3", "bi-back"],
            menu_icon="",
            default_index=0
        )
    
    if selected == "User Information":
        st.title("⚖️ AI 홍변")
        
        st.caption("")
        st.markdown("### User Information")
        st.caption("")

        # st.checkbox(
        #     "Widen layout",
        #     key="widen",
        #     help="Tick this box to toggle the layout to 'Wide' mode",
        # )

        # st.caption("")

        # CSV 파일 읽기
        df = pd.read_csv(LOG_FILE)

        # The code below is for Ag-grid
        gb = GridOptionsBuilder.from_dataframe(df)
        # enables pivoting on all columns
        gb.configure_default_column(
            enablePivot=True, enableValue=True, enableRowGroup=True
        )
        gb.configure_selection(selection_mode="multiple", use_checkbox=True)
        gb.configure_side_bar()
        gridOptions = gb.build()

        response = AgGrid(
            df,
            gridOptions=gridOptions,
            enable_enterprise_modules=True,
            update_mode=GridUpdateMode.MODEL_CHANGED,
            data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
            height=500,
            fit_columns_on_grid_load=False,
            configure_side_bar=True,
        )

        # The code below is for the download button
        cs, c1 = st.columns([2, 2])

        with cs:
            @st.cache_data
            def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return df.to_csv().encode("utf-8")

            csv = convert_df(df)

            st.download_button(
                label="Download results as CSV",
                data=csv,
                file_name="results.csv",
                mime="text/csv",
            )    
    elif selected == "Chatbot Information":
        st.title("⚖️ AI 홍변")

        st.caption("")
        st.markdown("### Chatbot Information")
        st.caption("")

        # CSV 파일 읽기
        df = pd.read_csv(NAVIGATE_FILE)

        # The code below is for Ag-grid
        gb = GridOptionsBuilder.from_dataframe(df)
        # enables pivoting on all columns
        gb.configure_default_column(
            enablePivot=True, enableValue=True, enableRowGroup=True
        )
        gb.configure_selection(selection_mode="multiple", use_checkbox=True)
        gb.configure_side_bar()
        gridOptions = gb.build()

        response = AgGrid(
            df,
            gridOptions=gridOptions,
            enable_enterprise_modules=True,
            update_mode=GridUpdateMode.MODEL_CHANGED,
            data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
            height=300,
            fit_columns_on_grid_load=False,
            configure_side_bar=True,
        )

        st.write("")

        cnt_chatbot = get_navigator_counts()
        chart_data = pd.DataFrame(
            {
                "Chatbot": ["소득세법", "민법", "형법", "도로교통법", "근로기준법", "개인정보 보호법", "의료법"],
                "Hits": cnt_chatbot
            }
        )
        # st.bar_chart(chart_data, x="Chatbot", y="Hits", horizontal=False)
        st.bar_chart(chart_data.set_index("Chatbot")["Hits"], use_container_width=True)
    elif selected == "Chatbot Wake Up":
        st.title("⚖️ AI 홍변")

        st.caption("")
        st.markdown("### Chatbot Wake Up")
        st.caption("")

        import user_agent
        user_agent.main()

    elif selected == "Go to Intro Page":
        st.session_state.page = "main"
        st.session_state.login_failed = False
        st.session_state.selected_law = None
        st.session_state.show_password_input = False
        st.rerun()



keyboard_to_url(
    key="g",
    url="https://github.com/CharlyWargnier/zero-shot-classifier/blob/main/streamlit_app.py",
)
keyboard_to_url(
    key_code=190,
    url="https://github.dev/CharlyWargnier/zero-shot-classifier/blob/main/streamlit_app.py",
)
