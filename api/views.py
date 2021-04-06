from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Entry

@api_view(['POST'])
def add_entry(request):
    # {'name': 'Schalk',
    # 'surname': 'Olivier',
    # 'address': '3 tafelkop street',
    # 'question1': 'false',
    # 'question2': 'false',
    # 'temperature': '35.9'}

    data = request.data
    names = f"{data['name']} {data['surname']}"
    cell = data['cell']
    question1 = True
    question2 = True

    if data['question1'] == 'false':
        question1 = False
    
    if data['question2'] == 'false':
        question2 = False

    temperature = data['temperature']



    Entry.objects.create(
        names=names,
        cell=cell,
        question1=question1,
        question2=question2,
        temperature=temperature
    )

    return Response({"status": True})