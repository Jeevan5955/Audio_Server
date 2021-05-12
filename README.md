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
 
 
### Results:

##### Song List & Add Song

![Home page](https://user-images.githubusercontent.com/54932235/117993421-5982b200-b35d-11eb-8673-ccd8fe322479.png)


##### Podcast List & Add Podcast

![podcast](https://user-images.githubusercontent.com/54932235/117993506-6e5f4580-b35d-11eb-8e52-2c6d41a34f28.png)

##### Audio-Book List & Add Audio-Book

![Audio-Book](https://user-images.githubusercontent.com/54932235/117993622-88992380-b35d-11eb-9c8f-532a9e2601cd.png)

##### Update

![Update](https://user-images.githubusercontent.com/54932235/117993747-9fd81100-b35d-11eb-9bfc-19e7d6f40eac.png)

## API End Points

#### Create 
#####  Example ``` 127.0.0.1/create/podcast```

##### i) ```<domain>/create/<audioFileType>```

![127 0 0 1_8000_create_podcast](https://user-images.githubusercontent.com/54932235/117994334-17a63b80-b35e-11eb-865e-fe3cbf577c5b.png)

#### Delete

#####  ```<domain>/delete/<audioFileType>/<audioFileID>```

![127 0 0 1_8000_delete_song_4](https://user-images.githubusercontent.com/54932235/117994561-445a5300-b35e-11eb-9464-4ee404cbf605.png)

![127 0 0 1_8000_delete_song_4 (1)](https://user-images.githubusercontent.com/54932235/117994448-2ee52900-b35e-11eb-96ec-4b3c721c2820.png)

#### Update

#####  ```<domain>/update/<audioFileType>/<audioFileID>```

#####  Example ``` 127.0.0.1```

![127 0 0 1_8000_update_podcast_2](https://user-images.githubusercontent.com/54932235/117994826-6fdd3d80-b35e-11eb-963a-d7b42f4235b6.png)

![127 0 0 1_8000_update_podcast_2 (1)](https://user-images.githubusercontent.com/54932235/117994856-753a8800-b35e-11eb-987b-6c1f14e538fa.png)

#### Get



##### Get complete list on songs/podcast/audiobook:

#####  ```<domain>/<audioFileType>```

![127 0 0 1_8000_song](https://user-images.githubusercontent.com/54932235/117995048-a1560900-b35e-11eb-8045-ce43091a3fd3.png)

##### Get particular songs/podcast/audiobook:

#####  ```<domain>/<audioFileType>/<audioFileID>```

![127 0 0 1_8000_song_2](https://user-images.githubusercontent.com/54932235/117995254-cea2b700-b35e-11eb-8b6e-25d7d823d8c0.png)









 

