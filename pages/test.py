import streamlit as st
from datetime import datetime

# タイトル
st.title("ユーザー情報入力フォーム")

# 性別の選択（ラジオボタン）
gender = st.radio(
    "性別を選択してください:",
    ("男性", "女性")
)

# 名前の入力
first_name = st.text_input("名前（名）を入力してください:")
last_name = st.text_input("名前（姓）を入力してください:")

# 生年月日の入力
birth_date = st.date_input("生年月日を選択してください:", datetime.now())

# 入力された情報の表示
if st.button("送信"):
    st.write("性別:", gender)
    st.write("名前:", last_name, first_name)
    st.write("生年月日:", birth_date)
