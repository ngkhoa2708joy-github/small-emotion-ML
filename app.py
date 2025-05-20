# app.py
import streamlit as st
import joblib
import os
import streamlit as st
import joblib

if os.path.exists("emotion_model.joblib"):
    model = joblib.load("emotion_model.joblib")
else:
    st.error("Không tìm thấy file model! Hãy chắc file 'emotion_model.joblib' nằm cùng thư mục với app.py.")


# Load model đã train
model = joblib.load("emotion_model.joblib")

# Giao diện
st.set_page_config(page_title="Emotion Detector", page_icon="💭")
st.title("💭 Emotion Detector")
st.write("Dự đoán cảm xúc từ câu nói của bạn 😄😢😡")

# Input từ user
text = st.text_input("Nhập câu của bạn:")

# Nút dự đoán
if st.button("Dự đoán"):
    if text.strip() == "":
        st.warning("Bạn chưa nhập gì cả!")
    else:
        prediction = model.predict([text])[0]
        st.success(f"👉 Cảm xúc được dự đoán: **{prediction.upper()}**")
