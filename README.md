# RESTful API with Python BBD using behave package

1) Builded personal API (STORE API)
    >> using RESTful API, Flask, Flask_restful, flask_jwt_extended, Flask_SQLAlchemy, 
    >>> Model => User, Item, Store
   
2) build RESTful API using BDD framework for testing
    >> create storeAPI for "User register and Login"
    >>> once login then it will auto delete user from server
                                                                                                                >
## steps to follow
 1) run STORE API ('D:\Python\Udemy_Courses\rest_api_flask_python\rest_api_python_3\python_section\adv_code>')
 2) once API up and running 
    >> go to ('D:\Python\Udemy_Courses\rest_api_backend_BDD_python\personal_api_store_project>')
    >>>activate virtualenv >> venv\Scripts\activate
    >>>> run scripts => behave features/userAPI.feature --no-capture
 3) User will register and able to login;                                                                                                                   
   >> once @login tag completed then it will trigger Environemnt.py file to destroy user_register data from server.
