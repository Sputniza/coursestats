import sys
sys.stderr = sys.stdout
import urllib, urllib2, json
from dateutil.relativedelta import relativedelta
import cgi, cgitb


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

courseId = raw_input ("Please, enter a course Id: ")
user_list = getUserList (courseId)
users = user_list.split(",")
print "Users participating in this course are: "
for user in users :
    print user[1:-1]
