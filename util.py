import pandas as pd


PATH = "Operations-Report-WGS BER.xlsx"
MASCHINENTYP_SCHLEPP = "Gepäck- und Ausrüstungswagen"


def get_df():
    # Read input and convert it to a dataframe
    df = pd.read_excel(PATH)
    # clean the data up
    df = pd.DataFrame(rename(df))
    return df


def get_maschinentyp_schlepp_df():
    df = get_df()
    df = df[df['Maschinentyp'] == MASCHINENTYP_SCHLEPP]
    return df


def create_data_file(data):
    data = dict(data)
    with open('data_file.txt', 'w') as f:
        for e in data:
            string = str(e) + ": " + str(data[e]) + "\n"
            f.write(string)


def rename(df):
    colum_length = df.columns.size

    for i in range(colum_length):
        name = df.keys()[i]
        substitute = df.iloc[0][i]
        df = df.rename(columns={name: substitute})

    df = df.iloc[1:, :]
    return df


def convert_time_to_float_time(time):
    time = str(time)
    x = time.split(':', 1)[0]
    y = time.split(':', 2)[1]
    time = x + "." + y
    return float(time)


if __name__ == '__main__':

    time = "02:04:00"
    float_time = convert_time_to_float_time(time)
    print(float_time)