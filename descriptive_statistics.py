'''
@author : jhhalls
'''


def descriptive_analysis(df):
    
    print('Desciption')
    display( df.describe())
    
    print('Information\n')
    display( df.info())
    
    print('skewness: ')
    display( df.skew().sort_values(ascending=False))
    
    print('kurtosis:')
    display(df.kurt())
    
    print('Spread of the data: ')
    display(df.std().sort_values(ascending=False))
    
    print('Variance:')
    display(df.var().sort_values(ascending = False))
    
    print('Maximum value in each feature:')
    display(df.max())
    
    print('minimum value in each feature:')
    display(df.min())