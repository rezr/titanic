#coding:latin-1
import utilities as util
import prepare_data as prep
from sklearn.ensemble import RandomForestClassifier

train= util.get_train_df()
#fill
train=prep.get_fill_df("Age",train,type='numeric',verbose=True)
train=prep.get_fill_df("Embarked",train,type='categorical',verbose=True)
#recode
train=prep.get_recode_df("Sex",train,type='categorical',verbose=True)
train=prep.get_recode_df("Embarked",train,type='categorical',verbose=True)
#drop
train=prep.drop_column_df(["Name","Cabin","Ticket"],train)
print(train.tail())
test= util.get_test_df()

#fill
test=prep.get_fill_df("Age",test,type='numeric',verbose=True)
test=prep.get_fill_df("Embarked",test,type='categorical',verbose=True)
#recode
test=prep.get_recode_df("Sex",test,type='categorical',verbose=True)
test=prep.get_recode_df("Embarked",test,type='categorical',verbose=True)
#drop
test=prep.drop_column_df(["PassengerId","Name","Cabin","Ticket"],test)

forest = RandomForestClassifier(n_estimators=50,oob_score=True)
print(train.iloc[1:,3:].tail())
forest = forest.fit(train.iloc[1:,3:],train.iloc[1:,2])
print(train.iloc[1:,3:])
print(forest.feature_importances_)
print(forest.oob_score_)
