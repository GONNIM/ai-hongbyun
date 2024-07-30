import streamlit as st # type: ignore
import pandas as pd
from datetime import datetime, date


# CSV 파일 경로 설정
LOG_FILE = 'visitor_log.csv'


def get_visitor_counts():
    try:
        # CSV 파일 읽기
        df = pd.read_csv(LOG_FILE)
        
        # 'Timestamp' 열을 datetime 형식으로 변환
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # 전체 방문자 수 계산
        total_visitors = len(df)
        
        # 오늘 날짜 계산 (자정으로 설정)
        today = datetime.combine(date.today(), datetime.min.time())
        
        # 오늘 방문자 수 계산
        today_visitors = len(df[df['Timestamp'].dt.floor('d') == today])
        
        return total_visitors, today_visitors
    except FileNotFoundError:
        st.error("로그 파일을 찾을 수 없습니다.")
        return 0, 0
    except pd.errors.EmptyDataError:
        st.error("로그 파일이 비어 있습니다.")
        return 0, 0
    except pd.errors.ParserError:
        st.error("로그 파일을 읽는 중 오류가 발생했습니다.")
        return 0, 0
    

def get_unique_visitor_counts():
    try:
        # CSV 파일 읽기
        df = pd.read_csv(LOG_FILE)
        
        column_name = 'User Key'

        unique_values = df[column_name].unique()
        unique_counts = len(unique_values)

        return unique_counts
    except FileNotFoundError:
        st.error("로그 파일을 찾을 수 없습니다.")
        return 0
    except pd.errors.EmptyDataError:
        st.error("로그 파일이 비어 있습니다.")
        return 0
    except pd.errors.ParserError:
        st.error("로그 파일을 읽는 중 오류가 발생했습니다.")
        return 0
