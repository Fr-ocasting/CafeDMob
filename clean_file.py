#!/usr/bin/env python
import os

# Read the file
filepath = 'Presentation_Limites_LLM.qmd'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacements for smart quotes and special characters
replacements = {
    '\u2018': "'",  # Left single quote
    '\u2019': "'",  # Right single quote  
    '\u201c': '"',  # Left double quote
    '\u201d': '"',  # Right double quote
    '\u2013': '-',  # En dash
    '\u2014': '--', # Em dash
    '\u2026': '...', # Ellipsis
}

# Apply replacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Successfully cleaned {filepath}')
