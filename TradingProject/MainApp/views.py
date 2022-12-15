from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import uploadform
import csv
# json_data = []
# from somewhere import handle_uploaded_file

def upload_file(request):
    
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        form = uploadform(request.POST, request.FILES)
        csv_file = request.FILES['csv_file']
        file_data = csv_file.read().decode("utf-8")
        file_lines = file_data.split('\n')
        json_data = []
        for line in file_lines:
            if line != '':
                data = line.split(',')
                dict = {}
                dict['Bank_Nifty'] = data[0]
                dict['Date'] = data[1]
                dict['Time'] = data[2]
                dict['Open'] = data[3]
                dict['High'] = data[4]
                dict['Low'] = data[5]
                dict['Close'] = data[6]
                dict['Volume'] = data[7]
                json_data.append(dict)
        print(json_data)
        return render (request, 'demo/home.html', {'json_data':json_data})
    else:
        json_data = ''
        form = uploadform()
    return render(request, 'demo/home.html', {'form': form, 'json_data':json_data})

# def json_data(request):
#     if request.method == 'POST':
#         if len(json_data)>0:
#             return render(request, 'demo/home.html', {'json_data':})