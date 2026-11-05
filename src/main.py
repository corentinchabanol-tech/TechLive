import argparse
import os
import json
from typing import List

from src.models import Segment
from ollama import chat

response = chat(
    model='qwen:4b',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
print(response.message.content)

DATA_DIR = '../data'
ENTRETIEN_DIR = os.path.join(DATA_DIR, 'entretiens')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("transcript_id", help="Un identifiant de transcript, entre 1 et 5", type=int)
  args = parser.parse_args()

  transcript_path = os.path.join(ENTRETIEN_DIR, f"E0{args.transcript_id}.json")

  with open(transcript_path, 'r', encoding='utf-8') as f:
    transcript: List[Segment] = json.load(f)

  report = Report(
    entretien_id: str
      statut_execution: Literal['ok', 'degrade', 'erreur']
      synthese: str # Généré par LLM -> envoi transcript et on dump
      besoins: List[Besoin] # Génération structuré depuis la liste des segments
      controles: List[Controle] # Est ce que R01-05 Généré par LLM Envoi des 5 règles + transcript et générations structurés sur schéma avec les 5 règles
      recommandations: List[Recommendation] # Codes produits suggérés (+ un raisonnement ?) Généré par llm Envoie transcript avec segid + Ref produit 
      sources_documentaires: List[ReferenceDocumentaire] # Ref des md
      questions_a_poser: List[str] # Généré par LLM
      diagnostic: Any
  )