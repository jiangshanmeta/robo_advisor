import requests


def download_risk_free_rate():
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv"

    params = {
        "id": "TB3MS",
        "cosd": "2000-01-01",  # 开始日期
        "coed": "2023-12-30",  # 结束日期
        "fq": "Monthly",  # 按月获取数据（TB3MS是月度数据）
        "fam": "avg",
        "fgst": "lin",
        "fgsnd": "2023-12-30",
        "fhml": "lin",
        "fml": "lin",
        "fsml": "0",
        "fst": "lin",
        "fqv": "8",
        "fshow": "lin",
        "fshowopt": "0",
        "fan": "Avg",
        "rea": "lin",
        "rec": "lin",
        "rn": "0",
        "rso": "0",
        "ro": "0",
        "lsv": "",
        "lev": "",
        "lcg": "",
        "lasid": "",
        "lhid": ""
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    with open("risk_free_rate.csv", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    download_risk_free_rate()
