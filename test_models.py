#!/usr/bin/env python
"""Script para listar modelos disponibles en Google Gemini API gratuita."""

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    print("❌ Error: GOOGLE_API_KEY no configurada en .env")
    exit(1)

print(f"✅ API Key encontrada: {api_key[:10]}...")
genai.configure(api_key=api_key)

print("\n📋 Listando modelos disponibles:\n")
for model in genai.list_models():
    print(f"  - {model.name}")
    if "generateContent" in model.supported_generation_methods:
        print(f"    ✅ Soporta generateContent")
