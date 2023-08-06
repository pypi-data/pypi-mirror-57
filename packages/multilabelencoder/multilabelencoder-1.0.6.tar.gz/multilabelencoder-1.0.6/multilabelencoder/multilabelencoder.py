import pickle
from sklearn.preprocessing import LabelEncoder
import bisect

#customized label encoder
class MultiColumnLabelEncoder:
    def __init__(self, columns = None):
        # list of column to encode
        self.columns = columns 
        #initialize dictionary of labels
        self.classes_ = {} 
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''        
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                print('column', col)
                encoder = LabelEncoder()
                output[col] = encoder.fit_transform(output[col])
                encoder_classes = encoder.classes_.tolist()
                #insert other as label to handle unrecognized labels from test data
                bisect.insort_left(encoder_classes, 'other')
                self.classes_[col]= encoder_classes
                
        else:
            for colname, col in output.iteritems():
                encoder = LabelEncoder()
                output[colname] = encoder.fit_transform(col)
                self.classes_[col]= encoder.classes_.tolist()
                #insert other as label to handle unrecognized labels from test data
                bisect.insort_left(encoder_classes, 'other')
                self.classes_[col]= encoder_classes        
        return output 

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)
    def save(self, fileName):
        """Save thing to a file."""
        f = open(fileName,"wb")
        pickle.dump(self,f)
        f.close()
    def load(fileName):
        """Return a thing loaded from a file."""
        f = open(fileName,"r")
        obj = pickle.load(f)
        f.close()
        return obj
    # make load a static method
    load = staticmethod(load)
