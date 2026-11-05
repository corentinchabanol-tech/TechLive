from dataclasses import dataclass
from typing import Any, List, Literal
from pydantic import BaseModel

@dataclass
class Segment:
  id: str
  debut_secondes: int
  locuteur: Literal['agent', 'client']
  texte: str

@dataclass
class Profil:
  id: str
  situation_professionnelle: str
  composition_foyer: str
  budget_mensuel_eur: int
  projets: List[str]
  date_mise_a_jour: str #AAAA-MM-DD

@dataclass
class Regle:
  id: str
  titre: str
  question: str

Famille = Literal['auto', 'habitation', 'mobilite', 'protection']

@dataclass
class Produit:
  id: str
  nom: str
  famille: Famille
  type: Literal['contrat', 'option']
  prix_mensuel_eur: int
  besoins_couverts: List[str]
  conditions: List[str]
  exclusions: List[str]
  limites: List[str]
  prerequis_produit_ids: List
  document_ids: List[str]

@dataclass
class Document:
  doc_id: str
  path: str
  famille: Famille
  type: Literal['fiche_garanties', 'notice_information']
  version: str
  produits_ids: List[str]
  section_ids: List[str]

@dataclass
class Detention:
  id: str
  client_id: str
  produit_id: str
  statut: Literal['actif', 'actif_a_confirmer']
  garanties: List[str]
  usage_declare: Literal['domicile-travail', 'privé'] | None
  prime_mensuelle_eur: int


##### REPORT CLASSES #####

@dataclass
class ReferenceDocumentaire:
  doc_id: str
  section_id: str

@dataclass
class Besoin:
  description: str
  segment_ids: List[str]

@dataclass
class Recommendation:
  produit_id: str
  motif: str # Pk on recommande ?
  a_confirmer: List[str]
  sources: List[ReferenceDocumentaire] # Ref documentaires md

@dataclass
class Controle:
  regle_id: str
  statut: Literal['observe', 'a_completer', 'non_verifiable', 'non_applicable']
  justification: str
  segment_ids: List[str]

@dataclass
class Diagnostic:
  mode: str
  modele: str
  appel_modele_effectue: bool
  duree_ms: int # ms
  avertissements: List[str]

@dataclass
class Report:
  entretien_id: str
  statut_execution: Literal['ok', 'degrade', 'erreur']
  synthese: str # Généré par LLM -> envoi transcript et on dump
  besoins: List[Besoin] # Génération structuré depuis la liste des segments
  controles: List[Controle] # Est ce que R01-05 Généré par LLM Envoi des 5 règles + transcript et générations structurés sur schéma avec les 5 règles
  recommandations: List[Recommendation] # Codes produits suggérés (+ un raisonnement ?) Généré par llm Envoie transcript avec segid + Ref produit 
  sources_documentaires: List[ReferenceDocumentaire] # Ref des md
  questions_a_poser: List[str] # Généré par LLM
  diagnostic: Diagnostic