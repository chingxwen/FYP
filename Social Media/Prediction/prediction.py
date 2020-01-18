import pandas as pd 
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller




register_matplotlib_converters()

# read csv

parse_date = ['date']

df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Stock/2018-05-05.2019-05-05.AAPL.csv',  parse_dates= parse_date,
                                                        dtype = [
                                                               ('open','float64'),
                                                               ('high','float64'),
                                                               ('low','float64'),
                                                               ('close','float64'),
                                                               ('adj_close','float64'),
                                                               ('volume','float64'),
                                                               ('Stockname','str'),
                                                               ('Open_USD','float64'),
                                                               ('High_USD','float64'),
                                                               ('Low_USD','float64'),
                                                               ('Close_USD','float64'),
                                                               ('Adj_Close_USD','U100')])
df1 = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/pushshiftsamsungsubmission2018August/pushshiftsamsungsubmission2018AugustSentimentAll.csv')

print(df['close'])
# print(df1['net'].loc['2018-08'])


# # Plot
# fig, axes = plt.subplots(nrows=3, ncols=2, dpi=120, figsize=(10,6))
# for i, ax in enumerate(axes.flatten()):
#     data = df[df.columns[i]]
#     ax.plot(data, color='red', linewidth=1)
   
#     # Decorations
#     ax.set_title(df.columns[i])
#     ax.xaxis.set_ticks_position('none')
#     ax.yaxis.set_ticks_position('none')
#     ax.spines['top'].set_alpha(0)
#     ax.tick_params(labelsize=6)
#     plt.tight_layout()

# plt.show()


# test for normal distribution 

stat,p = stats.normaltest(df.close)
print('Statictics = %.3f , p=%3.f' % (stat, p))

alpha = 0.05 

if p > alpha:
    print('Data is not normally distributed')

else:

    print('Data is normally distributed')

print('Kurtosis of distribution : {}'. format(stats.kurtosis(df.close)))
print('Skewness of normal distribution : {}'.format(stats.skew(df.close)))


# plot ditribution graph to check for probablity to see how each value is skewed

# plt.figure(figsize=(14,6))
# plt.subplot(1,2,1)
# df['close'].hist(bins=50)
# plt.title('Closing Price')
# plt.subplot(1,2,2)
# stats.probplot(df['close'], plot=plt)
# print(df.close.describe().T)

# plt.show()

# Autocorrelation and partial correlation

fig, ax = plt.subplots(2, figsize = (10,6)) #Close acf and pacf on training data
ax[0] = plot_acf(df.close, ax=ax[0], lags = 5)
ax[1] = plot_pacf(df.close, ax = ax[1])

plt.show()


# split series into train and testing data
nobs = 15

X_train, X_test = df[0:-nobs], df[-nobs:]

#check size

print(X_train.shape)
print(X_test.shape)


#Transformation

transform_data = X_train.dropna()
transform_data.head()

print(transform_data.describe())

#stationary check
def adfuller_test(series, signif=0.05, name='', verbose = False):

    #Perform ADFuller to test for Stationary of given series and print report 

    r = adfuller(series, autolag = 'AIC')
    output = {'test_statistic' : round(r[0],4), 'pvalue' : round(r[1],4), 'n_lags':round(r[2],4), 'n_obs': r[3] }

    p_value = output['pvalue']

    def adjust(val , length = 6): return str(val).ljust(length)

    print(f' Augmented Dickey-Fuller Test on "{name}" ', "\n  ", '-'*47 )
    print(f'Null Hypothesis: Data has unit root. Non-Stationary.')
    print(f'Significance Level = {signif}')
    print(f'Test statistic = {output["test_statistic"]}')
    print(f'No, lags chosen = {output["n_lags"]}')


    for key,val in r[4].items():

        print(f'Critical Value {adjust(key)} = {round(val,3)}')

    if p_value <= signif :
        print(f" => P-value = {p_value}.Rejecting Null Hypothesis")
        print(f"Series is Stationary")

    else:
        print(f" => P-Value ={p_value}.Weak evidence to reject the null hypothesis")
        print(f" => Series is Non-stationary")

    #ADF Test on each column 

for name, column in transform_data.iteritems():

    adfuller_test(column, name=column.name)
    print('\n')


