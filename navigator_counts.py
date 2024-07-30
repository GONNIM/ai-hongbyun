import streamlit as st # type: ignore
import pandas as pd


# CSV 파일 경로 설정
NAVIGATE_FILE = 'navigator_log.csv'


def get_navigator_counts():
    try:
        # CSV 파일 읽기
        df = pd.read_csv(NAVIGATE_FILE)
        
        column_name = 'Site Name'

        specific_value = '소득세법'
        tax_count = df[df[column_name] == specific_value].shape[0]
        specific_value = "민법"
        civil_count = df[df[column_name] == specific_value].shape[0]
        specific_value = "형법"
        criminal_count = df[df[column_name] == specific_value].shape[0]
        specific_value = "도로교통법"
        traffic_count = df[df[column_name] == specific_value].shape[0]
        specific_value = "근로기준법"
        labor_count = df[df[column_name] == specific_value].shape[0]
        specific_value = "개인정보 보호법"
        privacy_count = df[df[column_name] == specific_value].shape[0]
        specific_value = "의료법"
        medical_count = df[df[column_name] == specific_value].shape[0]

        return [tax_count, civil_count, criminal_count, traffic_count, labor_count, privacy_count, medical_count]
    except FileNotFoundError:
        st.error("로그 파일을 찾을 수 없습니다.")
        return [0, 0, 0, 0, 0, 0, 0]
    except pd.errors.EmptyDataError:
        st.error("로그 파일이 비어 있습니다.")
        return [0, 0, 0, 0, 0, 0, 0]
    except pd.errors.ParserError:
        st.error("로그 파일을 읽는 중 오류가 발생했습니다.")
        return [0, 0, 0, 0, 0, 0, 0]
