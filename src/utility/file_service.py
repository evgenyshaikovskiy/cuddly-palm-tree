import os


# this creates space to add new features, such as multiple savings, loading
# literally car simulation database
class File_Service():
    def __init__(self):
        pass

    def delete_car_saves(self):
        os.remove('car_information.txt')
