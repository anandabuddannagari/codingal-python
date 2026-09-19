#disctionary of students(id -> details)
students_data = {
    "id1": {"name": "Sara", "class":"v", "subject_integration":"english, math, science"},
    "id2":{"name":"david","class":"v","subject_integration":"english,math,science"},
    "id3":{"name":"Sara","class":"v", "sunject_integration":"english,math,ecience"},
    "id4":{"name":"Surya","class":"v", "subject_integration":"english,math,science"},
}
result ={}
seen_keys = [] #using a list instead of a set
for students_id, details in students_data.items():
    unique_key= (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[students_id]=details

    #print output line by line
for k,v in result.items():
    print(k, ":",v)

