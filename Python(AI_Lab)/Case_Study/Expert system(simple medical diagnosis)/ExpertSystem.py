#Program: 
 
class SymptomChecker: 
    def __init__(self): 
        self.symptoms = { 
            'fever': False, 
            'cough': False, 
            'headache': False, 
            'nausea': False, 
            'fatigue': False, 
            'shortness_of_breath': False, 
            'muscle_aches': False, 
            'sore_throat': False, 
        } 
 
    def get_user_input(self): 
        for symptom in self.symptoms: 
            response = input(f"Do you have {symptom.replace('_', ' ')}? (yes/no): ").lower() 
            self.symptoms[symptom] = response == 'yes' 
 
    def diagnose(self): 
        if self.symptoms['fever'] and self.symptoms['cough']: 
            if self.symptoms['headache'] and self.symptoms['muscle_aches']: 
                print("You may have the flu.") 
            elif self.symptoms['shortness_of_breath'] and self.symptoms['fatigue']: 
                print("You may have COVID-19. Consult a doctor.") 
            else: 
                print("You may have a common cold.") 
        elif self.symptoms['sore_throat'] and self.symptoms['fatigue']: 
            print("You may have a viral infection. Rest and consult a doctor.") 
        elif self.symptoms['nausea']: 
            print("You may have a stomach bug.") 
        else: 
            print("No specific diagnosis. Consult a doctor for more information.") 
 
if __name__ == "__main__": 
    print("Welcome to the Symptom Checker!") 
    checker = SymptomChecker() 
    checker.get_user_input() 
    print("\nDiagnosis Result:") 
    checker.diagnose() 
 
 
 
'''
Output: 
 
Welcome to the Symptom Checker! 
Do you have fever? (yes/no): yes 
Do you have cough? (yes/no): yes 
Do you have headache? (yes/no): no 
Do you have nausea? (yes/no): no 
Do you have fatigue? (yes/no): no 
Do you have shortness of breath? (yes/no): no 
Do you have muscle aches? (yes/no): no 
Do you have sore throat? (yes/no): no 
Diagnosis Result: 
You may have a common cold. 
'''