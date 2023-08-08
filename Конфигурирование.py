class User:
    def __init__(self, group: str):
        self.group = group

def process_admin_request(user, request): pass
def process_manager_request(user, request): pass
def process_client_request(user, request): pass

user = User(group="admin")
request = ""

# Вариант 1. Запускаем нужную функцию путем выбора в условном операторе
if user.group == "admin":
    process_admin_request(user, request)
elif user.group == "manager":
    process_manager_request(user, request)
elif user.group == "client":
    process_client_request(user, request)

# Вариант 2.
# Создаем словарь и указываем соответствие между значением аргумента и названием соответствующей функции
group_to_process_method = {
    "admin": process_admin_request,
    "manager": process_manager_request,
    "client": process_client_request
}

group_to_process_method[user.group](user, request)

