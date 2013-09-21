import utilities as util
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

def feature_extractor():
    print("featureextractor")


def get_pipeline():
    print("selection variable")
    print("selection modele")
    
def main():
    print("Reading in the training data")
    train = util.get_train_df()
    
    #clean data
    
    
    #print("Extracting features and training model")
    #classifier = get_pipeline()
    classifier = RandomForestClassifier(n_estimators = 100)

    classifier.fit(train[0::,1::],train[0::,0])
    #print("Saving the classifier")
    util.save_model(classifier)
    
if __name__=="__main__":
    main()