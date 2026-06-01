import sys
sys.path.append('backend')
from services.summarizer import generate_summary

text = "This is a dummy transcript with more than twenty words so that we can bypass the twenty word limit that was coded correctly in the first place into the file. The quick brown fox jumps over the lazy dog."

print(generate_summary(text))
