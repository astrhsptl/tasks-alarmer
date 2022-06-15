from django.contrib.auth.models import User

from website.models import Users_task, Users_tasks_broker


def add_task(title:str=None, discription:str=None, notification:str=None, users_id:int=None) -> None or Users_task:
    grehi = ['', None]
    if title.strip() in grehi or discription.strip() in grehi:
        return None
    else:
        new_task = Users_task(
            title=title, 
            discription=discription,
            notification=notification)
        new_task.save()
        print(new_task.pk)
        broker = Users_tasks_broker(task_id_id=new_task.pk, user_id_id=users_id)
        broker.save()

def get_concrete_user(
    username: str or None = None, 
    email: str or None = None, password: str or None = None,) -> User or None:
    
    if username and email is None or password is None:
        return None
    
    if username is None:
        try:
            take_user = User.objects.get(
                email=email,
                password=password,
            )
        except:
            print('exp from interaction')
    elif email is None:
        try:
            take_user = User.objects.get(
                username=username,
                password=password,
            )
        except:
            print('exp from interaction')
    
    return take_user

def create_new_user(username: str = None, 
    email: str = None, password: str = None,) -> User or None: 
    
    if username == None or email == None or password == None:  
        return None
    else:
        try:
            check = User.objects.get(email=email)
        except:
            check = None
        
        if check == None:
            try:
                new_user = User(username=username, email=email,
                password=password, is_active=False)
                return new_user
            except:
                return None
        else:
                return None

def confirming_user_account(username: str or None = None, 
    email: str or None = None, password: str or None = None,) -> True or False:
    get_user = get_concrete_user(username=username, 
    email=email, password=password)

    if get_user is not None:
        try:
            get_user.is_active = True
            get_user.save()
            return True
        except:
            return False
    
    else:
        return False