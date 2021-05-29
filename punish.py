import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['Country'].tolist())

    Country     = df['Country'].tolist()

    Punishment_Percent        = df['Punishment_Severity_Percent'].tolist()

    # print(df['quebec'].tolist())

    result_dict = {
        'Country '            : Country,
        'Punishment_Percent'             : Punishment_Percent
    }

    print(result_dict)

    return result_dict

def add_row(Country, Punishment_Percent):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'Country'       : Country, 
        'Punishment_Percent' : Punishment_Percent
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()