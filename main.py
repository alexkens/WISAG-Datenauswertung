import pandas as pd

import util


if __name__ == '__main__':

    df = pd.DataFrame(
        [
            (1, 'Hello', 158, True, 12.8),
            (2, 'Hey', 567, False, 74.2),
            (3, 'Hi', 123, False, 1.1),
            (4, 'Howdy', 578, True, 45.8),
            (5, 'Hello', 418, True, 21.1),
            (6, 'Hi', 98, False, 98.1),
        ],
        columns=['colA', 'colB', 'colC', 'colD', 'zzzzzz']
    )
    print(df)

    df['colF'] = df['colA'] + df['colC']

    print(df)












