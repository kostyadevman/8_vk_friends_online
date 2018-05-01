import vk
import getpass

APP_ID = 1234567


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return getpass.getpass('Enter password: ')


def get_online_friends(login, password, api_version=5.52):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v=api_version)
    online_friends_ids = api.friends.getOnline()
    friends_online = api.users.get(
        user_ids=online_friends_ids,
        fields=['last_name', 'first_name']
    )
    return friends_online


def print_friends_to_console(friends_online):
    print('Friends online: ')
    for friend in friends_online:
        print('{} {}'.format(
            friend.get('first_name'),
            friend.get('last_name'))
        )


if __name__ == '__main__':
    try:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(login, password)
        print_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print('Invalid login or password')
