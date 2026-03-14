# 🎵 SoundFlow - Modern Music Player

A sleek, modern web-based music player built with Django, featuring a Spotify-inspired dark UI with playlist management and seamless playback.

![SoundFlow](media/Capture0.png)

## ✨ Features

- **Modern Dark UI**: Clean, professional interface inspired by Spotify with neon green accents
- **Dynamic Playlist**: Click any song in the playlist to play it instantly
- **Seamless Playback**: Auto-plays next song when current track ends
- **Interactive Controls**: 
  - Play/Pause functionality
  - Previous/Next track navigation
  - Seekable progress bar
  - Volume control
- **Real-time Updates**: Album art, song title, and artist update dynamically
- **Responsive Design**: Optimized layout that fits perfectly on screen without scrolling
- **Active Track Highlighting**: Currently playing song is highlighted in the playlist

## 🛠️ Tech Stack

### Backend
- **Django 6.0** - Python web framework
- **SQLite** - Database for storing song metadata
- **Python 3.14.1** - Programming language

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern features (flexbox, custom scrollbars)
- **JavaScript (jQuery)** - Interactive functionality
- **Font Awesome 6.0** - Icons
- **MediaElement.js** - Audio player library

### Additional Tools
- **syncedlyrics** - For fetching synced lyrics from online sources
- **indic-transliteration** - For transliterating Hindi lyrics to Roman script

## 📁 Project Structure

```
musicPlayer-django/
├── App/
│   ├── migrations/
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   ├── templates/
│   │   ├── index.html
│   │   └── main.html
│   ├── models.py          # Song model
│   ├── views.py           # View logic
│   └── urls.py            # URL routing
├── MusicPlayer/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py
├── media/                 # Uploaded songs and images
├── static/                # Collected static files
├── db.sqlite3             # Database
├── manage.py              # Django management script
├── fetch_synced_lyrics.py # Script to fetch synced lyrics
├── transliterate_lyrics.py # Script to transliterate lyrics
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.14+ installed
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd musicPlayer-django
   ```

2. **Install dependencies**
   ```bash
   pip install django
   pip install syncedlyrics
   pip install indic-transliteration
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Music Player: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## 📝 Adding Songs

### Method 1: Django Admin Panel (Recommended)

1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Click on "Songs" → "Add Song"
4. Fill in the details:
   - **Title**: Song name
   - **Artist**: Artist name
   - **Image**: Album cover (upload image file)
   - **Audio file**: Upload MP3 file OR provide external URL
   - **Duration**: Song duration (e.g., "3:45")
   - **Lyrics**: Optional - JSON format with timestamps
5. Click "Save"

### Method 2: Using Python Script

```python
from App.models import Song

song = Song.objects.create(
    title="Song Title",
    artist="Artist Name",
    image="path/to/image.jpg",
    audio_file="path/to/song.mp3",
    duration="3:45"
)
song.save()
```

## 🎤 Adding Synced Lyrics

### Fetch Lyrics Automatically

1. **Run the lyrics fetcher script**
   ```bash
   python fetch_synced_lyrics.py "Song Name" "Artist Name"
   ```

2. **For Hindi songs, transliterate to Roman script**
   ```bash
   python transliterate_lyrics.py song_lyrics.json
   ```

3. **Copy the JSON output and paste it in Django admin**
   - Go to the song in admin panel
   - Paste JSON in the "Lyrics" field
   - Save

### Lyrics Format
```json
[
  {"time": "0:15", "lyrics": "First line"},
  {"time": "0:30", "lyrics": "Second line"},
  {"time": "0:45", "lyrics": "Third line"}
]
```

## 🎨 UI Features

- **Dark Theme**: Professional dark background (#0d0d0d)
- **Neon Green Accents**: Spotify-inspired green (#1ed760)
- **Smooth Animations**: Hover effects and transitions
- **Custom Scrollbar**: Styled scrollbar for playlist
- **Responsive Layout**: Fits perfectly on screen without scrolling
- **Active State**: Visual feedback for currently playing song

## 🔧 Configuration

### Database Settings
Located in `MusicPlayer/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### Static Files
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

## 📊 Database Schema

### Song Model
```python
class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=20)
```

## 🎯 Key Functionalities

### Player Controls
- **Play/Pause**: Toggle playback
- **Previous/Next**: Navigate through playlist
- **Seek**: Click on progress bar to jump to any position
- **Volume**: Adjust audio volume

### Playlist Management
- **Click to Play**: Click any song in playlist to play it
- **Auto-advance**: Automatically plays next song
- **Visual Feedback**: Active song is highlighted
- **Scrollable**: Smooth scrolling for large playlists

### Dynamic Updates
- Album art changes with each song
- Song title and artist update in real-time
- Progress bar shows current playback position
- Time display shows current time and total duration

## 🐛 Troubleshooting

### CSS not loading?
```bash
python manage.py collectstatic --noinput
# Then hard refresh browser: Ctrl + Shift + R
```

### Songs not playing?
- Check if audio files are in the `media/` folder
- Verify file paths in Django admin
- Check browser console for errors

### Lyrics not syncing?
- Ensure lyrics are in correct JSON format
- Check that timestamps match song duration
- Verify lyrics field is not empty in database

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created with ❤️ using Django and modern web technologies.

## 🙏 Acknowledgments

- UI inspired by Spotify
- Icons from Font Awesome
- Audio player powered by MediaElement.js
- Lyrics fetching via syncedlyrics library
