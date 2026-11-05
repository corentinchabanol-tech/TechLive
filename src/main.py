import argparse
import os
import json
from typing import List

from src.models import Segment
from pydantic import BaseModel
from ollama import chat
from src.utils import normalize_segment

MODEL = 'qwen:4b'

def call_strucured_output(prompt: str, json_schema: BaseModel) -> BaseModel:
  response = chat(
      model=MODEL,
      messages=[{'role': 'user', 'content': prompt}],
      format=json_schema.model_json_schema()
  )
  return response.message.content

def call(prompt: str) -> str:
  response = chat(
        model=MODEL,
        messages=[{'role': 'user', 'content': prompt}],
    )
  return response.message.content

DATA_DIR = '../data'
ENTRETIEN_DIR = os.path.join(DATA_DIR, 'entretiens')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("transcript_id", help="Un identifiant de transcript, entre 1 et 5", type=int)
  args = parser.parse_args()

  entretien_id = f"E0{args.transcript_id}"
  transcript_path = os.path.join(ENTRETIEN_DIR, f"{entretien_id}.json")

  with open(transcript_path, 'r', encoding='utf-8') as f:
    transcript: List[Segment] = json.load(f)

  report = None

  try:
    # 1ere étape - synthèse
    synthese = call(
      f"""Fais moi un synthèses brève en quelque phrases de cet échange entre un collaborateur AXA et un client:
      {'\n'.join(normalize_segment(seg) for seg in transcript)}
      """
    )

    report = Report(
        entretien_id = entretien_id,
        statut_execution = 'ok',
        synthese = synthese,
        besoins: List[Besoin] # Génération structuré depuis la liste des segments
        controles: List[Controle] # Est ce que R01-05 Généré par LLM Envoi des 5 règles + transcript et générations structurés sur schéma avec les 5 règles
        recommandations: List[Recommendation] # Codes produits suggérés (+ un raisonnement ?) Généré par llm Envoie transcript avec segid + Ref produit 
        sources_documentaires: List[ReferenceDocumentaire] # Ref des md
        questions_a_poser: List[str] # Généré par LLM
        diagnostic: Any
      )
  except:
    report = failed_report