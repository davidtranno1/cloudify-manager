def get_admin_user():
    return {
            'username': 'admin',
            'password': 'admin',
            'role': 'administrator'
    }


def get_test_users():
    test_users = [
        {
            'username': 'alice',
            'password': 'alice_password',
            'role': 'administrator'
        },
        {
            'username': 'bob',
            'password': 'bob_password',
            'role': 'default'
        },
        {
            'username': 'clair',
            'password': 'clair_password',
            'role': 'viewer'
        },
        {
            'username': 'dave',
            'password': 'dave_password',
            'role': 'suspended'
        },
        {
            'username': 'eve',
            'password': 'eve_password',
            'role': 'default'
        }
    ]
    return test_users
