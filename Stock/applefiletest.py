{
  "cells": [
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "# Important imports\n\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport matplotlib.dates as mdates\nimport matplotlib.cbook as cbook\nimport numpy as np\nimport os",
      "execution_count": 1,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "# Read freshly downloaded file\ndata = pd.read_csv(\"AAPL.csv\")\n\n# Remove rows with null values\ndata['High'] = data['High'].replace('null', np.nan)\ndg = data.dropna(axis=0, subset=['High'])\n\n#renaming columns\ndg.rename(columns={'Adj Close':'adj_close', 'Date':'date', 'Volume': 'volume', 'Close':'close', 'Low': 'low', 'High': 'high', 'Low': 'low', 'Open':'open'}, inplace = True)\n\n# Write to a new csv\n#pd.DataFrame.from_dict(data=dg, orient='columns').to_csv(\"cleanedAAPL.csv\")\n\n# Change data to a dataframe\ndf = pd.DataFrame(dg)\n",
      "execution_count": 2,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "\n# Insert new column data into new column, stating the stockname - so later can combine multiple files\nStockname = []\nfilename = \"AAPL.csv\"\n\nfor i in range (len(df.high)):\n    Stockname.append(os.path.splitext(filename)[0])\n    \n# Add a column and column name\ndf.insert(7, \"Stockname\", Stockname , True)\n\n\nprint(Stockname)\nprint(df)",
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": "['AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL']\n            date        open        high         low       close   adj_close  \\\n0     2015-09-30  110.169998  111.540001  108.730003  110.300003  102.941124   \n1     2015-10-01  109.070000  109.620003  107.309998  109.580002  102.269157   \n2     2015-10-02  108.010002  111.010002  107.550003  110.379997  103.015785   \n3     2015-10-05  109.879997  111.370003  109.070000  110.779999  103.389107   \n4     2015-10-06  110.629997  111.739998  109.769997  111.309998  103.883736   \n5     2015-10-07  111.739998  111.769997  109.410004  110.779999  103.389107   \n6     2015-10-08  110.190002  110.190002  108.209999  109.500000  102.194481   \n7     2015-10-09  110.000000  112.279999  109.489998  112.120003  104.639717   \n8     2015-10-12  112.730003  112.750000  111.440002  111.599998  104.154366   \n9     2015-10-13  110.820000  112.449997  110.680000  111.790001  104.331711   \n10    2015-10-14  111.290001  111.519997  109.559998  110.209999  102.857132   \n11    2015-10-15  110.930000  112.099998  110.489998  111.860001  104.397049   \n12    2015-10-16  111.779999  112.000000  110.529999  111.040001  103.631767   \n13    2015-10-19  110.800003  111.750000  110.110001  111.730003  104.275711   \n14    2015-10-20  111.339996  114.169998  110.820000  113.769997  106.179642   \n15    2015-10-21  114.000000  115.580002  113.699997  113.760002  106.170296   \n16    2015-10-22  114.330002  115.500000  114.099998  115.500000  107.794189   \n17    2015-10-23  116.699997  119.230003  116.330002  119.080002  111.135353   \n18    2015-10-26  118.080002  118.129997  114.919998  115.279999  107.588867   \n19    2015-10-27  115.400002  116.540001  113.989998  114.550003  106.907570   \n20    2015-10-28  116.930000  119.300003  116.059998  119.269997  111.312668   \n21    2015-10-29  118.699997  120.690002  118.269997  120.529999  112.488594   \n22    2015-10-30  120.989998  121.220001  119.449997  119.500000  111.527328   \n23    2015-11-02  120.800003  121.360001  119.610001  121.180000  113.095245   \n24    2015-11-03  120.790001  123.489998  120.699997  122.570000  114.392502   \n25    2015-11-04  123.129997  123.820000  121.620003  122.000000  113.860535   \n26    2015-11-05  121.849998  122.690002  120.180000  120.919998  113.335655   \n27    2015-11-06  121.110001  121.809998  120.620003  121.059998  113.466873   \n28    2015-11-09  120.959999  121.809998  120.050003  120.570000  113.007607   \n29    2015-11-10  116.900002  118.070000  116.059998  116.769997  109.445953   \n...          ...         ...         ...         ...         ...         ...   \n999   2019-09-19  222.009995  223.759995  220.369995  220.960007  220.960007   \n1000  2019-09-20  221.380005  222.559998  217.470001  217.729996  217.729996   \n1001  2019-09-23  218.949997  219.839996  217.649994  218.720001  218.720001   \n1002  2019-09-24  221.029999  222.490005  217.190002  217.679993  217.679993   \n1003  2019-09-25  218.550003  221.500000  217.139999  221.029999  221.029999   \n1004  2019-09-26  220.000000  220.940002  218.830002  219.889999  219.889999   \n1005  2019-09-27  220.539993  220.960007  217.279999  218.820007  218.820007   \n1006  2019-09-30  220.899994  224.580002  220.789993  223.970001  223.970001   \n1007  2019-10-01  225.070007  228.220001  224.199997  224.589996  224.589996   \n1008  2019-10-02  223.059998  223.580002  217.929993  218.960007  218.960007   \n1009  2019-10-03  218.429993  220.960007  215.130005  220.820007  220.820007   \n1010  2019-10-04  225.639999  227.490005  223.889999  227.009995  227.009995   \n1011  2019-10-07  226.270004  229.929993  225.839996  227.059998  227.059998   \n1012  2019-10-08  225.820007  228.059998  224.330002  224.399994  224.399994   \n1013  2019-10-09  227.029999  227.789993  225.639999  227.029999  227.029999   \n1014  2019-10-10  227.929993  230.440002  227.300003  230.089996  230.089996   \n1015  2019-10-11  232.949997  237.639999  232.309998  236.210007  236.210007   \n1016  2019-10-14  234.899994  238.130005  234.669998  235.869995  235.869995   \n1017  2019-10-15  236.389999  237.649994  234.880005  235.320007  235.320007   \n1018  2019-10-16  233.369995  235.240005  233.199997  234.369995  234.369995   \n1019  2019-10-17  235.089996  236.149994  233.520004  235.279999  235.279999   \n1020  2019-10-18  234.589996  237.580002  234.289993  236.410004  236.410004   \n1021  2019-10-21  237.520004  240.990005  237.320007  240.509995  240.509995   \n1022  2019-10-22  241.160004  242.199997  239.619995  239.960007  239.960007   \n1023  2019-10-23  242.100006  243.240005  241.220001  243.179993  243.179993   \n1024  2019-10-24  244.509995  244.800003  241.809998  243.580002  243.580002   \n1025  2019-10-25  243.160004  246.729996  242.880005  246.580002  246.580002   \n1026  2019-10-28  247.419998  249.250000  246.720001  249.050003  249.050003   \n1027  2019-10-29  248.970001  249.750000  242.570007  243.289993  243.289993   \n1028  2019-10-30  244.759995  245.300003  241.210007  243.259995  243.259995   \n\n        volume Stockname  \n0     66473000      AAPL  \n1     63929100      AAPL  \n2     58019800      AAPL  \n3     52064700      AAPL  \n4     48196800      AAPL  \n5     46765600      AAPL  \n6     61979600      AAPL  \n7     52766100      AAPL  \n8     30467200      AAPL  \n9     33049300      AAPL  \n10    44462400      AAPL  \n11    37673500      AAPL  \n12    39232600      AAPL  \n13    29759200      AAPL  \n14    48967800      AAPL  \n15    41795200      AAPL  \n16    41654100      AAPL  \n17    59366900      AAPL  \n18    66333800      AAPL  \n19    69884400      AAPL  \n20    85551400      AAPL  \n21    51227300      AAPL  \n22    49365300      AAPL  \n23    32203300      AAPL  \n24    45519000      AAPL  \n25    44886100      AAPL  \n26    39552700      AAPL  \n27    33042300      AAPL  \n28    33871400      AAPL  \n29    59127900      AAPL  \n...        ...       ...  \n999   22060600      AAPL  \n1000  55413100      AAPL  \n1001  19165500      AAPL  \n1002  31190800      AAPL  \n1003  21903400      AAPL  \n1004  18833500      AAPL  \n1005  25352000      AAPL  \n1006  25977400      AAPL  \n1007  34805800      AAPL  \n1008  34612300      AAPL  \n1009  28606500      AAPL  \n1010  34619700      AAPL  \n1011  30576500      AAPL  \n1012  27955000      AAPL  \n1013  18692600      AAPL  \n1014  28253400      AAPL  \n1015  41698900      AAPL  \n1016  24106900      AAPL  \n1017  21840000      AAPL  \n1018  18475800      AAPL  \n1019  16896300      AAPL  \n1020  24358400      AAPL  \n1021  21811800      AAPL  \n1022  20573400      AAPL  \n1023  18957200      AAPL  \n1024  17318800      AAPL  \n1025  18330500      AAPL  \n1026  24112500      AAPL  \n1027  35660100      AAPL  \n1028  30950600      AAPL  \n\n[1029 rows x 8 columns]\n",
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "pd.DataFrame.from_dict(data=df, orient='columns').to_csv(\"cleanedappletesting.csv\")",
      "execution_count": 8,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "",
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "name": "python36",
      "display_name": "Python 3.6",
      "language": "python"
    },
    "language_info": {
      "mimetype": "text/x-python",
      "nbconvert_exporter": "python",
      "name": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.6",
      "file_extension": ".py",
      "codemirror_mode": {
        "version": 3,
        "name": "ipython"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}