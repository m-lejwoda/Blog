import json
import os
import pytest
from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from blogapp.models import Article
from blogapp.views import ArticleListView, LoginView

@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    return make_user


def test_login_url_is_returning_200(client):
    print(os.environ['SECRET_KEY'])
    print(os.environ['TEST_KEY'])
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


def test_dashboard_url_is_returning_200(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

def test_register_url_is_returning_200(client):
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200

def test_logout_url_is_returning_302(client):
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302

def test_archival_schedule_url_is_returning_200(client):
    url = reverse('archival_schedule')
    response = client.get(url)
    assert response.status_code == 200

def test_upcoming_schedule_url_is_returning_200(client):
    url = reverse('upcoming_schedule')
    response = client.get(url)
    assert response.status_code == 200

def test_all_news_url_is_returning_200(client):
    url = reverse('news')
    response = client.get(url)
    assert response.status_code == 200
# reverse('edit_project', kwargs={'project_id':4})

@pytest.mark.django_db
def test_post_detail_url_is_returning_200(client, create_user):
    # Post.objects.create(slug='test')
    user = create_user(username='test', email='foo@bar.com', password='bar')
    print(user)
    url = reverse('post_detail', kwargs={'slug': 'test'})
    response = client.get(url)
    assert response.status_code == 200




def test_dasboard_url_check_view():
    url = reverse('index')
    assert resolve(url).func.view_class == ArticleListView

def test_login_url_check_view():
    login_url = reverse('login')
    assert resolve(login_url).func.view_class == LoginView




@pytest.fixture(scope="session")
def fixture_1():
    print('run fixture 1')
    return 1


def test_example(fixture_1):
    print("example")
    num = fixture_1
    assert num == 1


def test_example1(fixture_1):
    print("example 2")
    num = fixture_1
    assert num == 1
