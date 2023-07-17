# program to show how the module can be imported. 
from prediction import predict
 
#symptoms = ['Symptom_1', 'Symptom_2', 'Symptom_3']    # insert symptoms from dataset
symptoms = ['shivering','chills']
# predicting the disease
predict(symptoms)