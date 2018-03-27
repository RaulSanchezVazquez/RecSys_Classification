def get_hist_user(params):
    """
    Get Hist. user one hotted
    """
    
    DATE = params['DATE']
    TARGET = params['TARGET']
    ID_ITEM = params['ID_ITEM']
    ID_USER = params['ID_USER']
    user_hist = params['data']
    
    user_hist.sort_values(
        DATE,
        inplace=True
    )

    data = []
    target = []
    date = []
    
    for it in range(user_hist.shape[0]):
        hist = user_hist.iloc[:it+1]
        hist.index = hist[ID_ITEM].astype(str)

        cum_hist = (
            hist.iloc[:-1][TARGET]
        ).to_dict()
        
        if hist.shape[0] > 1:
            cum_hist['i-1'] = str(hist.iloc[-2][ID_ITEM])
        else:
            cum_hist['i-1'] = 'first'

        cum_hist['i'] = str(hist.iloc[-1][ID_ITEM])
        cum_hist['user'] = hist.iloc[-1][ID_USER].astype(str)
        
        data.append(cum_hist)
        date.append(hist.iloc[-1][DATE])
        target.append(hist.iloc[-1][TARGET])
        
    return data, date, target