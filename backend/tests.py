from django.test import TestCase
import pytest
from .models import Set

@pytest.mark.django_db
def test_set_create():
    s = Set(name="Welcome to Rathe", tag="WTR")
    s.save()
    assert Set.objects.count() == 1