import mod1
config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": ""
}

firebase_upload = mod1.lets_do_it(config)

store_img = firebase_upload.storage()
store_img.child("/d.png").put("d.png")
