 # model relation



## library install

$ pip install django

$ pip install ipython

$ pip install django_extensions



## project & app

$ django-admin startproject model_relation .

 - model_relation/settings.py 수정

 - ```python
   #...
   INSTALLED_APPS = [
       # 3rd party apps
       'django_extensions',
   #...
   ]
   ```



$ python manage.py shell_plus

​	shell_plus 실행되는지만 확인



$ python manage.py startapp manytomany

 - model_relation/settings.py 수정

 - ```python
   #...
   INSTALLED_APPS = [
       # local apps
       'manytomany',
   #...
   ]
   ```



manytomany/models.py 수정



## migrate

$ python manage.py makemigrations

 - ```bash
   Migrations for 'manytomany':
     manytomany\migrations\0001_initial.py
       - Create model Doctor
       - Create model Patient
       - Create model Reservation$ python manage.py migrate
   ```

$ python manage.py migrate

$ python manage.py shell_plus

```bash
In [1]: doctor = Doctor.objects.create(name='jason')

In [2]: doctor
Out[2]: <Doctor: 1번 의사 jason>

In [3]: Doctor.objects.all()
Out[3]: <QuerySet [<Doctor: 1번 의사 jason>]>

In [4]: patient = Patient.objects.create(name='muzi')

In [5]: patient
Out[5]: <Patient: 1번 환자 muzi>

In [6]: Patient.objects.all()
Out[6]: <QuerySet [<Patient: 1번 환자 muzi>]>

In [7]: Reservation.objects.create(doctor=doctor, patient=patient)
Out[7]: <Reservation: 1번 의사의 1번 환자>

# 해당 의사가 갖고 있는 모든 patient 정보를 호출
# Reservation에서 Doctor를 ForeignKey로 잡고 있어서 사용 가능.
In [9]: doctor.reservation_set.all()
Out[9]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

In [10]: patient2 = Patient.objects.create(name='neo')

In [11]: Reservation.objects.create(doctor=doctor, patient=patient2)
Out[11]: <Reservation: 1번 의사의 2번 환자>

# 1번 의사가 patient, patient2 진료
In [12]: doctor.reservation_set.all()
Out[12]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>

In [15]: patient.reservation_set.all()
Out[15]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

In [13]: patient2.reservation_set.all()
Out[13]: <QuerySet [<Reservation: 1번 의사의 2번 환자>]>
```



##  중계모델 건너뛰고 참조하기

manytomany/models.py 수정

```python
#...
class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    # through : Reservation 을 통해 가져온다.
#...
```

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py shell_plus

```bash
In [1]: patient = Patient.objects.get(pk=1)

In [2]: patient
Out[2]: <Patient: 1번 환자 muzi>

In [3]: patient.reservation_set.all()
Out[3]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

# 중계 모델을 거치지 않고 의사 정보를 불러올 수 있다.
In [4]: patient.doctors.all()
Out[4]: <QuerySet [<Doctor: 1번 의사 jason>]>

In [5]: doctor = Doctor.objects.create(name='john')

In [6]: Reservation.objects.create(doctor=doctor, patient=patient)
Out[6]: <Reservation: 2번 의사의 1번 환자>

In [7]: patient
Out[7]: <Patient: 1번 환자 muzi>

In [8]: patient.reservation_set.all()
Out[8]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 2번 의사의 1번 환자>]>

In [9]: patient.doctors.all()
Out[9]: <QuerySet [<Doctor: 1번 의사 jason>, <Doctor: 2번 의사 john>]>

```



## 중계모델 건너뛰고 역참조하기

manytomany/models.py 수정

```python
class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(
        Doctor,
        through='Reservation',
        related_name='patients',  # patients 라는 이름으로 역참조 가능
    )
```

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py shell_plus

```bash
In [1]: doctor = Doctor.objects.get(pk=1)

In [2]: patient = Patient.objects.get(pk=1)

In [3]: patient.doctors.all()
Out[3]: <QuerySet [<Doctor: 1번 의사 jason>, <Doctor: 2번 의사 john>]>

# Patients
In [4]: doctor.patients.all()
Out[4]: <QuerySet [<Patient: 1번 환자 muzi>, <Patient: 2번 환자 neo>]>

```



## 중계모델 없이 참조하기

manytomany/models.py 수정

```python
#...
class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(
        Doctor,
        # through = 'Reservation',
        related_name='patients',  # patients 라는 이름으로 역참조 가능
    )
    # through : Reservation 을 통해 가져온다.
    
    def __str__(self):
        return f'{self.id}번 환자 {self.name}'

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'

```

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py shell_plus

```bash
In [1]: doctor = Doctor.objects.create(name='jason')

In [2]: patient = Patient.objects.create(name='neo')

In [5]: doctor.patients.add(patient)

In [6]: doctor.patients.all()
Out[6]: <QuerySet [<Patient: 1번 환자 neo>]>

In [7]: patient.doctors.all()
Out[7]: <QuerySet [<Doctor: 1번 의사 jason>]>

In [8]: patient2 = Patient.objects.create(name='test')

In [9]: doctor.patients.add(patient2)

In [10]: doctor.patients.all()
Out[10]: <QuerySet [<Patient: 1번 환자 neo>, <Patient: 2번 환자 test>]>

In [13]: patient.doctors.remove(doctor)

In [14]: patient.doctors.all()
Out[14]: <QuerySet []>

In [16]: doctor.patients.all()
Out[16]: <QuerySet [<Patient: 2번 환자 test>]>

In [17]: patient2.doctors.remove(doctor)

In [18]: doctor.patients.all()
Out[18]: <QuerySet []>
```

위의 중계모델 없이 참조하기는 
doctor, patient 끼리 참조하고자할 때는 유용하지만
진료시간, 진료장소 등 다른 정보를 같이 저장해야 할 경우엔
중계모델을 만들어 사용해야 한다.