# Résultat attendu — rapport JSON

Ce document définit uniquement le contrat du résultat à produire. Aucun exemple de rapport rempli,
statut attendu par entretien, recommandation attendue ou code de validation n’est fourni.
Des champs supplémentaires sont acceptés si les champs ci-dessous sont présents.

## Objet principal

| Champ | Type | Attendu |
|---|---|---|
| entretien_id | string | Identifiant de l’entretien analysé |
| statut_execution | string | ok, degrade ou erreur |
| synthese | string | Synthèse libre de l’échange |
| besoins | array d’objets | Besoins identifiés, éventuellement vide |
| controles | array de 5 objets | Une entrée pour chacune des règles R01 à R05 |
| recommandations | array d’objets | Produits ou garanties suggérés, éventuellement vide |
| sources_documentaires | array d’objets | Références aux documents exploités |
| questions_a_poser | array de strings | Informations restant à confirmer, éventuellement vide |
| diagnostic | objet | Informations techniques d’exécution |

`statut_execution` décrit l’état technique de l’analyse, pas un verdict de conformité juridique.
Une dégradation ou une erreur doit être explicitée dans les avertissements.

## Éléments des listes

| Élément | Champs requis |
|---|---|
| besoins[] | description: string ; segment_ids: array de strings |
| controles[] | regle_id: string ; statut: string ; justification: string ; segment_ids: array de strings |
| recommandations[] | produit_id: string ; motif: string ; a_confirmer: array de strings ; sources: array de références documentaires |
| Référence documentaire | doc_id: string ; section_id: string |

Les segments cités doivent exister dans l’entretien. Chaque règle figure exactement une fois.
Les produits et couples document/section cités doivent exister dans les données de référence.
Une recommandation présente doit avoir au moins une source documentaire. Les listes de références
de segments peuvent être vides quand aucun élément ne peut être cité.

Statuts des contrôles : `observe` (élément présent), `a_completer` (élément incomplet),
`non_verifiable` (information insuffisante), `non_applicable` (critère non applicable selon l’analyse).
La pertinence sémantique des statuts et recommandations n’est pas notée.

## Diagnostic

| Champ | Type | Attendu |
|---|---|---|
| mode | string | reel, simule ou sans_modele |
| modele | string | Identifiant du modèle utilisé, ou indication explicite de substitution/absence |
| appel_modele_effectue | boolean | Indique honnêtement si une inférence réelle a été tentée |
| duree_ms | number | Durée d’analyse en millisecondes, supérieure ou égale à zéro |
| avertissements | array de strings | Limites, dégradations ou erreurs rencontrées |

Le mode simulé ne doit pas être présenté comme une inférence réelle. La démonstration locale doit
comporter une génération réellement obtenue et utilisée. En cas de réponse modèle inexploitable,
un rapport dégradé ou une erreur applicative documentée est acceptable. Si l’application retourne
une erreur distincte plutôt qu’un rapport, son contrat doit être décrit dans votre README.
