from distutils.log import error
from django.shortcuts import render
from .models import Note

from django.shortcuts import redirect

# Create your views here.
def home_view(request):
    DB = Note()

    notes = Note.objects.raw('SELECT * FROM Notes_note')
    dict_notes = {'notes': notes}


    if request.POST:
        if request.POST['description_field']:
            DB.note_Title = request.POST['title_field']
            DB.note_description = request.POST['description_field']
            DB.finished_note = False
            DB.save()

            return redirect('/notes')

        else:
            print('Un error ha ocurrido :(')



    return render(request, 'home.html', dict_notes)



def delete_post(request, id):
    delete_id = Note.objects.get(id = id)
    delete_id.delete()


    return redirect('/notes')


def mark_task(request, id):
    mark_id = Note.objects.get(id = id)

    if Note.objects.filter(id = id).get().finished_note == False:
        Note.objects.filter(id = id).update(finished_note = True)

    else:
        Note.objects.filter(id = id).update(finished_note = False)


    return redirect('/notes')





def edit_task(request, id):
    dict_edit = {}

    title_field_get = Note.objects.filter(id = id).get().note_Title
    description_field_get = Note.objects.filter(id = id).get().note_description


    dict_edit['title_field'] = title_field_get
    dict_edit['description_field'] = description_field_get

    dict_edit['id'] = id




    print(dict_edit)
    return render(request, 'edit.html', dict_edit)



def edit_task_post(request, id):

    title_field_get = Note.objects.filter(id = id).get().note_Title
    description_field_get = Note.objects.filter(id = id).get().note_description


    if request.POST:

        Note.objects.filter(id = id).update(note_Title = request.POST['title_field'], note_description = request.POST['description_field'])

        return redirect('/notes')
