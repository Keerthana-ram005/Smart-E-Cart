import sys
sys.path.append('backend')
from services.whisper_service import extract_ingredients_from_text

test_text = 'Okay so today we are going to make a cake. We need to add 2 cups of sugar, 1 cup of milk, and 3 eggs. Then mix it with some flour and half a teaspoon of salt.'
print(extract_ingredients_from_text(test_text))
