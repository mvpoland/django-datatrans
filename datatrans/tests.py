from django.core.cache import cache
from django.test import TestCase
from django.utils import translation
from django.contrib.contenttypes.models import ContentType

from datatrans.models import KeyValue, make_digest
from test_project.testapp.models import Option


class DatatransTests(TestCase):
    def setUp(self):
        self.nl = "nl"
        self.en = "en"
        self.name_en = "Message in English"
        self.name_nl = "Bericht in het Nederlands"
        self.field = "name"
        self.instance = Option.objects.create(name=self.name_en)

    def test_default_values(self):
        value = KeyValue.objects.lookup(
            self.name_en, self.nl, self.instance, self.field
        )
        self.assertEqual(value, self.name_en)

        kv = KeyValue.objects.get_keyvalue(
            self.name_en, self.nl, self.instance, self.field
        )
        kv.value = self.name_nl
        kv.save()

        value = KeyValue.objects.lookup(
            self.name_en, self.nl, self.instance, self.field
        )
        self.assertEqual(value, self.name_en)

        kv.edited = True
        kv.save()

        value = KeyValue.objects.lookup(
            self.name_en, self.nl, self.instance, self.field
        )
        self.assertEqual(value, self.name_nl)

    def test_cache(self):
        digest = make_digest(self.name_en)
        type_id = ContentType.objects.get_for_model(self.instance.__class__).id
        cache_key = "datatrans_{}_{}_{}_{}_{}".format(
            self.nl, digest, type_id, self.instance.id, self.field
        )

        self.assertEqual(cache.get(cache_key), None)

        translation.activate(self.nl)

        kv = KeyValue.objects.get_keyvalue(
            self.name_en, self.nl, self.instance, self.field
        )
        self.assertEqual(cache.get(cache_key).value, self.name_en)
        kv.value = self.name_nl
        kv.save()
        kv = KeyValue.objects.get_keyvalue(
            self.name_en, self.nl, self.instance, self.field
        )
        self.assertEqual(cache.get(cache_key).value, self.name_nl)
        kv.value = "{}2".format(self.name_nl)
        kv.save()
        self.assertEqual(cache.get(cache_key).value, "{}2".format(self.name_nl))
        kv.delete()
        self.assertEqual(cache.get(cache_key), None)

    def test_fuzzy(self):
        kv = KeyValue.objects.get_keyvalue(
            self.name_en, self.nl, self.instance, self.field
        )
        kv.value = self.name_nl
        kv.edited = True
        kv.fuzzy = True
        kv.save()

        value = KeyValue.objects.lookup(
            self.name_en, self.nl, self.instance, self.field
        )
        self.assertEqual(value, self.name_nl)
