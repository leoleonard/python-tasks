import requests


# Uzupełnij funkcję get_post_body tak, aby zwracała treść postu o
# zadanym id
# URL: http://jsonplaceholder.typicode.com/posts/<post_id>
def get_post_body(post_id):
    url = 'http://jsonplaceholder.typicode.com/posts/{0}'.format(post_id)
    r = requests.get(url)
    if r.status_code == 200:
        if 'content-type' in r.headers and 'application/json' in r.headers['content-type']:
            data = r.json()
    return data['body']

# Uzupełnij funkcję get_commenters_data w taki sposób, aby
# zwracała listę krotek, zawierających imię i nazwisko komentującego
# oraz jego adres e-mail
# URL: http://jsonplaceholder.typicode.com/posts/<post_id>/comments
def get_commenters_data(post_id):
    commenters_data = []
    url = 'http://jsonplaceholder.typicode.com/posts/{0}/comments'.format(post_id)
    r = requests.get(url)
    if r.status_code == 200:
        if 'content-type' in r.headers and 'application/json' in r.headers['content-type']:
            comments = r.json()
    for comment in comments:
        commenters_data.append((comment['name'], comment['email']))
    return commenters_data

# Uzupełnij funkcję get_user_posts w taki sposób, aby zwracała listę
# tematów postów użytkownika o zadanym id
# URL: https://jsonplaceholder.typicode.com/posts?userId=<user_id>
#
# Podpowiedź: Opis przekazywania parametrów do zapytań GET znajduje się tutaj:
# http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
def get_user_posts(user_id):
    query = {'user_id': user_id}
    post_titles = []
    url = 'http://jsonplaceholder.typicode.com/posts'
    r = requests.get(url, params=query)
    if r.status_code == 200:
        if 'content-type' in r.headers and 'application/json' in r.headers['content-type']:
            posts = r.json()
    for post in posts:
        post_titles.append(post['title'])
    return post_titles

if __name__ == '__main__':
    print(get_post_body(10))
    print('=' * 20)
    print(get_commenters_data(10))
    print('=' * 20)
    print(get_user_posts(1))
