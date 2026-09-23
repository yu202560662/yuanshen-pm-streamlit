import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",

    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.miyoushe.com/ys',
        'Report a bug': "https://ys.mihoyo.com/cloud/#/",
        'About': "我是派蒙,你的提瓦特小助手"
    }
)

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com")
if "messages" not in st.session_state:
    st.session_state.messages = []



st.title("欢迎进入提瓦特")
st.header("欢迎来到璃月港")
st.subheader("我是超级无敌薯条大王&应急食品&最好的伙伴")


st.write("嗨！我是派蒙，是旅行者最好的伙伴!")
st.write("还记得我们刚认识的时候吗？我一不小心掉进湖里，差点就溺水啦，还好被你救上来咯！为了报答你的救命之恩，我就勉为其难当你的专属向导，陪你在提瓦特大陆到处冒险，帮你寻找失散的亲人！")
st.write("提瓦特可好玩啦！蒙德有自由的风，璃月藏着古老的岩，稻妻飘荡着雷暴……七国每一处都有新鲜事儿！我看得懂各地古怪文字，还能解读石碑上的秘密。路上有藏起来的宝箱、奇奇怪怪的路人，都可以问我！")
st.write("别看我个子小小的，本事可不小！冒险的时候，我会提醒你小心怪物和陷阱，遇到有意思的人和事，我还能陪你一起吐槽")
st.image("./data/29d777e240d03e18831c784481159f5e.jpg")
st.write("但是！有一件事绝对不能做——不许再叫我应急食品！我才不是用来填饱肚子的东西！哼！")
st.image("./data/685ca0a53bc804df1eb8ade6b99755a2.jpg")

st.radio("你认为派蒙应该叫什么名字:",["最好的伙伴","应急食品",'飞行矮堇瓜',"大名鼎鼎的派蒙小朋友","白白矮矮香香吵吵事情多多双足兽"])
st.image("./data/a388e2fde136b61c44127674eaefc273.jpg")

prompt=st.chat_input("请输入你冒险之旅的问题:")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个可爱调皮的小派蒙，你必须带入原神派蒙的游戏设定以及你必须熟悉游戏的各个术语专业名称且能够为玩家提供游戏攻略,能够回答旅行者的问题，并且能够用游戏术语进行交流。"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    st.chat_message("assistant").write(response.choices[0].message.content)

    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})




