from django.shortcuts import render
import matplotlib.pyplot as plt
# io : 입출력 연산을 위한 Python 표준 라이브러리
# ByteIO : 이진 데이터를 다루기 위한 버퍼(임시 저장 공간) 제공
# 버퍼 : 파일 시스템과 유사 / 실제로 파일로 만들지 않고, 메모리 단에서 작업 가능
from io import BytesIO
# 텍스트 <-> 이진 테이터 변환 모듈 
import base64

# <참고> UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
# PLT를 만드는 곳과 화면에 그리는 곳이 달라서 오류가 날 수 있습니다.
# 해결 : 백엔드를 Agg로 설정하여 변경(Matplotlib 라이브러리 공식문서 - Backend)
plt.switch_backend('Agg')

# Create your views here.
'''
def problem21(request):
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]
    
    plt.clf() # 다른 view 함수에서 plt를 그린 상태일 경우, 중복 출력되는 것을 방지(plt 초기화)
    plt.plot(x, y)
    # 임시 저장 -> STATIC_DIR에 등록, 갱신 때 마다 저장 필요 X
    # buffer 활용 : Python 내장 모듈 io에 포함된 BytesIO 클래스 사용
    # 메모리 내에 데이터를 저장 및 조작할 수 있는 기능 제공
    # plt.plot -> 이진 데이터 -> 버퍼에 저장 -> 저장 주소를 template에 전달
    buffer = BytesIO() # 빈 버퍼 생성
    plt.savefig(buffer, format='png') # 버퍼에 plt를 png 형태로 저장
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '') # 버퍼 내용을 base64로 인코딩 / 템플릿에 넘기기 위해 디코딩    
    buffer.close() # 버퍼 닫기

    # 이미지를 웹 페이지에 표시하기 위해
    # URL 형식(주소 형식)으로 만들어진 문자열 생성
    
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}' 
    }
    return render(request, 'weathers/problem1.html', context)
'''


import pandas as pd
csv_path = 'weathers/data/austin_weather.csv'

def problem1(request):
    # 읽어온 csv 파일을 df에 저장
    df = pd.read_csv(csv_path)
    context = {
        'df' : df,
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df = pd.read_csv(csv_path)
    Date = pd.to_datetime(df['Date'])
    TempHighF = df['TempHighF']
    TempLowF = df['TempLowF']
    TempAvgF = df['TempAvgF']

    # plot 초기화
    plt.clf()
    # plt.plot 생성
    plt.plot(Date, TempHighF, label='TempHighF')
    plt.plot(Date, TempLowF, label='TempLowF')
    plt.plot(Date, TempAvgF, label='TempAvgF')    
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenherit)')
    plt.grid()
    plt.legend()
    buffer = BytesIO() # 빈 버퍼 생성
    plt.savefig(buffer, format='png') # 버퍼에 plt를 png 형태로 저장
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '') # 버퍼 내용을 base64로 인코딩 / 템플릿에 넘기기 위해 디코딩    
    buffer.close() # 버퍼 닫기
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}' 
    }
    
    # # 일별 최고, 평균, 최저 온도
    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    # df['Date'] = pd.to_datetime(pd['Date'])
    # df['Month'] = df['Date'].dt.month
    df = df.groupby(pd.Grouper(key="Date", freq="1M")).agg({
        "TempHighF" : "mean", 
        "TempLowF" : "mean", 
        "TempAvgF" : "mean"
        }).reset_index()
    print(df)
    Date = df['Date']
    TempHighF = df['TempHighF']
    TempLowF = df['TempLowF']
    TempAvgF = df['TempAvgF']

    # plot 초기화
    plt.clf()
    # plt.plot 생성
    plt.plot(Date, TempHighF, label='TempHighF')
    plt.plot(Date, TempLowF, label='TempLowF')
    plt.plot(Date, TempAvgF, label='TempAvgF')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenherit)')
    plt.grid()
    plt.legend(loc='lower right')
    
    buffer = BytesIO() # 빈 버퍼 생성
    plt.savefig(buffer, format='png') # 버퍼에 plt를 png 형태로 저장
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '') # 버퍼 내용을 base64로 인코딩 / 템플릿에 넘기기 위해 디코딩    
    buffer.close() # 버퍼 닫기
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}' 
    }
    
    # # 일별 최고, 평균, 최저 온도
    return render(request, 'weathers/problem3.html', context)

import numpy as np
def problem4(request):
    df = pd.read_csv(csv_path)
    # Date = pd.to_datetime(df['Date'])
    print(df)
    Events = df["Events"]
    num_events = [0] * 5
    
    NAN_data_counts = len(df)
    for event in Events:
        # arr = event.split(",")
        # for e in arr:

        if 'Rain' in event:
            num_events[1] += 1
            NAN_data_counts -= 1
        if 'Thunderstorm' in event:
            num_events[2] += 1
            NAN_data_counts -= 1
        if 'Fog' in event:
            num_events[3] += 1
            NAN_data_counts -= 1
        if 'Snow' in event:
            num_events[4] += 1
            NAN_data_counts -= 1

    num_events[0] = NAN_data_counts
    events = ['No Event', 'Rain', 'Thunderstorm', 'Fog', 'Snow']
    x = np.arange(5)
    y = num_events
    plt.clf() # 다른 view 함수에서 plt를 그린 상태일 경우, 중복 출력되는 것을 방지(plt 초기화)
    plt.bar(x, y)
    plt.xticks(x, events)
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.grid()
    # 임시 저장 -> STATIC_DIR에 등록, 갱신 때 마다 저장 필요 X
    # buffer 활용 : Python 내장 모듈 io에 포함된 BytesIO 클래스 사용
    # 메모리 내에 데이터를 저장 및 조작할 수 있는 기능 제공
    # plt.plot -> 이진 데이터 -> 버퍼에 저장 -> 저장 주소를 template에 전달
    buffer = BytesIO() # 빈 버퍼 생성
    plt.savefig(buffer, format='png') # 버퍼에 plt를 png 형태로 저장
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '') # 버퍼 내용을 base64로 인코딩 / 템플릿에 넘기기 위해 디코딩    
    buffer.close() # 버퍼 닫기

    # 이미지를 웹 페이지에 표시하기 위해
    # URL 형식(주소 형식)으로 만들어진 문자열 생성
    
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}' 
    }
    return render(request, 'weathers/problem4.html', context)
