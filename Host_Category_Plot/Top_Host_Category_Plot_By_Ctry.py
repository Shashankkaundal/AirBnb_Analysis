import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = ['Heiti TC']
str1="No Data available"
def Top_Host_Category_Plot_By_Ctry(val):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    df2 = data[data["Country"] == val]
    Name_Cord_DF = df2[['Name','Price']]
    Name_Cord_DF['Price'] = Name_Cord_DF['Price'].astype(int)
    Name_Cord_DF.sort_values(['Price'], inplace=True,ascending=False)
    Name_Cord_DF.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Host_Category_Plot/Host_By_Country.csv",
                       index=False)
    if Name_Cord_DF.shape[0]<1:
        return str1
    else:
        abc=sns.barplot(data=Name_Cord_DF.head(10), x="Price",
                y="Name", errorbar=("pi", 95), palette="pastel", hue="Price", legend=False)
        z=wrap_labels(abc,25)
    #abc.set_xticklabels(abc.get_xticklabels(),
                              #rotation=90,
                              #horizontalalignment='right')
    # ax.locator_params(integer=True)
        return plt
import textwrap
def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_yticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                                    break_long_words=break_long_words))
    ax.set_yticklabels(labels, rotation=0)