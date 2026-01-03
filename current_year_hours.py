import sys
from streamlit_app import get_data, zip_to_gps

if __name__ == "__main__":
    assert len(sys.argv) == 2, "please provide zip code as argument"
    zip_code = sys.argv[1]
    lat, lon = zip_to_gps(zip_code)
    from_year = 2020
    to_year = 2026
    chill_max = 45
    chill_min = 32
    df, _ = get_data(lat, lon, from_year, to_year)
    df = df[df.year == to_year]  # limit to this year
    df["count"] = (df["temperature_2m"] <= chill_max) & (
        df["temperature_2m"] >= chill_min
    )
    chill_hours_this_year = df["count"].sum()
    print(chill_hours_this_year)
