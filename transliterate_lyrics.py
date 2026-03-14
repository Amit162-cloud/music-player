"""
Script to transliterate Hindi lyrics to Roman script
"""
import json

try:
    from indic_transliteration import sanscript
    from indic_transliteration.sanscript import transliterate
    TRANSLITERATION_AVAILABLE = True
except ImportError:
    TRANSLITERATION_AVAILABLE = False
    print("indic-transliteration not installed.")
    print("Install it with: pip install indic-transliteration")

def transliterate_lyrics_file(input_file, output_file):
    
    if not TRANSLITERATION_AVAILABLE:
        print("\nPlease install the required library:")
        print("pip install indic-transliteration")
        return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lyrics_data = json.load(f)
        
        transliterated_lyrics = []
        for item in lyrics_data:
            hindi_text = item['lyrics']
            roman_text = transliterate(hindi_text, sanscript.DEVANAGARI, sanscript.ITRANS)
            
            transliterated_lyrics.append({
                "time": item['time'],
                "lyrics": roman_text
            })
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(transliterated_lyrics, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Transliterated lyrics saved to: {output_file}")
        
        print("\n" + "=" * 60)
        print("Copy this JSON and paste in Django admin 'lyrics' field:")
        print("=" * 60)
        print(json.dumps(transliterated_lyrics, ensure_ascii=False))
        print("=" * 60)
        
        print(f"\nPreview (first 5 lines):")
        for i, lyric in enumerate(transliterated_lyrics[:5]):
            print(f"  [{lyric['time']}] {lyric['lyrics']}")
        
        print(f"\nTotal lines: {len(transliterated_lyrics)}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found!")
        print("First run: python fetch_synced_lyrics.py")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
        output_file = input_file.replace('.json', '_romanized.json')
    else:
        input_file = "qaafirana_lyrics.json"
        output_file = "qaafirana_lyrics_romanized.json"
    
    print("=" * 60)
    print("Hindi to Roman Transliteration")
    print("=" * 60)
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    print("=" * 60)
    
    transliterate_lyrics_file(input_file, output_file)
