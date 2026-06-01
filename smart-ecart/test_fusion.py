import sys
sys.path.append('backend')
from services.ingredient_fusion import fuse_ingredients

audio_list = [{'name': 'egg', 'quantity': '3', 'source': 'whisper'}, {'name': 'milk', 'quantity': '1 cup of', 'source': 'whisper'}]
vision_list = []
ocr_list = []
res = fuse_ingredients(audio_list, vision_list, ocr_list)
print('FUSED:', res)
