import pytest
from django.test import TestCase
from django.db.utils import DataError, IntegrityError
from django.contrib.auth import get_user_model

from .models import Bloc, Class, Keyword, Set, Card, CardKeyword, Supertype, Subtype, Stat, Talent, Type

@pytest.fixture
def setup():
    Stat.objects.create(name='Pitch')
    Stat.objects.create(name='Cost')
    Stat.objects.create(name='Power')
    Stat.objects.create(name='Defense')
    Talent.objects.create(name='Light')
    Talent.objects.create(name='Shadow')
    Type.objects.create(name='Action')
    Type.objects.create(name='Instant')
    Class.objects.create(name='Ninja')
    Class.objects.create(name='Generic')
    Class.objects.create(name='Brute')
    Subtype.objects.create(name='Aura')
    Subtype.objects.create(name='Item')
    Subtype.objects.create(name='Trap')
    Supertype.objects.create(name='Ice')
    Supertype.objects.create(name='Lightning')
    Keyword.objects.create(name='Go again', description='Gain an action point when the card resolves.')
    Keyword.objects.create(name='Dominate', description='The defending player cannot defend with more than one card from hand.')
    Bloc.objects.create(name='Welcome to Rathe', description='The og')
    Bloc.objects.create(name='Arcane Rising', description='The magical one')

@pytest.mark.django_db
class TestSets:
    def test_set_create(self):
        s = Set.objects.create(name='Welcome to Rathe', id='WTR')
        s.save()
        assert Set.objects.count() == 1

    def test_set_tag_too_long(self):
        with pytest.raises(DataError, match='.* too long .*'):
            s = Set.objects.create(name='Iorem Set', id='IOREMIPSUMAXIMUM')

    def test_set_empty_fields(self):
        pass # TODO: Use drf to ensure that empty fields won't exist in the db

@pytest.mark.django_db
@pytest.mark.usefixtures('setup')
class TestCards:        
    def test_card_create(self):
        c = Card.objects.create(
            name='Snatch',
            text='If Snatch hits, draw a card',
            _class=Class.objects.get(name='Generic'),
            _type=Type.objects.get(name='Action'),
            bloc=Bloc.objects.get(name='Welcome to Rathe')
        )
        c.save()
        assert Card.objects.count() == 1
        assert c.is_banned_cc == False
        assert c.is_banned_blitz == False
    
    def test_card_unique(self):
        c1 = Card.objects.create(
            name='Snatch',
            text='If Snatch hits, draw a card',
            _class=Class.objects.get(name='Generic'),
            _type=Type.objects.get(name='Action'),
            bloc=Bloc.objects.get(name='Welcome to Rathe')
        )
        c1.save()
        with pytest.raises(IntegrityError, match='.* violates unique constraint .*'):
            c2 = Card.objects.create(
                name='Snatch',
                text='If Snatch hits, draw a card',
                _class=Class.objects.get(name='Generic'),
                _type=Type.objects.get(name='Action'),
                bloc=Bloc.objects.get(name='Welcome to Rathe')
            )
            c2.save()

    def test_banned_card_create(self):
        c = Card.objects.create(
            name='Snatch',
            text='If Snatch hits, draw a card',
            _class=Class.objects.get(name='Generic'),
            _type=Type.objects.get(name='Action'),
            bloc=Bloc.objects.get(name='Welcome to Rathe'),
            is_banned_cc=True,
            is_banned_blitz=True
        )
        c.save()
        assert c.is_banned_cc == True
        assert c.is_banned_blitz == True

    def test_keyworded_cards_create(self):
        c = Card.objects.create(
            name='Snatch',
            text='If Snatch hits, draw a card',
            _class=Class.objects.get(name='Generic'),
            _type=Type.objects.get(name='Action'),
            bloc=Bloc.objects.get(name='Welcome to Rathe')
        )
        c.save()
        assert c.talent==None
        ck1 = CardKeyword.objects.create(card=c, keyword=Keyword.objects.get(name='Go again'))
        ck1.save()
        assert ck1.card == c
        assert ck1.keyword == Keyword.objects.get(name='Go again')
        ck2 = CardKeyword.objects.create(card=c, keyword=Keyword.objects.get(name='Dominate'))
        ck2.save()
        assert c.cardkeyword_set.count() == 2
        assert Keyword.objects.get(name='Go again').cardkeyword_set.count() == 1
        assert Keyword.objects.get(name='Dominate').cardkeyword_set.count() == 1

        c2 = Card.objects.create(
            name='Head Jab',
            text='',
            _class=Class.objects.get(name='Ninja'),
            _type=Type.objects.get(name='Action'),
            bloc=Bloc.objects.get(name='Welcome to Rathe'),
            talent=None
        )
        c2.save()
        ck3 = CardKeyword.objects.create(card=c2, keyword=Keyword.objects.get(name='Go again'))
        ck3.save()
        assert c2.cardkeyword_set.count() == 1
        assert Keyword.objects.get(name='Go again').cardkeyword_set.count() == 2
        assert Keyword.objects.get(name='Dominate').cardkeyword_set.count() == 1
        assert Keyword.objects.count() == 2
        assert Card.objects.count() == 2
        assert CardKeyword.objects.count() == 3

    def test_talent_card_create(self):
        c = Card.objects.create(
            name='Snatch',
            text='If Snatch hits, draw a card',
            _class=Class.objects.get(name='Generic'),
            _type=Type.objects.get(name='Action'),
            bloc=Bloc.objects.get(name='Welcome to Rathe'),
            talent=Talent.objects.get(name='Light')
        )
        c.save()
        assert c.talent == Talent.objects.get(name='Light')

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