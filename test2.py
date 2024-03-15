from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd


driver = webdriver.Chrome()

# Spécifiez le chemin vers votre fichier Excel téléchargé localement
excel_file_path = '/home/fesia/testSelenium/selenium_env/DATA TEST CAP-IRVE (1).xlsx'

# Lisez le fichier Excel avec pandas
df_excel = pd.read_excel(excel_file_path)

# Configurer les options du navigateur
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialiser le navigateur
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://cap-irve-stage.digetit.com/")

# Remplir le formulaire de connexion
email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#email"))
) 
email_input.send_keys("natifesia@gmail.com")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(" natifesia-test@cap-irve-dev")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

## Aller sur la page "Nouveau Projet" avec une attente explicite
wait = WebDriverWait(driver, 10)
nouveau_projet_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1gactu1")))
nouveau_projet_button.click()



# Récupérer les données du premier projet à partir du DataFrame
projet_data = df_excel.iloc[0]

## Simuler le clic sur le "combobox" pour ouvrir la liste déroulante
combobox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "demo-simple-select"))
)
combobox.click()

# Sélectionner une option en cliquant sur l'élément li correspondant à l'option spécifique
option_to_select = "test"  # Remplacez par le texte de l'option que vous souhaitez sélectionner
option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//li[@role='option'][text()='{option_to_select}']"))
)
option.click()


# ... Continuer à remplir les autres champs avec les valeurs extraites du fichier Excel

nom_affaire_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="Nom_affaire"]'))
)
nom_affaire_input.send_keys("entreprise clairina")

# Remplir le champ "Date de Deadline"
date_deadline_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="Date_Deadline"]'))
)
date_deadline_input.clear()  # Effacer toute date existante
date_deadline_input.send_keys("2024-03-15")  # Remplacer par la date que vous souhaitez saisir (au format "YYYY-MM-DD")
# Remplir le champ "Addresse"
adresse_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="adresse"]'))
)
adresse_input.send_keys("Madagascar")

# Sélectionner une option dans le "combobox" pour "Prioritaire"
check_priotitaire = driver .find_element(By .ID, "mui-component-select-prioritaire")
check_priotitaire.click()

webdriver.ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()


submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/main/div[2]/div/div/div[2]/div/form/div/div[8]/div/button[2]')
submit_button.click()

#on commence par l' etape 2
# Remplir le champ "Type d'abonnement"
type_abonnement_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-typeAbonnement"))
)
type_abonnement_dropdown.click()  # Pour ouvrir la liste déroulante

# Sélectionner un élément spécifique dans la liste déroulante
specific_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-value="Vert"]'))  # Utilisation du sélecteur CSS pour l'élément spécifique
)
specific_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Remplir le champ "Régime"
regime_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-regime"))
)
regime_dropdown.click()  # Pour ouvrir la liste déroulante

# Sélectionner un élément spécifique dans la liste déroulante
specific_regime_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-value="TT"]'))  # Utilisation du sélecteur CSS pour l'élément spécifique
)
specific_regime_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Modifier la stratégie d'attente et le délai
puissance_souscrite_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, ":rp:"))
)
puissance_souscrite_input.clear()  # Effacer toute valeur existante
puissance_souscrite_input.send_keys("2")  # Remplacer "VotreValeur" par la valeur que vous choisissez

# Remplir le champ "Unité de Puissance Souscrite"
unite_dropdown = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-unite_puissance_soucrite"))
)
unite_dropdown.click()  # Pour ouvrir la liste déroulante

# Sélectionner l'unité spécifique dans la liste déroulante
specific_unite_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-value="KVA"]'))  # Utilisation du sélecteur CSS pour l'unité spécifique
)
specific_unite_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Remplir le champ "Puissance Déjà Consommée"
puissance_consommee_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, ":rl:"))
)
puissance_consommee_input.clear()  # Effacer toute valeur existante
puissance_consommee_input.send_keys("2")  # Remplacer "VotreValeur" par la valeur que vous souhaitez 

# Remplir le champ "Unité de Puissance Consommée"
unite_consommee_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-unite_puissance_consommee"))
)
unite_consommee_dropdown.click()  # Pour ouvrir la liste déroulante

# Sélectionner l'unité spécifique dans la liste déroulante
specific_unite_consommee_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-value="KW"]'))  # Utilisation du sélecteur CSS pour l'unité spécifique
)
specific_unite_consommee_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Remplir le champ "Mode de Pose vers TGBT"
mode_pose_tgbt_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-mode_pose_tgbt"))
)
mode_pose_tgbt_dropdown.click()  # Pour ouvrir la liste déroulante

# Sélectionner le mode spécifique dans la liste déroulante
specific_mode_pose_tgbt_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-value="13"]'))  # Utilisation du sélecteur CSS pour le mode spécifique
)
specific_mode_pose_tgbt_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Remplir le champ "Distance entre la source et le TGBT"
distance_tgbt_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, ":rm:"))
)
distance_tgbt_input.clear()  # Effacer toute valeur existante
distance_tgbt_input.send_keys("4")

# Sélectionner "Oui" dans le champ "Souhaitez-vous forcer la protection"
forcing_protection_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-equipement_existant_tgt"))
)
forcing_protection_dropdown.click()  # Pour ouvrir la liste déroulante

# Sélectionner "Oui" dans la liste déroulante
specific_forcing_protection_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//li[text()="Oui"]'))  # Utilisation du sélecteur XPath pour l'élément spécifique
)
specific_forcing_protection_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Sélectionner le constructeur dans le champ "Constructeur"
constructeur_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-Constructeur"))
)
constructeur_dropdown.click()  # Pour ouvrir la liste déroulante

# Sélectionner un élément spécifique dans la liste déroulante
specific_constructeur_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//li[text()="LEGRAND"]'))  # Remplacer "Legrand" par le constructeur spécifique que vous souhaitez choisir
)
specific_constructeur_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Sélectionner le type d'équipement dans le champ "Type d'équipement"
type_equipement_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-type_equipement"))
)
type_equipement_dropdown.click()  # Pour ouvrir la liste déroulante


# Choisir "Disj. Boitier moulé" dans la liste déroulante
choix_boitier_moule = driver.find_element(By.CSS_SELECTOR, 'li[data-value="Disj. Boitier moulé"]')
choix_boitier_moule.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Ouvrir la liste déroulante du nom de l'équipement
nom_equipement_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-nom_equipement_tgbt"))
)
nom_equipement_dropdown.click()

# Sélectionner "NS2000H 2000A 4P4D" dans la liste déroulante du nom de l'équipement
specific_nom_equipement_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//li[text()="DPX3 630A 4P4D"]'))  # Utiliser XPath pour sélectionner l'option "NS2000H 2000A 4P4D"
)
specific_nom_equipement_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Remplir le champ "Valeur de IK1"
ik1_valeur_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, ":rn:"))
)
ik1_valeur_input.clear()  # Effacer toute valeur existante
ik1_valeur_input.send_keys("2")  # Remplacer "02" par la valeur que vous souhaitez saisir

# Remplir le champ "Valeur de LK3"
lk3_valeur_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, ":ro:"))
)
lk3_valeur_input.clear()  # Efface toute valeur existante
lk3_valeur_input.send_keys("2")  # Remplacez "VotreValeurLK3" par la valeur que vous souhaitez saisir


# Ouvrir la liste déroulante
td_irve_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "mui-component-select-td_irve"))
)
td_irve_dropdown.click()

# Sélectionner "Oui" dans la liste déroulante
specific_td_irve_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-value="true"]'))  # Utiliser le sélecteur CSS pour sélectionner "Oui" basé sur l'attribut "data-value"
)
specific_td_irve_element.click()

# Attendre un bref délai pour permettre à l'élément d'être sélectionné
time.sleep(1)

# Cliquer sur le bouton "Suivant"
suivant_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.MuiButton-root[type="submit"]'))  # Utilisation du sélecteur CSS pour le bouton "Suivant"
)
suivant_button.click()

# Attendre un bref délai pour permettre à la nouvelle page de se charger
time.sleep(1)


#etape 3

element = driver.find_element(By.ID, ':rq:')
element.clear()  # Effacer la valeur existante
element.send_keys('TD_test')  # Remplacer la valeur par 'Nom_du_TD'

## Trouver l'élément par son ID et mettre à jour sa valeur
consommation_input = driver.find_element(By.ID, ':rr:')
consommation_input.clear()  # Effacer la valeur existante
consommation_input.send_keys("150")  # Remplacer la valeur par la consommation choisie

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-TD_IRVE_existant'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "Oui" dans la liste déroulante
oui_element = driver.find_element(By.XPATH, "//li[@data-value='true']")
oui_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Constructeur'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "SCHNEIDER" dans la liste déroulante
schneider_element = driver.find_element(By.XPATH, "//li[@data-value='SCHNEIDER']")
schneider_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Type_equipement_amont'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "Disj. Boitier moulé" dans la liste déroulante
disj_element = driver.find_element(By.XPATH, "//li[@data-value='Disj. Boitier moulé']")
disj_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Nom_equipement'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "NS800L 800A 4P4D" dans la liste déroulante
ns800_element = driver.find_element(By.XPATH, "//li[@data-value='NS800L 800A 4P4D']")
ns800_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Mode_pose'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "Souterrain" dans la liste déroulante
souterrain_element = driver.find_element(By.XPATH, "//li[@data-value='61']")
souterrain_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Trouver l'élément par son ID et mettre à jour sa valeur
distance_element = driver.find_element(By.ID, ':rs:')
distance_element.clear()  # Effacer la valeur existante
distance_element.send_keys("150")  # Remplacer la valeur par la distance choisie

## Trouver l'élément interrupteur par son nom
interrupteur_element = driver.find_element(By.NAME, 'interrupteur')

# Cocher l'interrupteur s'il n'est pas déjà coché
if not interrupteur_element.is_selected():
    interrupteur_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Constructeur_aval'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "SCHNEIDER" dans la liste déroulante
schneider_element = driver.find_element(By.XPATH, "//li[@data-value='SCHNEIDER']")
schneider_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Nom_equipement_aval'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "INV320 4P" dans la liste déroulante
inv320_element = driver.find_element(By.XPATH, "//li[@data-value='INV320 4P']")
inv320_element.click()

# Trouver l'élément par son ID et mettre à jour sa valeur
coef_element = driver.find_element(By.ID, ':rt:')
coef_element.clear()  # Effacer la valeur existante
coef_element.send_keys("")  # Remplacer la valeur par le coefficient souhaité

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Type_de_cable'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "AL" dans la liste déroulante
al_element = driver.find_element(By.XPATH, "//li[@data-value='AL']")
al_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)


# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Un_ou_Double'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "Double" dans la liste déroulante
double_element = driver.find_element(By.XPATH, "//li[@data-value='Double']")
double_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Attendre que l'élément soit cliquable
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Etat_aval'))
)

# Cliquer pour ouvrir la liste déroulante
select_element.click()

# Attendre un court instant pour permettre à la liste déroulante de se déployer
time.sleep(2)

# Sélectionner l'élément "Oui" dans la liste déroulante
oui_element = driver.find_element(By.XPATH, "//li[@data-value='true']")
oui_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Trouver l'élément de la case à cocher par son nom
checkbox_element = driver.find_element(By.NAME, 'voyant_sous_tension')

# Cocher la case à cocher
if not checkbox_element.is_selected():
    checkbox_element.click()

# Attendre un court instant pour voir le résultat
time.sleep(3)

# Cibler l'élément du bouton en utilisant la tabulation
button = driver.find_element(By.XPATH, '//*[@type="button" and contains(text(), "Ajouter au tableau")]')

# Cliquer sur le bouton
button.click()

# Attendre un court instant pour voir le résultat
time.sleep(2)
# Attente explicite pour que l'élément soit présent dans le DOM
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@title="Toggle SortBy"]'))
)

# Effectuer une action avec l'élément
element.click()
# Attendre un court instant pour voir le résultat
time.sleep(2)


#etape 4
# Attendre que le bouton de sélection soit cliquable
select_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-nom_amont'))
)

# Cliquer sur le bouton de sélection pour ouvrir la liste déroulante
select_button.click()

# Attendre que l'option "Tgb" soit visible et cliquable
tgb_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-value="TGBT"]'))
)

# Cliquer sur l'option "Tgb" dans la liste déroulante
tgb_option.click()

# Cibler le formulaire "nom de la borne" par son ID et en saisir une nouvelle valeur
nom_borne_input = driver.find_element(By.ID, ':r10:')
nom_borne_input.clear()  # Efface la valeur existante
nom_borne_input.send_keys("Nouvelle valeur")  # Remplace "Nouvelle valeur" par la valeur que vous souhaitez saisir

# Attendre un court instant pour voir le résultat
time.sleep(2)

# Attendre que le bouton de sélection soit cliquable
select_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Type_Borne'))
)

# Cliquer sur le bouton de sélection pour ouvrir la liste déroulante
select_button.click()

# Attendre que l'option "Double" soit visible et cliquable
double_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-value="Double"]'))
)

# Cliquer sur l'option "Double" dans la liste déroulante
double_option.click()

# Attendre que le bouton de sélection soit cliquable
select_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Puissance'))
)

# Cliquer sur le bouton de sélection pour ouvrir la liste déroulante
select_button.click()

# Attendre que l'option "7.4" soit visible et cliquable
option_7_4 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-value="7.4"]'))
)

# Cliquer sur l'option "7.4" dans la liste déroulante
option_7_4.click()

# Attendre que le bouton de sélection soit cliquable
select_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Mode_pose'))
)

# Cliquer sur le bouton de sélection pour ouvrir la liste déroulante
select_button.click()

# Attendre que l'option "Souterrain" soit visible et cliquable
option_souterrain = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-value="61"]'))
)

# Cliquer sur l'option "Souterrain" dans la liste déroulante
option_souterrain.click()

# Attendre que les formulaires et les listes déroulantes soient cliquables
distance_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, ':r11:'))
)
courant_borne_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Courant_de_la_borne'))
)

# Saisir une nouvelle valeur dans le formulaire "distance"
distance_input.clear()  # Efface la valeur existante
distance_input.send_keys("10")  # Remplace "10" par la valeur de distance que vous souhaitez saisir

# Cliquer sur le formulaire "courant de la borne" pour ouvrir la liste déroulante
courant_borne_select.click()

# Attendre que l'option "monophase" soit visible et cliquable
option_monophase = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-value="monophase"]'))
)

# Cliquer sur l'option "monophase" dans la liste déroulante
option_monophase.click()


# Ouvrir la page web
driver.get("https://www.example.com")  # Remplacer par l'URL de votre page web

# Attendre que les éléments soient cliquables
protection_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'mui-component-select-Protection_integré'))
)

# Cliquer sur le formulaire "protection" pour ouvrir la liste déroulante
protection_select.click()

# Attendre que l'option "Oui" soit visible et cliquable
option_oui = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-value="true"]'))
)

# Cliquer sur l'option "Oui" dans la liste déroulante
option_oui.click()

# Saisir une valeur dans le formulaire "coefficient de fusionnement"
coefficient_fusionnement_input = driver.find_element(By.ID, ':r12:')
coefficient_fusionnement_input.clear()  # Effacer la valeur existante
coefficient_fusionnement_input.send_keys("0.5")  # Remplace "0.5" par la valeur souhaitée