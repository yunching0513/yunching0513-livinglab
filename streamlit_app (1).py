import altair as alt
import numpy as np
import random
import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
import plotly.express as px
import time 
import datetime

st.title('The Happy Tree Sensor')

import streamlit as st

st.header('2023 MADE Living Lab')

if st.button('Say hello to the Happy Trees!'):
     st.write('Hi! We are the Happy Tree team from AMS Insitute! :sunglasses::sunglasses:')
else:
     st.write('Goodbye!')

###Step 1 Building a Table 
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# API请求
url = "https://api.thingspeak.com/channels/2316159/feeds.json?results=20"
response = requests.get(url)
data = response.json()

# 提取数据
feeds = data['feeds']

# 转换为DataFrame
df = pd.DataFrame(feeds)

# 打印DataFrame
st.dataframe(df)

# My Sensor's Data
# 初始传感器数据
sensor_data = {
    'channel': {
        'id': 2316159,
        'name': 'Andrew',
        'description': 'Our happy tree Andrew'
    },
    'feeds': []
}


import streamlit as st
import pandas as pd
import datetime
import time
import requests

# 创建一个空的DataFrame，用于存储传感器数据
data = pd.DataFrame(columns=["Date", "Moisture"])

# 创建一个Streamlit应用
st.title("Real-time Sensor Data")

# 添加启动和停止数据更新的按钮
start_button = st.button("Start Data Update")
stop_button = st.button("Stop Data Update")

update_data = False  # 控制数据更新的标志

# Initialize the chart
chart = st.line_chart(data.set_index("Date"))

# Simulate real-time data updates
while True:
    if start_button:
        update_data = True
        start_button = False

    if stop_button:
        update_data = False
        stop_button = False

    if update_data:
        current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        
        # Get data from the API
        api_url = "https://api.thingspeak.com/channels/2316159/feeds.json?results=2"
        response = requests.get(api_url)
        api_data = response.json()
        
        # Extract humidity data from the API response
        new_moisture = api_data['feeds'][0]['field1']

        new_data = pd.DataFrame({"Date": [current_time], "Moisture": [new_moisture]})

        # Use the concat function to add the new data row to the existing data
        data = pd.concat([data, new_data], ignore_index=True)

        # Update the chart data
        chart.line_chart(data.set_index("Date"))

     # Simulate data update interval (e.g., update every 1 minute)
    time.sleep(5)