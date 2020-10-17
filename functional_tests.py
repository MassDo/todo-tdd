from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Scénario "Robert découvre le site":
        # Etant donné Robert un visiteur qui a entendu parler de notre site
        # Quand il saisit l'url de notre site via son navigateur
        self.browser.get('http://localhost:8000')
        # Alors il peut lire "To-Do" dans l'onglet
        self.assertIn('To-Do', self.browser.title)
        # Echec volontaire du test
        self.fail('Finish the test!')
        # Et on lui propose de saisir une note de texte.


        # [suite des scénarios pour plus tard ...]

if __name__ == '__main__':
    unittest.main()
