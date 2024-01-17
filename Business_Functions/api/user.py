import requests

class User:

    def post_user(self):
        
        data = {
                 "name": "morpheus",
                 "job": "leader"
                }
        
        self.response = requests.post("https://reqres.in/api/users",data)
        assert self.response.status_code == 201, self.response.status_code

    def verify_post_user(self):    
        response_text = self.response.json()
        assert response_text["name"] == "morpheus",response_text["name"]
        assert response_text["job"] == "leader",response_text["job"]
        assert int(response_text["id"]) > 0, (response_text["id"]) 
        assert type(response_text["createdAt"]) == str,type(response_text["createdAt"])

       

    
    def get_user_by_id(self,user_id):
        self.response = requests.get("https://reqres.in/api/users/"+ str(user_id))
        assert self.response.status_code == 200, self.response.status_code 

    def verify_get_user_by_id(self, user_id):
        expected_response = {
                            "data": {
                                "id": user_id,
                                "email": "janet.weaver@reqres.in",
                                "first_name": "Janet",
                                "last_name": "Weaver",
                                "avatar": "https://reqres.in/img/faces/2-image.jpg"
                            },
                            "support": {
                                "url": "https://reqres.in/#support-heading",
                                "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
                            }
                        }
        
        assert self.response.json() == expected_response, self.response


    


    




