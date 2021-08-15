import requests
import pandas as pd
import re

def get_tickers():
    res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")
    df = pd.read_html(res.text)[0]
    df.columns = ['有價證券代號及名稱', '國際證券辨識號碼(ISIN Code)', '上市日', '市場別', '產業別', 'CFICode', '備註']

    stackCodeList = []
    for code in df['有價證券代號及名稱']:
        pattern = "[0-9]"
        stackCode = code.split('　')
        if stackCode[0] and re.search(pattern, stackCode[0]) and len(stackCode[0]) == 4:
            stackCodeList.append(str(stackCode[0]))
    
    return stackCodeList


