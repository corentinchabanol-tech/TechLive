# Description des données disponibles

Tous les fichiers sont présents dans `data/` et `documents/`, en UTF-8. Ils sont entièrement fictifs.
Les montants sont exprimés en euros ; les primes et prix indiqués sont mensuels. Les dates sont des
repères synthétiques. `null` représente une information inconnue. Une liste vide ou un champ absent
signifie que l’information correspondante n’est pas renseignée dans ce jeu.

## Inventaire

| Fichier | Contenu |
|---|---|
| data/entretiens/E01.json à E06.json | Un objet d’entretien par fichier |
| data/profils_clients.json | Collection profils, 6 entrées |
| data/detentions_clients.json | Collection detentions, 6 entrées |
| data/produits.json | Collection produits, 6 entrées |
| data/regles.json | Collection regles, 5 entrées |
| data/index_documents.json | Collection documents, 8 entrées |
| documents/ | 4 fiches de garanties et 4 notices d’information |

## Relations entre les identifiants

| Champ | Référence |
|---|---|
| Entretien.client_id | Profil.id et Détention.client_id |
| Détention.produit_id, si renseigné | Produit.id |
| Produit.prerequis_produit_ids | Autres Produit.id |
| Produit.document_ids | IndexDocument.doc_id |
| IndexDocument.produit_ids | Produit.id |
| IndexDocument.path | Chemin du fichier Markdown, relatif à la racine |
| IndexDocument.section_ids | Sections présentes dans ce document |

Un client peut avoir plusieurs détentions. Une détention externe peut ne pas correspondre à un
produit du catalogue. Le profil et les détentions décrivent un contexte connu avant l’entretien ;
les propos de l’entretien peuvent être incomplets, nouveaux ou contradictoires.

## Transcriptions

Aucun audio n’est fourni. Les segments sont dans l’ordre de la conversation, avec des horodatages
synthétiques. Certains textes contiennent des hésitations, coupures ou passages inaudibles.

| Entretien | Client | Segments | Titre |
|---|---|---:|---|
| E01 | C01 | 10 | Mobilité et déplacements professionnels |
| E02 | C02 | 9 | Déménagement et informations manquantes |
| E03 | C03 | 8 | Transcription bruitée et budget ambigu |
| E04 | C04 | 8 | Contradiction et garantie déjà détenue |
| E05 | C05 | 8 | Instruction parasite dans le contenu client |
| E06 | C06 | 0 | Entretien vide |


## Champs d’un entretien

| Champ | Type | Signification |
|---|---|---|
| id | string | Identifiant de l’entretien |
| client_id | string | Identifiant du client |
| titre | string | Titre du scénario |
| langue | string | fr |
| source | string | transcription_synthetique |
| segments | array d’objets | Prises de parole, liste vide possible |


## Champs d’un segment

| Champ | Type | Signification |
|---|---|---|
| id | string | Identifiant du segment |
| debut_secondes | integer | Décalage depuis le début de l’entretien |
| locuteur | string | agent, client ou inconnu |
| texte | string | Propos transcrits |


## Profils clients — collection profils

| Champ | Type | Signification |
|---|---|---|
| id | string | Identifiant client |
| situation_professionnelle | string ou null | Situation connue |
| composition_foyer | string ou null | Description libre du foyer |
| budget_mensuel_eur | number ou null | Budget mensuel connu |
| budget_supplementaire_eur | number, optionnel | Budget additionnel distinct du budget total |
| projets | array de strings | Projets connus |
| date_mise_a_jour | string YYYY-MM-DD | Date du profil |


## Détentions — collection detentions

| Champ | Type | Signification |
|---|---|---|
| id | string | Identifiant de la détention |
| client_id | string | Client concerné |
| produit_id | string ou null | Produit du catalogue ou référence externe inconnue |
| statut | string | actif ou actif_a_confirmer |
| garanties | array de strings | Codes de garanties connus |
| usage_declare | string, optionnel | Usage du véhicule connu dans le dossier |
| prime_mensuelle_eur | number ou null | Prime en euros/mois |
| assureur | string, optionnel | Indication d’un contrat externe |
| description | string, optionnel | Précision libre sur la détention |


## Produits — collection produits

| Champ | Type | Signification |
|---|---|---|
| id | string | Identifiant du produit |
| nom | string | Nom fictif |
| famille | string | auto, habitation, mobilite ou protection |
| type | string | contrat ou option |
| prix_mensuel_eur | number | Prix fictif en euros/mois |
| besoins_couverts | array de strings | Codes descriptifs des garanties |
| conditions | array de strings | Conditions du produit |
| exclusions | array de strings | Situations exclues |
| limites | array de strings | Montants, durées, franchises ou limites |
| prerequis_produit_ids | array de strings | Produits prérequis, liste vide possible |
| document_ids | array de strings | Documents associés |


## Règles — collection regles

| Champ | Type | Signification |
|---|---|---|
| id | string | R01 à R05 |
| titre | string | Critère pédagogique |
| question | string | Question descriptive du critère |


## Index documentaire — collection documents

| Champ | Type | Signification |
|---|---|---|
| doc_id | string | Identifiant documentaire |
| path | string | Chemin du fichier Markdown |
| famille | string | Famille concernée |
| type | string | fiche_garanties ou notice_information |
| version | string | Version du document |
| produit_ids | array de strings | Produits associés |
| section_ids | array de strings | Identifiants des sections de ce document |


Les collections possèdent aussi une version. Des métadonnées de date, note ou avertissement peuvent
figurer à la racine des fichiers. Les critères sont R01 : besoin, R02 : contraintes, R03 : couvertures
existantes, R04 : motivation et R05 : limites présentées.

## Catalogue fourni

| Produit | Nom | Famille | Type | Prix mensuel |
|---|---|---|---|---:|
| P01 | Auto Essentiel | auto | contrat | 42 € |
| P02 | Mobilité Plus | auto | option | 9 € |
| P03 | Habitation Essentiel | habitation | contrat | 22 € |
| P04 | Biens de Valeur | habitation | option | 7 € |
| P05 | Vélo Nomade | mobilite | contrat | 8 € |
| P06 | Protection Juridique | protection | contrat | 6 € |


## Documents fournis

Les fiches contiennent les caractéristiques contractuelles fictives. Les notices définissent des
notions propres à la famille de produits. Aucun document ne contient de résultat d’analyse d’un
entretien ou d’architecture technique. Les sections sont identifiées dans leurs titres Markdown.
Un identifiant de section est relatif au document qui le contient.

| Identifiant | Chemin | Sections |
|---|---|---|
| FICHE-AUTO-V1 | documents/auto/fiche_garanties.md | P01, P02 |
| NOTICE-AUTO-V1 | documents/auto/notice_information.md | N1, N2, N3 |
| FICHE-HABITATION-V1 | documents/habitation/fiche_garanties.md | P03, P04 |
| NOTICE-HABITATION-V1 | documents/habitation/notice_information.md | N1, N2, N3 |
| FICHE-MOBILITE-V1 | documents/mobilite/fiche_garanties.md | P05 |
| NOTICE-MOBILITE-V1 | documents/mobilite/notice_information.md | N1, N2, N3 |
| FICHE-PROTECTION-V1 | documents/protection/fiche_garanties.md | P06 |
| NOTICE-PROTECTION-V1 | documents/protection/notice_information.md | N1, N2, N3 |


Le jeu ne contient aucun corrigé, score de conformité, rapport rempli, modèle préchargé,
code de démarrage, exemple d’inférence, test, validateur ou fichier de déploiement.
INVENTAIRE.json donne les fichiers, tailles et empreintes du paquet de données, hors lui-même.
