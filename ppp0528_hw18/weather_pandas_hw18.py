from ppp0519.sfarm_hw import submit_to_api
import os.path
import requests
import pandas as pd

def download_weather(station_id, year, filename):

    URL =f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)


def main():
    filename_2012 = "weather(146)_2012-2012.csv"
    if not os.path.exists(filename_2012):
        download_weather(146, 2012, filename_2012)

    filename_su_2019 = "weather(119)_2019-2019.csv"
    if not os.path.exists(filename_su_2019):
        download_weather(119, 2019, filename_su_2019)

    filename_2019 = "weather(146)_2019-2019.csv"
    if not os.path.exists(filename_2019):
        download_weather(146, 2019, filename_2019)

    filename_2020 = "weather(146)_2020-2020.csv"
    if not os.path.exists(filename_2020):
        download_weather(146, 2020, filename_2020)

    filename_2024 = "weather(146)_2024-2024.csv"
    if not os.path.exists(filename_2024):
        download_weather(146, 2024, filename_2024)

    df_12 = pd.read_csv(filename_2012, skipinitialspace=True)
    df_su19 = pd.read_csv(filename_su_2019, skipinitialspace=True)
    df_19 = pd.read_csv(filename_2019, skipinitialspace=True)
    df_20 = pd.read_csv(filename_2020, skipinitialspace=True)
    df_24 = pd.read_csv(filename_2024, skipinitialspace=True)

    ysum_12 =round(df_12["rainfall"].sum(),1)
    ymax_24 = round(df_24["tmax"].max(),1)
    ymm_20 = round((df_20["tmax"] - df_20["tmin"]).max() ,1)
    yabs_19 = round((abs(df_su19["rainfall"].sum() - df_19["rainfall"].sum())),1)

    # http://sfarm.digitalag.kr:8800
    name = "이성학"
    affiliation = "스마트팜학과"
    student_id = "202210099"

    answer1 = ysum_12
    answer2 = ymax_24
    answer3 = ymm_20
    answer4 = yabs_19

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__=="__main__":
    main()