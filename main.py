import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

st.title("📚 MBTI별 국어 과목 성취도 분석")
st.write("당신의 MBTI 유형은 국어 과목에서 어떤 성취도를 보일까요? 아래에서 MBTI 유형을 선택해보세요!")

# --- 데이터 생성 (예시 데이터) ---
# 실제 데이터가 있다면 이 부분을 실제 데이터로 대체해주세요.
data = {
    'MBTI 유형': ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
                  'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'],
    '평균 국어 점수': [85, 88, 92, 90, 80, 83, 93, 91,
                      78, 82, 89, 87, 86, 89, 94, 92],
    '성취도 등급': ['B', 'B+', 'A', 'A', 'C+', 'C+', 'A+', 'A',
                   'C', 'C+', 'B+', 'B+', 'B', 'B+', 'A+', 'A'],
    '주요 학습 스타일': ['꼼꼼한 분석', '차분한 정리', '심층적 이해', '논리적 접근',
                       '실용적 학습', '경험 중심', '개념 연결', '탐구적 사고',
                       '즉흥적 응용', '활동적 참여', '아이디어 발상', '토론 및 논쟁',
                       '체계적 관리', '협력적 학습', '공감적 이해', '목표 지향']
}
df = pd.DataFrame(data)

# --- MBTI 유형 선택 (스크롤) ---
st.sidebar.header("MBTI 유형 선택 🧐")
selected_mbti = st.sidebar.selectbox(
    "알고 싶은 MBTI 유형을 선택하세요:",
    df['MBTI 유형'].unique()
)

st.write(f"---")

# --- 결과 표시 ---
if selected_mbti:
    st.subheader(f"✨ **{selected_mbti}** 유형의 국어 과목 성취도")
    result = df[df['MBTI 유형'] == selected_mbti]

    # 표로 결과 보여주기
    st.table(result.set_index('MBTI 유형')) # MBTI 유형을 인덱스로 설정하여 깔끔하게 표시

    st.markdown(f"**💡 {selected_mbti}** 유형은 **{result['주요 학습 스타일'].iloc[0]}**에 강점을 보여요.")
    st.markdown(f"평균적으로 **{result['평균 국어 점수'].iloc[0]}점**을 기록하며, 성취도 등급은 **{result['성취도 등급'].iloc[0]}**입니다. 📈")

else:
    st.info("좌측 사이드바에서 MBTI 유형을 선택해주세요.")

st.write("---")
st.caption("※ 이 데이터는 예시이며, 실제 MBTI별 국어 성취도를 대표하지 않습니다.")
