import pytest
from django.test import TestCase
from django.db.utils import DataError, IntegrityError
from django.contrib.auth import get_user_model

from .models import Set, Card

@pytest.mark.django_db
class TestSets:
    def test_set_create(self):
        s = Set.objects.create(name="Welcome to Rathe", tag="WTR")
        s.save()
        assert Set.objects.count() == 1

    def test_set_tag_too_long(self):
        with pytest.raises(DataError, match=".* too long .*"):
            s = Set.objects.create(name="Iorem Set", tag="IOREMIPSUM")

    def test_set_empty_fields(self):
        pass # TODO: Use drf to ensure that empty fields won't exist in the db

@pytest.mark.django_db
class TestCards:
    def test_card_create(self):
        s = Card.objects.create_card(name='Snatch', text='If Snatch hits, draw a card', _class=Card.Class.GENERIC, _type=Card.Type.ATTACK_ACTION, pitch=1)
        s.save()
        assert Card.objects.count() == 1
        assert s.is_banned == False
    
    def test_card_unique(self):
        s1 = Card.objects.create_card(name='Snatch', text='If Snatch hits, draw a card', _class=Card.Class.GENERIC, _type=Card.Type.ATTACK_ACTION, pitch=1)
        s1.save()
        with pytest.raises(IntegrityError, match=".* violates unique constraint .*"):
            s2 = Card.objects.create_card(name='Snatch', text='If Snatch hits, draw a card', _class=Card.Class.GENERIC, _type=Card.Type.ATTACK_ACTION, pitch=1)
            s2.save()

    def test_banned_card_create(self):
        s = Card.objects.create_card(name='Snatch', text='If Snatch hits, draw a card', _class=Card.Class.GENERIC, _type=Card.Type.ATTACK_ACTION, pitch=1, is_banned=True)
        s.save()
        assert s.is_banned == True

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)