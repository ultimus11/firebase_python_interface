import mod1
config = {
    "apiKey": "AIzaSyCoU34ezqb7B5JLOhMhfj0IU5JFIoAwBos",
    "authDomain": "frutcon-2cf1d.firebaseapp.com",
    "databaseURL": "https://frutcon-2cf1d.firebaseio.com",
    "projectId": "frutcon-2cf1d",
    "storageBucket": "frutcon-2cf1d.appspot.com",
    "messagingSenderId": "774855078271"
}

firebase_upload = mod1.lets_do_it(config)

store_img = firebase_upload.storage()
store_img.child("/d.png").put("d.png")