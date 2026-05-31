import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. 秘密のAPIキーを読み込んで、Geminiを動かす準備
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. アプリの画面（見た目）をデザインする
st.title("🤖 僕の・私の AIアシスタント")
st.write("質問を入力して「送信」ボタンを押してね。")

# 文字を入力する箱（入力欄）を作る
user_input = st.text_input("質問内容", placeholder="例：オムライスの作り方を教えて")

# 「送信」ボタンを作る
if st.button("AIに質問する"):
    
    # 入力欄が空っぽじゃないか確認する
    if user_input:
        with st.spinner("Geminiが考えています..."):
            try:
                # 3. Geminiに質問を送信する
                config = types.GenerateContentConfig(
                    system_instruction="あなたは優秀なアシスタントです。中学生にもわかるように短く答えてください。"
                )
                
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_input, # 入力欄に書かれた文字を渡す
                    config=config
                )
                
                # 4. 返ってきた答えを画面に表示する
                st.success("🤖 Geminiからの返答：")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("質問を入力してください。")