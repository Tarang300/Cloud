import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Gender':0, 'self_employed':0, 'family_history':0, 'treatment':1,
       'work_interfere':1, 'no_employees':4, 'remote_work':0, 'tech_company':1,
       'benefits':2, 'care_options':1, 'wellness_program':1, 'seek_help':2,
       'anonymity':2, 'leave':2, 'mental_health_consequence':1,
       'phys_health_consequence':1, 'coworkers':1, 'supervisor':2,
       'mental_health_interview':1, 'phys_health_interview':0,
       'mental_vs_physical':2, 'obs_consequence':0, 'age_bin':3})

print(r.json())