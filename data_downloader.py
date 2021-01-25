import requests
import io
import pandas as pd
from dateutil.parser import parse

_SOURCE_CASES = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"
_SOURCE_DEATHS = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv"
_SOURCE_RECOVERED = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv"

def download_dataframe(url: str) -> pd.DataFrame:
    response = requests.get(url)
    if response.ok:
        raw_data = response.content.decode("UTF-8")
        return pd.read_csv(io.StringIO(raw_data))
    else:
        print(f"Error with {url}")
        return None
    
def transform_dataframe(df: pd.DataFrame, c_type: str, country: str = "Germany") -> pd.DataFrame:
    dict_cases = df[df["Country/Region"] == country].to_dict(orient='dict')
    df_prep = pd.DataFrame(columns=["date", f"abs_{c_type}"])
    for k, v in dict_cases.items():
        date = ""
        try:
            date = parse(k)
        except:
            continue
        value_from_dict = 0
        for val in v.values():
            value_from_dict = val
            break
        df_prep = df_prep.append({"date": date, f"abs_{c_type}": value_from_dict}, ignore_index=True)


    for index, _ in df_prep.iterrows():
        if index == 0:
            continue
        pre_day = df_prep.at[index - 1, f"abs_{c_type}"]
        cur_day = df_prep.at[index, f"abs_{c_type}"]
        new_c = cur_day - pre_day
        df_prep.at[index, f"new_{c_type}"] = new_c
    return df_prep.fillna(0)


if __name__ == "__main__":
    transform_dataframe(download_dataframe(_SOURCE_CASES), "cases").to_csv("cases_transformed.csv", index=False)
    transform_dataframe(download_dataframe(_SOURCE_DEATHS), "deaths").to_csv("deaths_transformed.csv", index=False)
    transform_dataframe(download_dataframe(_SOURCE_RECOVERED), "recovered").to_csv("recovered_transformed.csv", index=False)