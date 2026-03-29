from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializer import NoteSerializers

@api_view(["GET"])
def get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializers(notes,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_post(request):
    serializer = NoteSerializers(data=serializer.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["PUT"])
def update_note(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializers(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
def delete_note(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note Deleted")
