import streamlit as st # type: ignore
import streamlit.components.v1 as components # type: ignore


# JavaScript를 이용하여 User Agent를 가져오는 HTML/JS 코드
user_agent_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var userAgent = window.navigator.userAgent;
    document.getElementById("user-agent").innerText = userAgent;
    // Streamlit에 User Agent를 보내기 위해 hidden form 사용
    var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", "/user_agent");
    var hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", "user_agent");
    hiddenField.setAttribute("value", userAgent);
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
});
</script>
<div id="user-agent"></div>
"""

# Streamlit 애플리케이션 실행
def main():
    st.title("User Agent Information")
    
    # JavaScript 코드 삽입
    components.html(user_agent_js)

    # User Agent 정보를 Streamlit으로 전달받기
    if 'user_agent' in st.session_state:
        st.write("User Agent:", st.session_state.user_agent)
    else:
        st.write("User Agent를 가져오는 중입니다...")

# Streamlit 요청 핸들러 설정
def user_agent_request_handler():
    import streamlit.web.server.websocket_headers as wsh # type: ignore

    if st._is_running_with_streamlit:
        handler = st.server.get_websocket_handler()
        headers = wsh.get_headers(handler.request)
        user_agent = headers.get("User-Agent", "Unknown")
        st.session_state.user_agent = user_agent
