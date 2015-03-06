from django.test import TestCase

from coopInfo.models import Person , Cooperative

class PersonContentFileNameTest(TestCase):

    def testSubmitAJpegWithName(self):

        aPerson  = Person()
        currentFileName = "bob-19282.jpg"
        aPerson.name = "Bob Biture"

        aCoop = Cooperative()
        aCoop.id = 12

        aPerson.name = "Bob Biture"
        aPerson.coopId = aCoop 

        result = aPerson.content_file_name(currentFileName)
        self.assertEqual(result, "persons/BobBiture-12.jpg")