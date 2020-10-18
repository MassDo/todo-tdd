import time 
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 1 - Scénario "Robert découvre le site":
        # Etant donné Robert,
        #  un visiteur qui a entendu parler de notre site
        # Quand il saisit l'url de notre site via son navigateur
        self.browser.get('http://localhost:8000')
        # Alors il peut lire "To-Do" dans l'onglet,        
        self.assertIn('To-Do', self.browser.title)
        # Et dans un header sur la page.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # Et on lui propose de saisir une note de texte.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 2 - Scénario "Robert ajoute une note":
        # Etant donné Robert (toujours lui !)
        #  un visiteur sur notre page d'accueil.
        # Quand il ajoute du texte ("Acheter du pain"), 
        #  dans la zone de texte
        inputbox.send_keys('Acheter du pain')
        # Et qu'il appuie sur entrée
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # Alors sa note est ajoutée dans un tableau,
        #  sur la même page avec le numéro de la note devant.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(r.text == '1: Acheter du pain' for r in rows)
        )
        
        # Echec volontaire du test
        self.fail('Finish the test!')
        # [suite des scénarios pour plus tard ...]

if __name__ == '__main__':
    unittest.main()
