from sklearn.metrics import confusion_matrix

# 아델리: 'A'
# 친스트랩(아델리 아닌것): 'C'

y_true = np.array(['A', 'A', 'C', 'A', 'C', 'C', 'C'])
y_pred = np.array(['A', 'C', 'A', 'A', 'A', 'C', 'C'])

confusion_matrix(y_true=y_true, 
                 y_pred=y_pred,
                 labels=["A", "C"])

