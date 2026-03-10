from django.shortcuts import render


def home(request):
    return render(request, 'app1/home.html')


def about(request):
    developer = 'Abdullah'
    return render(request, 'app1/about.html', context = {'developer': developer})


def info(request):
    data = {
        'name': 'Django',
        'version': '6.0',
        'release_date': 'December 7, 2023',
    }
    data_stu = {"stu1": {"name": "Alice", "age": 20},
                "stu2": {"name": "Bob", "age": 22},
                "stu3": {"name": "Charlie", "age": 21},
                "stu4": {"name": "David", "age": 23},
                "stu5": {"name": "Eve", "age": 20}}
    return render(request, 'app1/info.html')
    # return render(request, 'app1/info.html', context = {'data': data)
    # return render(request, 'app1/info.html', context = {'data_stu': data_stu})

def contact(request):
    return render(request, 'app1/contact.html')