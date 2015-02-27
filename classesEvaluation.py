def getUserList (courseId):
    """
    courseId: str 

    Returns a dict with key: UserID and value Username
    """
    language = "en"
    if courseId :
        api_query_url = "http://" + language + ".wikipedia.org/w/api.php?action=liststudents&format=json&courseids=" + courseId
        response = urllib2.urlopen(api_query_url)
        str_response = response.read()
        data = json.loads(str_response, "utf8" )
        users_data = data["students"]
        users = []
    for user in users_data:
        users.append(user["username"])
    user_list = '"' + '","'.join(users) + '"'
    # re-encode so that we can make a usable sql query string
    user_list = user_list.encode("utf8")
    # print user_list
    return user_list

class course(object):
    
    def __init__ (self, title, courseid):
        self.title = title
        self.id = courseid
        
    def __str__ (self):
        return (self.name+': ' + str(self.id))            
        
    def getId(self):
        return self.id
        
    def getTitle(self):
        return self.title
        
class user(object):
    
    def __init__(self, username):
        self.name = username
        
    def __str__ (self):        
        return self.name        
        
    def isParticipant(self, courseId):        
        return self.name in self.getUserlist(courseId)
        