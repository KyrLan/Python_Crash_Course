
def make_car (mark, model, **user_info):
    profile = {}
    profile['Mark'] = mark
    profile['Model'] = model
    for key, value in user_info.items():
        profile[key] = value
    return profile

car = make_car('Ford', 'Fusion', color = 'blue', tow_package = True)
print(car)