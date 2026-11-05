from typing import List

from models import Segment
import pandas as pd

def normalize_segment(seg: Segment) -> str:
  return f"[id: {seg.id}] [{seg.debut_secondes}s] {seg.locuteur}: {seg.texte}"

def segments_to_text(df: pd.DataFrame) -> str:
  segments: List[Segment] = [Segment(**seg_dict) for seg_dict in list(df['segments'])]
  segments.sort(key = lambda seg: seg.debut_secondes)
  final_text: str = ""

  for seg in segments:
    final_text += f"- {normalize_segment(seg)}\n"

  return final_text