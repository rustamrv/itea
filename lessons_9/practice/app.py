from flask import Flask, render_template, redirect, request, url_for
from models import Student, Faculty, Group, Curator, RateList

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    rows = Student.objects
    return render_template('index.html', students=rows)


@app.route('/detail_student/<string:student_id>')
def get_detail_student(student_id):
    student = Student.objects(id=student_id)
    try:
        rates = RateList.objects(student=student[0])
        data = {
            "student": student[0],
            "rates": rates,
            "show": True,
        }
        return render_template('detail_student.html', **data)
    except IndexError:
        return render_template('error.html', error=f'Not found student with id {student_id}')


@app.route('/delete_student/<string:student_id>')
def delete_student(student_id):
    student = Student.objects(id=student_id)
    student.delete()
    return redirect(url_for('index'))


@app.route('/update/<string:student_id>', methods=['GET'])
def update_student(student_id):
    student = Student.objects(id=student_id)
    faculties = Faculty.objects
    groups = Group.objects
    curators = Curator.objects
    data = {
        "student": student[0],
        "faculties": faculties,
        "groups": groups,
        "curators": curators,
        "show": False,
    }
    return render_template('detail_student.html', **data)


@app.route('/update_student/<string:student_id>', methods=['post'])
def update_student_save(student_id):
    student = Student.objects.get(id=student_id)
    faculties = Faculty.objects
    groups = Group.objects
    curators = Curator.objects
    data = {
        "student": student,
        "faculties": faculties,
        "groups": groups,
        "curators": curators,
        "show": True,
    }
    data_form = dict(request.form)
    student.first_name = data_form['first_name']
    student.last_name = data_form['last_name']
    student.group = Group.objects.get(id=data_form['groups'])
    student.faculty = Faculty.objects.get(id=data_form['faculty'])
    student.curator = Curator.objects.get(id=data_form['curators'])

    student.save()
    return render_template('detail_student.html', **data)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == "GET":
        faculties = Faculty.objects
        groups = Group.objects
        curators = Curator.objects
        data = {
            "faculties": faculties,
            "groups": groups,
            "curators": curators,
        }
        return render_template('add_student.html', **data)
    else:
        data_form = dict(request.form)
        student = Student()
        student.first_name = data_form['first_name']
        student.last_name = data_form['last_name']
        student.group = Group.objects.get(id=data_form['groups'])
        student.faculty = Faculty.objects.get(id=data_form['faculty'])
        student.curator = Curator.objects.get(id=data_form['curators'])
        student.save()
        return redirect(url_for('index'))


@app.route('/list_faculties', methods=['GET', 'POST'])
def list_faculties():
    if request.method == "GET":
        faculties = Faculty.objects
        return render_template('list_faculties.html', faculties=faculties, show=False)
    else:
        data_form = dict(request.form)
        faculty = Faculty.objects.get(id=data_form['faculties'])
        students = Student.objects(faculty=faculty)
        result = []
        for i in students:
            rate_list = RateList.objects(student=i, rate=5)
            res = {
                'student': i,
                'rate': rate_list.average('rate')
            }
            result.append(res)

        data = {
            "faculties":  Faculty.objects,
            "faculty": faculty,
            "rate_list": result,
            "show": True
        }
        return render_template('list_faculties.html', **data)


@app.route('/list_curators', methods=['GET', 'POST'])
def list_curators():
    if request.method == "GET":
        curators = Curator.objects
        return render_template('list_curators.html', curators=curators, show=False)
    else:
        data_form = dict(request.form)
        curator = Curator.objects.get(id=data_form['curators'])
        students = Student.objects(curator=curator)
        data = {
            "curators": Curator.objects,
            "curator": curator,
            "students": students,
            "show": True
        }
        return render_template('list_curators.html', **data)


if __name__ == "__main__":
    app.run(debug=True)