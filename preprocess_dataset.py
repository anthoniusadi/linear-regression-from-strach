import pandas as pd
#!extract data from dataset
def export():
    df = pd.read_csv('dataset/prices.csv')
    df=df.dropna(how='any')
    df = df.drop(['open','high','low','volume'],axis=1)
    df=df[df['symbol']=='AAPL']
    df = df.drop(df.index[19:])
    day = df['date'].str[8:10].astype('int32')
    df['day']=day
    df = df.drop(['date','symbol'],axis=1)
    df['day']= pd.to_numeric(df['day'])
    df['close']= pd.to_numeric(df['close']).astype('int')
    # df.to_csv('stock.csv',index=False)
    X =df['day'].to_numpy()
    Y =df['close'].to_numpy()
    X_Tr= X[:8]
    Y_Tr= Y[:8]
    X_Ts= X[8:]
    Y_Ts= Y[8:]

    # from matplotlib import pyplot as plt
    # r=(day)
    # plt.plot(r,df['close'])
    # plt.xticks(r,rotation='vertical')
    # plt.xlabel('day')
    # plt.ylabel('$')
    # plt.title('AAPL Stocks')
    # plt.show()
    return X_Tr,X_Ts,Y_Tr,Y_Ts