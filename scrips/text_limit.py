import pandas as pd
import matplotlib.pyplot as plt

path = "/Users/yukihirakawa/Desktop/django/pdf_text/scrips/file_example_CSV_5000.csv"
df = pd.read_csv(path, index_col=0)
# valiables = ["First Name", "Last Name", "Country"]
# dt = df[valiables]
# dt = df.query('(Gender == "Female")')

plt.hist(x=df["Age"])
plt.ylabel('Country')

plt.show()


# plt.plot(df['Gender'], df['Age']) # 折れ線グラフをプロット

# plt.title('Transition of Sensor1 value')          # 図のタイトル
# plt.xlabel('Time (s)')                            # x軸のラベル
# plt.ylabel('Value')                               # y軸のラベル

# plt.show()    