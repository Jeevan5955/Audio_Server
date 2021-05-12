# Audio_Server
 
 #### Setup:
 
 ##### 1.
 
 ##### i)  ```git clone https://github.com/Jeevan5955/Audio_Server.git```
 ##### ii) ```cd Audio_Server``` 
 ##### iii) ```  pip install -r requirements.txt```
 
 ##### 2.
 
 ##### i) Create a PostgreSQL database
 ##### Reference: https://www.postgresql.org/
 ##### ii) Open setting.py 
 ##### Path: Audio_Server/filled/setting.py
 ##### iii) Add PostgreSQL database details

 ```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  '*****',
        'USER': '****',
        'PASSWORD': '*****',
        'HOST': '*****',
        'PORT': 5432

    }
}
```

##### 3.

 ##### i)  ```python manage.py makemigrations```
 ##### ii) ```python manage.py migrate``` 
 ##### iii) ```python manage.py runserver```




 

