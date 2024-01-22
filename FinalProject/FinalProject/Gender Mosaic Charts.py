import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
df = pd.read_csv('removedNulls.csv')
df["education"].replace([' 11th', ' 9th', ' 7th-8th', ' 5th-6th', ' 10th', ' Preschool', ' 12th', ' 1st-4th'], "Pre High School", inplace = True)

# # Mosaic Plot of Men/Women Education
mosaic(df, ["sex", "education"])
plt.title("Women/Men Who Earn >50K")
plt.show()
# # Mosaic Plot of Men/Women Income
# mosaic(df, ["sex", "income"])
#
# plt.title("Women/Men Who Earn >50K")
# plt.show()
