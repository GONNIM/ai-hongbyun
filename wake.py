import requests
import time


laws = {
    "소득세법": {
        "description": "소득세법에 관한 모든 것을 답변해 드립니다.",
        "link": "https://stevehong-law-tax.streamlit.app/"
    },
    "민법": {
        "description": "계약, 소유, 상속, 채무 등 다양한 개인 권리와 의무에 관해 자세히 알려드립니다.",
        "link": "https://stevehong-law-civil.streamlit.app/"
    },
    "형법": {
        "description": "다양한 범죄와 그에 따른 처벌, 자기 방어, 개인의 권리와 보호에 관해 자세히 알려드립니다.",
        "link": "https://stevehong-law-criminal.streamlit.app/"
    },
    "도로교통법": {
        "description": "도로교통법상의 다양한 규정과 그에 따른 처벌, 운전자의 권리와 의무, 교통사고 발생 시 대처 방법 등에 대해 자세히 알려드립니다.",
        "link": "https://stevehong-law-traffic.streamlit.app/"
    },
    "근로기준법": {
        "description": "근로기준법상의 다양한 규정과 그에 따른 처벌, 노동자의 권리와 의무, 근로 조건 위반 시 대처 방법 등에 대해 자세히 알려드립니다.",
        "link": "https://stevehong-law-labor.streamlit.app/"
    },
    "개인정보 보호법": {
        "description": "개인정보 보호법상의 다양한 규정과 그에 따른 처벌, 개인정보 주체의 권리와 의무, 개인정보 유출 시 대처 방법 등에 대해 자세히 알려드립니다.",
        "link": "https://stevehong-law-privacy.streamlit.app/"
    },
    "의료법": {
        "description": "의료법상의 다양한 규정과 그에 따른 처벌, 환자의 권리와 의무, 의료사고 발생 시 대처 방법 등에 대해 자세히 알려드립니다.",
        "link": "https://stevehong-law-medical.streamlit.app/"
    }
}

def wake_up_sites():
    for i, (law, info) in enumerate(laws.items()):
        selected_law = law
        law_info = laws[selected_law]

        try:
            response = requests.get(law_info['link'])
            if response.status_code == 200:
                print(f"{time.ctime()}: {selected_law} app is Awake!")
            else:
                print(f"{time.ctime()}: Failed to wake up the {selected_law} app, status code: {response.status_code}")
        except Exception as e:
            print(f"{time.ctime()}: An error occurred at {selected_law}: {e}")

while True:
    selected_law = None
    wake_up_sites()
    time.sleep(600)
