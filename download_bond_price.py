import requests


def download_bond_price(id: str, start_date: str, end_date: str, file_name: str):
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv"

    params = {
        "id": id,
        "cosd": start_date,  # 开始日期
        "coed": end_date,  # 结束日期
        "fq": "Monthly",  # 按月获取数据（TB3MS是月度数据）
        "fam": "avg",
        "fgst": "lin",
        "fgsnd": end_date,
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

    response = requests.get(url, params=params, timeout=180)
    response.raise_for_status()

    with open(file_name, "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    download_bond_price("BAMLCC8A015PYTRIV", "1984-06-29", "2020-12-31", "data/corporate_bond.csv")
    download_bond_price("DGS10", "1984-06-29", "2020-12-31", "data/treasury_bond_yield.csv")
    download_bond_price("DTB3", "1984-06-29", "2020-12-31", "data/short_term_risk_free_rate.csv")
