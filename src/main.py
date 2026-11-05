import argparse
import os
import json
from typing import List

from src.models import Controle, Segment, Besoin
from pydantic import BaseModel
from ollama import chat
from src.utils import normalize_segment

### class pydantic for structured output generation
class BesoinArray(BaseModel):
  besoins: List[Besoin]

class ControleArray(BaseModel):
  controles: List[Controle]

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
REGLES_PATH = os.path.join(DATA_DIR, 'regles.json')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("transcript_id", help="Un identifiant de transcript, entre 1 et 5", type=int)
  args = parser.parse_args()

  entretien_id = f"E0{args.transcript_id}"
  transcript_path = os.path.join(ENTRETIEN_DIR, f"{entretien_id}.json")

  with open(transcript_path, 'r', encoding='utf-8') as f:
    transcript: List[Segment] = json.load(f)

  report = None
  stringify_transcript = '\n'.join(normalize_segment(seg) for seg in transcript)

  try:
    # 1ere étape - synthèse
    synthese = call(
      f"""Fais moi un synthèses brève en quelque phrases de cet échange entre un collaborateur AXA et un client:
      {stringify_transcript}
      """
    )

    # 2 - les besoins clients

    besoins: BesoinArray = call_strucured_output(
      f"""
      Extrais les besoins exprimés par l'interlocuteur "client" en citant l'id du segment qui l'exprime:
      {stringify_transcript}
""",
      BesoinArray
    )

    # 3 - analyse des règles

    rules_prompt: str = # TODO
    controles: ControleArray = call_strucured_output(
      f"""
Pour chaqu'une des règles sous cités analyse son respect au vu du transcript
{rules_prompt}

{stringify_transcript}
""",
      ControleArray
    )

    report = Report(
        entretien_id = entretien_id,
        statut_execution = 'ok',
        synthese = synthese,
        besoins = besoins.besoins,
        controles = controles.controles
        recommandations: List[Recommendation] # Codes produits suggérés (+ un raisonnement ?) Généré par llm Envoie transcript avec segid + Ref produit 
        sources_documentaires: List[ReferenceDocumentaire] # Ref des md
        questions_a_poser: List[str] # Généré par LLM
        diagnostic: Any
      )
  except:
    report = failed_report