"""
Script to fetch synced lyrics from online sources and convert to JSON format
"""
import json
import re

try:
    from syncedlyrics import search
    SYNCEDLYRICS_AVAILABLE = True
except ImportError:
    SYNCEDLYRICS_AVAILABLE = False
    print("syncedlyrics not installed. Install it with: pip install syncedlyrics")

def lrc_to_json(lrc_text):
    lyrics_list = []
    
    pattern = r'\[(\d+):(\d+)\.?\d*\](.*)'
    
    for line in lrc_text.split('\n'):
        match = re.match(pattern, line)
        if match:
            minutes = int(match.group(1))
            seconds = int(match.group(2))
            lyrics_text = match.group(3).strip()
            
            if lyrics_text:
                time_str = f"{minutes}:{seconds:02d}"
                lyrics_list.append({
                    "time": time_str,
                    "lyrics": lyrics_text
                })
    
    return lyrics_list

def fetch_lyrics(song_name, artist_name):
    if not SYNCEDLYRICS_AVAILABLE:
        print("\nPlease install syncedlyrics first:")
        print("pip install syncedlyrics")
        return None
    
    print(f"Searching for synced lyrics: {song_name} by {artist_name}...")
    
    try:
        lrc = search(f"{song_name} {artist_name}")
        
        if lrc:
            print("✓ Synced lyrics found!")
            return lrc
        else:
            print("✗ No synced lyrics found online")
            return None
            
    except Exception as e:
        print(f"Error fetching lyrics: {e}")
        return None

def save_lyrics_json(lyrics_list, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(lyrics_list, f, ensure_ascii=False, indent=2)
    print(f"✓ Lyrics saved to: {filename}")

def main():
    import sys
    
    if len(sys.argv) >= 3:
        song_name = sys.argv[1]
        artist_name = sys.argv[2]
    else:
        print("=" * 60)
        print("Synced Lyrics Fetcher")
        print("=" * 60)
        song_name = input("Enter song name: ").strip()
        artist_name = input("Enter artist name: ").strip()
        
        if not song_name or not artist_name:
            print("Error: Song name and artist name are required!")
            return
    
    print("\n" + "=" * 60)
    print(f"Fetching lyrics for: {song_name} by {artist_name}")
    print("=" * 60)
    
    lrc_text = fetch_lyrics(song_name, artist_name)
    
    if lrc_text:
        lyrics_json = lrc_to_json(lrc_text)
        
        if lyrics_json:
            output_file = f"{song_name.lower().replace(' ', '_')}_lyrics.json"
            save_lyrics_json(lyrics_json, output_file)
            
            print("\n" + "=" * 60)
            print("Copy this JSON and paste in Django admin 'lyrics' field:")
            print("=" * 60)
            print(json.dumps(lyrics_json, ensure_ascii=False))
            print("=" * 60)
            
            print(f"\nPreview (first 5 lines):")
            for i, lyric in enumerate(lyrics_json[:5]):
                print(f"  [{lyric['time']}] {lyric['lyrics']}")
            
            print(f"\nTotal lines: {len(lyrics_json)}")
        else:
            print("Could not parse lyrics")
    else:
        print("\nTip: You can also manually create lyrics using this format:")
        print('[{"time": "0:15", "lyrics": "First line"}, {"time": "0:30", "lyrics": "Second line"}]')

if __name__ == "__main__":
    main()
