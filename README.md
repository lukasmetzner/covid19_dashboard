# Streamlit Covid19 Dashboard
**Hobby project! Not the work of an expert 😅**
### Sources
- **JHU CSSE - 	Johns Hopkins University Center for Systems Science and Engineering**
- <a href="https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases" target="_blank">Source Dashboard</a>
- <a href="https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv" target="_blank">Global Cases Download ⬇</a>
- <a href="https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv" target="_blank">Global Deaths Download ⬇</a>
- <a href="https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv" target="_blank">Global Recovered Download ⬇</a>

### Setup
**Requirements**
```bash
pip3 install -r requirements.txt
```
**Download data**
```bash
python3 ./scripts/data_downloader.py <your_country> # The default is Germany, if not specified
```
**Start streamlit server**
```bash
streamlit run ./streamlit_dashboard/app.py
```

![Dashboard preview](misc/dashboard_preview.png "Preview")
