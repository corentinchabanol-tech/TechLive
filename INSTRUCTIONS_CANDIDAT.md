# Énoncé — Assistant IA de conseil en assurance

## Internet et assistants de code

**L’utilisation de GitHub Copilot ou de tout autre assistant de code ou assistant IA pour réaliser
le test est interdite**, qu’il soit intégré à l’IDE, accessible sur le Web ou exécuté localement.
Cela inclut les suggestions et complétions génératives, la génération ou modification de code,
l’aide à la conception, l’explication du code et le débogage par un assistant.

**Internet reste autorisé** : recherches Web classiques, consultation de sites, forums et dépôts
publics, lecture de toute documentation et téléchargement d’outils, de bibliothèques ou de modèles.
Les exemples de code déjà publiés dans ces ressources peuvent être consultés et utilisés.
Il est interdit de solliciter un assistant conversationnel ou une fonction de génération pour
produire la réalisation du test, même si le service est gratuit.

Cette interdiction concerne l’assistance au développement. Le modèle local utilisé par l’application
pour analyser les données d’assurance fait partie du sujet et reste obligatoire ; il ne doit pas
être détourné en assistant de code. Les fonctions non génératives ordinaires de l’IDE restent autorisées.

## 1. Contexte et objectif

Vous devez réaliser un prototype d’assistant qui analyse la transcription d’un entretien entre un
agent d’assurance et un client. Le prototype dispose également du profil du client, de ses contrats
et garanties déjà détenus, d’un catalogue de produits et de documents métier.

L’application doit produire un rapport comprenant une synthèse, les besoins identifiés, l’examen
des cinq critères de conseil fournis, des suggestions de produits ou garanties et les informations
restant à confirmer. Le format attendu est défini dans FORMAT_RAPPORT.md.

**Durée : 90 minutes de travail effectif.** Nous évaluons la réalisation technique complète et la
reproductibilité. L’exactitude métier des analyses, la qualité rédactionnelle du modèle et la justesse
des recommandations ne sont pas notées. Les règles sont pédagogiques et ne constituent pas un
référentiel juridique.

## 2. Entrées disponibles

| Ensemble | Volume |
|---|---:|
| Transcriptions d’entretiens | 6 entretiens, 43 segments |
| Profils clients | 6 |
| Contrats et garanties détenus | 6 enregistrements |
| Catalogue | 6 produits ou options |
| Critères de conseil | 5 |
| Documents produits | 8 documents, pour 4 familles |
| Index documentaire | 8 entrées |

Les fichiers, champs et relations sont décrits dans DESCRIPTION_DONNEES.md. Ils sont fournis en
UTF-8 et sont entièrement fictifs. Aucun travail de speech-to-text ou de recherche juridique n’est
demandé. Aucune réponse attendue par entretien n’est fournie.

## 3. Comportement fonctionnel attendu

- L’entretien doit pouvoir être sélectionné par son identifiant.
- L’analyse doit exploiter la transcription, le profil correspondant, les détentions connues,
  le catalogue, les critères et le texte des documents métier.
- Au moins une véritable génération du modèle doit contribuer au résultat de l’analyse.
- Le résultat doit être enregistré dans un fichier JSON conforme au format demandé.
- Les références aux entretiens, segments, produits, règles et sections doivent correspondre aux
  identifiants des données fournies.
- Une réponse inexploitable du modèle doit conduire à un comportement explicite et documenté.
- Le même programme doit accepter un autre entretien du jeu sans modification de son code.

**E01 est l’entretien obligatoire pour la démonstration de bout en bout.** Les autres entretiens
permettent de varier les entrées ; aucune analyse exhaustive ni mesure de précision n’est requise.
Il n’est pas nécessaire de développer une interface graphique. L’interface d’exécution et
l’organisation du programme sont à votre choix et doivent être documentées.

## 4. Contraintes de modèle et de coût

Le modèle utilisé dans la démonstration doit s’exécuter sur votre machine, avec des poids disponibles
gratuitement sous une licence libre ou permissive identifiée. L’application ne doit utiliser aucune
inférence distante, même gratuite, ni mécanisme de repli vers un fournisseur cloud.

Les composants applicatifs, d’inférence et de déploiement doivent être open source et utilisables
gratuitement. Aucun GPU, abonnement LLM ou compte cloud payant ne doit être nécessaire. Le modèle,
sa révision, sa licence et les composants utilisés doivent être indiqués dans le README de remise.

GitHub pour la remise et GitHub Actions pour la CI/CD sont les services hébergés autorisés, dans
les quotas gratuits disponibles. Les téléchargements de fichiers publics et la consultation de
documentation sur Internet sont autorisés. Ces plateformes ne sont pas présentées comme des logiciels
intégralement open source. Le matériel et l’électricité ne sont pas des frais d’API demandés au candidat.

## 5. Déploiement local attendu

Après clonage du dépôt remis et avec les prérequis système documentés déjà installés, une seule
commande doit permettre de rendre la solution utilisable localement avec le modèle réel.
Vous choisissez cette commande et l’indiquez clairement dans votre README.

Le lancement doit prendre en charge les dépendances applicatives, les ressources du modèle manquantes,
le démarrage des composants et la vérification effective du fonctionnement. Il ne doit pas nécessiter
de préparation manuelle applicative, d’édition de configuration ou de démarrage séparé du modèle.

Le démarrage doit afficher ou indiquer comment utiliser l’application, enregistrer le rapport de
démonstration et signaler clairement un échec. Une commande d’arrêt doit également être documentée.
Les ressources téléchargées doivent être réutilisables lors d’une relance. Une fois les ressources
en cache, l’inférence et le redémarrage doivent fonctionner sans accès réseau externe.

Vous devez indiquer l’OS et les prérequis système pris en charge. Une seule combinaison documentée
suffit. Aucun déploiement cloud ou hébergement public permanent n’est requis.

## 6. CI/CD attendue avec GitHub Actions

Le dépôt remis doit contenir une automatisation active sur pull request et sur push vers `main`.
Elle doit vérifier les tests, produire un livrable déployable et démontrer une exécution de ce livrable
avec validation du résultat. Un échec des vérifications doit rendre l’exécution CI en échec.

Les tests et l’exécution CI peuvent substituer la réponse du modèle afin de ne pas imposer le
téléchargement de poids ni l’inférence réelle sur le runner. Cette substitution doit être clairement
signalée. La CI doit vérifier le mécanisme de déploiement fourni ; un livrable seulement construit
mais jamais exécuté ne suffit pas.

Sur `main`, le livrable exact testé, son identifiant, le commit associé et les traces utiles doivent
être récupérables depuis GitHub Actions. Documentez son utilisation locale. Les ressources temporaires
créées par la CI doivent être nettoyées, y compris après un échec.

La démonstration locale réelle reste obligatoire et est distincte des vérifications simulées de CI.

## 7. Vérifications minimales

| Vérification | Résultat attendu |
|---|---|
| Cas nominal automatisé | L’analyse d’E01 avec une réponse modèle substituée respecte le contrat de sortie |
| Cas d’échec automatisé | Une réponse modèle inexploitable produit le comportement d’erreur annoncé |
| Exécution CI | Le livrable est réellement exécuté et son résultat vérifié |
| Démonstration locale | La commande unique produit une analyse d’E01 avec le véritable modèle local |

Aucun code de test, réponse simulée, validateur ou exemple de rapport n’est fourni.
La pertinence sémantique des textes n’est pas évaluée ; le respect des contrats et la maîtrise
du comportement d’exécution le sont.

## 8. Remise

À T+90, arrêtez les modifications et transmettez :
- l’URL de votre dépôt GitHub, accessible à l’évaluateur ;
- le SHA du commit final ;
- le lien vers l’exécution GitHub Actions de ce commit.

Le dépôt doit contenir votre réalisation, ses tests, son automatisation, les données de référence
et un README précisant :
- les prérequis, les commandes de lancement, de test et d’arrêt ;
- les choix de réalisation, versions, modèle, licence et fonctionnement du cache ;
- les preuves d’un même appel réel : entrée transmise au modèle, sortie brute et rapport produit ;
- la récupération et l’utilisation du livrable CI ;
- les limites, éléments inachevés et les principales ressources documentaires consultées.

Ne commitez pas les poids du modèle, environnements virtuels, caches, secrets ou clés d’accès.
Un run lancé avant T+90 peut se terminer après, sans modification supplémentaire du code.
Une réalisation incomplète doit être remise en l’état avec ses limites documentées.

## 9. Évaluation

| Dimension | Points |
|---|---:|
| Exploitation des données et documents | 20 |
| Intégration effective du modèle local | 15 |
| Contrat de sortie et erreurs | 10 |
| CI GitHub Actions | 15 |
| Livrable déployable et reproductibilité | 10 |
| Déploiement local automatisé | 20 |
| Qualité de la remise GitHub | 10 |
| Exactitude métier et qualité rédactionnelle du modèle | 0 |

Les choix d’architecture, d’outils, de bibliothèques et de modèle sont à votre initiative. Aucun
framework particulier, mécanisme de recherche documentaire, schéma d’architecture ou procédure
d’implémentation n’est fourni ni imposé.
