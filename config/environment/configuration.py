class Configuration(): #TODO: consider if configurations can be made better than this
    #Apparently this makes it so that _Configuration can find the object.. Don't do that though
    __form_secret = 'super_secret_secret' 
    
    def __init__(self):
        pass
    def get_form_secret(self):
        return self.__form_secret