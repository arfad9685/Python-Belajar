import json
json_string = '''
{
"id": 1,     
"name": "Arif",
"courses": ["Python", "Java"],
"age": 20
}'''
student_dict = json.loads(json_string)
print(student_dict)