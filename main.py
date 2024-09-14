class employee:

    # Initializing (Constructor)
    def __init__(self):
        print('Employee created.')

    #Deleting (Destructor)
    def __del__(self):
        obj = employee()
        del obj

