import streamlit as st # type: ignore
from streamlit.server.server import Server # type: ignore


# User Agent 정보를 얻어오는 함수
def get_user_agent():
    session_infos = Server.get_current()._session_info_by_id.values()
    for session_info in session_infos:
        headers = session_info.ws.request.headers
        if "User-Agent" in headers:
            return headers["User-Agent"]
    return "User Agent not found"


# Streamlit 애플리케이션 실행
def main():
    st.title("User Agent Information")
    user_agent = get_user_agent()
    st.write("User Agent:", user_agent)
