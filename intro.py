import streamlit as st  # type: ignore

from style import style_main
from visitor_log import log_visitor_info
from navigator_log import log_navigator_info


API_KEY = st.secrets["API_KEY"]
USER_KEY = st.secrets["USER_KEY"]
LOGIN_PW = st.secrets["LOGIN_PW"]

if 'user_key' not in st.session_state:
    st.session_state.user_key = None

# Initialize Session
if 'page' not in st.session_state:
    st.session_state.page = "main"

if 'login_failed' not in st.session_state:
    st.session_state.login_failed = False

# Initialize
if 'selected_law' not in st.session_state:
    st.session_state.selected_law = None

# Page Config
st.set_page_config(page_title="AI 홍변", page_icon="⚖️", layout="wide")


def go_to_admin():
    st.session_state.page = "admin"


def check_password():
    s_password = st.session_state.password
    if s_password == API_KEY or s_password == USER_KEY or s_password == LOGIN_PW:
        go_to_admin()
        st.rerun()
    else:
        st.session_state.login_failed = True


if st.session_state.page == "main":
    # Title
    st.title("⚖️ AI 홍변")

    # 방문자 정보 기록 호출
    st.session_state.user_key = log_visitor_info()

    # Header Section
    st.markdown(style_main, unsafe_allow_html=True)

    # Chatbot List Section
    laws = {
        "소득세법": {
            "description": "소득세법에 관한 모든 것을 답변해 드립니다.",
            "link": "https://stevehong-law-tax.streamlit.app/",
            "link_2": "https://ai-hongbyun-tax.streamlit.app/"
        },
        "민법": {
            "description": "계약, 소유, 상속, 채무 등 다양한 개인 권리와 의무에 관해 자세히 알려드립니다.",
            "link": "https://stevehong-law-civil.streamlit.app/",
            "link_2": ""
        },
        "형법": {
            "description": "다양한 범죄와 그에 따른 처벌, 자기 방어, 개인의 권리와 보호에 관해 자세히 알려드립니다.",
            "link": "https://stevehong-law-criminal.streamlit.app/",
            "link_2": ""
        },
        "도로교통법": {
            "description": "도로교통법상의 다양한 규정과 그에 따른 처벌, 운전자의 권리와 의무, 교통사고 발생 시 대처 방법 등에 대해 자세히 알려드립니다.",
            "link": "https://stevehong-law-traffic.streamlit.app/",
            "link_2": ""
        },
        "근로기준법": {
            "description": "근로기준법상의 다양한 규정과 그에 따른 처벌, 노동자의 권리와 의무, 근로 조건 위반 시 대처 방법 등에 대해 자세히 알려드립니다.",
            "link": "https://stevehong-law-labor.streamlit.app/",
            "link_2": ""
        },
        "개인정보 보호법": {
            "description": "개인정보 보호법상의 다양한 규정과 그에 따른 처벌, 개인정보 주체의 권리와 의무, 개인정보 유출 시 대처 방법 등에 대해 자세히 알려드립니다.",
            "link": "https://stevehong-law-privacy.streamlit.app/",
            "link_2": ""
        },
        "의료법": {
            "description": "의료법상의 다양한 규정과 그에 따른 처벌, 환자의 권리와 의무, 의료사고 발생 시 대처 방법 등에 대해 자세히 알려드립니다.",
            "link": "https://stevehong-law-medical.streamlit.app/",
            "link_2": ""
        }
    }

    # 7-column layout
    selected_law = None
    columns = st.columns(7)

    for i, (law, info) in enumerate(laws.items()):
        if columns[i].button(law, key=law):
            st.session_state.selected_law = law
            st.rerun()

    if st.session_state.selected_law:
        selected_law = st.session_state.selected_law
        law_info = laws[selected_law]
        
        law_card = f"""
        <div class="law-card">
            <div class="law-name">{selected_law}</div>
            <div class="law-description">{law_info['description']}</div>
            <a href="{law_info['link']}" target="_blank" class="law-link">⚖️ AI 홍변 - {selected_law} 챗봇 열기</a>
        </div>
        """
        if law_info['link_2']:
            law_card = f"""
            <div class="law-card">
                <div class="law-name">{selected_law}</div>
                <div class="law-description">{law_info['description']}</div>
                <a href="{law_info['link_2']}" target="_blank" class="law-link">⚖️ AI 홍변 (Season 2) - {selected_law} 챗봇 열기</a>
            </div>
            """
    else:
        law_card = f"""
        <div class="law-card">
            <div class="law-name">상단의 법령을 선택해 주세요!</div>
            <div class="law-description">무엇이든 물어보세요!</div>
            <a href="#" target="_self" class="law-link">⚖️ AI 홍변</a>
        </div>
        """

    if st.markdown(law_card, unsafe_allow_html=True):
        if selected_law:
            result = log_navigator_info(selected_law, law_info)

    # Footer
    st.write("")
    st.markdown('<div class="footer"><p>© 2024 AI 홍변</p></div>', unsafe_allow_html=True)

    st.divider()

    if st.button("Go to Admin Page"):
        st.session_state.show_password_input = True

        if st.session_state.show_password_input:
            st.text_input('Enter Password', type='password', key='password')
            st.button('Submit', on_click=check_password)

    if st.session_state.login_failed:
        st.error('Incorrect password, please try again.')
elif st.session_state.page == "admin":
    import admin
    admin.app()
