# Czech Keyboard Touch Typing Tutor 🎹⌨️

A comprehensive desktop application to learn touch typing on the Czech QWERTZ keyboard layout with proper 10-finger technique.

## Features ✨

### 🎯 Complete Touch Typing System
- **1200+ Progressive Exercises**: Structured learning path from beginner to expert
- **Czech QWERTZ Layout**: Native support for Czech keyboard layout with all diacritics (ě, š, č, ř, ž, ý, á, í, é, ú, ů)
- **Real Czech Words**: Over 200 authentic Czech words with proper diacritics in exercises
- **Czech Sentences**: 30+ real Czech sentences for natural typing practice
- **Visual Keyboard**: Interactive keyboard display with real-time highlighting
- **Finger Placement Guide**: Color-coded keys showing which finger should press each key
- **10-Finger Technique**: Proper finger placement training following touch typing standards

### 📊 Learning & Progress Tracking
- **Real-time Feedback**: Instant mistake detection and correction
- **Performance Metrics**: 
  - Words Per Minute (WPM)
  - Accuracy percentage
  - Mistake tracking per character
  - Time taken per exercise
- **Progress Reports**: Detailed statistics and improvement trends
- **Persistent Storage**: Automatic saving of all practice sessions
- **Difficulty Levels**: 8 progressive levels from basic to expert

### 🎨 User Interface
- **Modern GUI**: Built with Python Tkinter
- **Color-coded Fingers**: 
  - Pink for pinkies
  - Purple for ring fingers
  - Blue for middle fingers
  - Green for index fingers
  - Gold for thumbs
- **Live Exercise Display**: Clear text with color highlighting (green for correct, red for mistakes)
- **Comprehensive Feedback**: Detailed feedback after each exercise

## Exercise Structure 📚

### Level 1: Home Row (150 exercises)
Keys: a, s, d, f, j, k, l, ů
- Foundation of touch typing
- Finger positioning base
- Includes simple Czech words

### Level 2: Top Row (150 exercises)
Keys: q, w, e, r, t, z, u, i, o, p
- Extension from home row upward
- Building muscle memory

### Level 3: Bottom Row (150 exercises)
Keys: y, x, c, v, b, n, m
- Complete alphabet coverage

### Level 4: Czech Basic Words (200 exercises)
Real Czech words: ale, ano, být, den, dobrý, jak, který, můj, také, všech, atd.
- Over 90 common Czech words
- Natural language practice
- Includes words with diacritics

### Level 5: Czech Diacritics Focus (150 exercises)
Practice words specifically with: ě, š, č, ř, ž, ý, á, í, é, ú, ů
- Words like: být, může, již, řekl, přes, důvod, věc, atd.
- Intensive diacritic training
- Real Czech vocabulary

### Level 6: Intermediate Czech Words (150 exercises)
Words: člověk, český, děkuji, jméno, několik, případ, společnost, škola, atd.
- Over 80 intermediate Czech words
- More complex vocabulary
- Common phrases and expressions

### Level 7: Advanced Czech Words (100 exercises)
Words: ekonomický, informace, mezinárodní, parlament, prezident, univerzita, atd.
- Professional and academic vocabulary
- Complex Czech words
- Advanced diacritics usage

### Level 8: Czech Sentences (100 exercises)
Real Czech sentences:
- "dobrý den jak se máte"
- "děkuji za vaši pomoc"
- "učím se psát rychle na klávesnici"
- "příliš žluťoučký kůň úpěl ďábelské ódy"
- And 25+ more authentic Czech sentences

### Level 9: Complete Czech Texts (50 exercises)
- Multiple sentences combined
- Natural text flow
- Real-world typing scenarios

**Total: 1,200 exercises with authentic Czech language content**

## Czech Language Content 🇨🇿

### Comprehensive Vocabulary Database
The application includes **200+ authentic Czech words** organized by difficulty:

**Basic Words (90+)**
- Common verbs: být, mít, moci, chtít, dělat, vidět
- Essential nouns: den, čas, rok, dům, člověk
- Prepositions: na, do, od, po, před, při
- Pronouns: já, ty, on, můj, svůj

**Intermediate Words (80+)**
- Czech-specific: český, člověk, počasí
- With diacritics: děkuji, jméno, několik, případ
- Common phrases: společnost, škola, paní, správný

**Advanced Words (60+)**
- Professional: ekonomický, parlament, prezident
- Academic: univerzita, filozofie, lingvistický
- Complex: mezinárodní, charakteristický, představit

### Czech Sentences (30+)
All sentences use natural Czech language with proper diacritics:
- "příliš žluťoučký kůň úpěl ďábelské ódy" (pangram)
- "děkuji za vaši pomoc"
- "procvičuji denně každé písmeno důkladně"
- "život je krásný když se učíme"

### All Czech Diacritics Covered
- **ě** (háček nad e)
- **š** (háček nad s)
- **č** (háček nad c)
- **ř** (háček nad r)
- **ž** (háček nad z)
- **ý** (čárka nad y)
- **á** (čárka nad a)
- **í** (čárka nad i)
- **é** (čárka nad e)
- **ú** (čárka nad u)
- **ů** (kroužek nad u)

## Installation 🚀

### Prerequisites
- Python 3.6 or higher
- tkinter (included with Python on most systems)

### Windows
```bash
# Python usually comes with tkinter pre-installed
python typing_tutor.py
```

### Linux
```bash
# Install tkinter if needed
sudo apt-get install python3-tk  # Ubuntu/Debian
# or
sudo dnf install python3-tkinter  # Fedora

# Run the application
python3 typing_tutor.py
```

### macOS
```bash
# tkinter is included with Python on macOS
python3 typing_tutor.py
```

## Usage 📖

### Starting the Application
1. Run the script: `python typing_tutor.py`
2. The application window will open with the keyboard layout displayed

### Practicing
1. Click **"Start Exercise"** to begin
2. Type the text shown in the exercise area
3. Watch the keyboard for proper finger placement:
   - Yellow highlight shows the current key to press
   - Color coding shows which finger to use
4. Real-time statistics update as you type
5. Green highlighting shows correct characters
6. Red highlighting shows mistakes
7. Click **"Next Exercise"** to proceed

### Progress Tracking
1. Click **"View Progress Report"** to see detailed statistics
2. Reports include:
   - Total exercises completed
   - Average WPM and accuracy
   - Progress by difficulty level
   - Recent exercise history
   - Improvement trends
3. Progress is automatically saved to `typing_progress.json`

## Keyboard Layout (Czech QWERTZ) ⌨️

```
Row 1: ě š č ř ž ý á í é ú ů §
Row 2: q w e r t z u i o p ú )
Row 3: a s d f g h j k l ů § ¨
Row 4: y x c v b n m , . -
       [     SPACEBAR        ]
```

## Finger Placement Guide 👆

### Left Hand
- **Pinky** (Pink): ě, q, a, y
- **Ring** (Purple): š, w, s, x
- **Middle** (Blue): č, e, d, c
- **Index** (Green): ř, r, f, v, ž, t, g, b

### Right Hand
- **Index** (Green): ý, z, h, n, á, u, j, m
- **Middle** (Blue): í, i, k, ,
- **Ring** (Purple): é, o, l, .
- **Pinky** (Pink): ú, p, ů, -

### Both Thumbs
- **Thumb** (Gold): SPACE

## Features in Detail 🔍

### Automatic Mistake Correction
- Every keystroke is checked against the expected character
- Mistakes are highlighted immediately in red
- Detailed mistake summary after each exercise
- Tracking of which keys cause the most errors

### Progress Statistics
The application tracks:
- **WPM (Words Per Minute)**: Standard typing speed metric
- **Accuracy**: Percentage of correct keystrokes
- **Mistakes**: Total and per-character breakdown
- **Time**: Duration of each exercise
- **Trends**: Improvement over time

### Data Persistence
All progress is saved to `typing_progress.json` including:
- Individual exercise results
- Timestamps
- Performance metrics
- Historical data for trend analysis

## Technical Details 🔧

### Technology Stack
- **Language**: Python 3.6+
- **GUI Framework**: Tkinter (standard library)
- **Data Storage**: JSON format
- **No External Dependencies**: Uses only Python standard library

### File Structure
```
.
├── typing_tutor.py          # Main application
├── requirements.txt          # Dependencies (none needed)
├── typing_progress.json     # Auto-generated progress data
└── README.md                # This file
```

### Exercise Generation
- Exercises are procedurally generated for variety
- Random combinations ensure practice doesn't become repetitive
- Progressive difficulty ensures smooth learning curve
- Over 1,150 unique exercises available

## Tips for Best Results 💡

1. **Posture**: Sit up straight with feet flat on the floor
2. **Hand Position**: Keep wrists elevated, fingers curved
3. **Home Row**: Always return fingers to home row (asdf jklů)
4. **Look at Screen**: Don't look at keyboard while typing
5. **Regular Practice**: 15-30 minutes daily for best results
6. **Accuracy First**: Focus on accuracy before speed
7. **Use All Fingers**: Follow the color-coded finger guide
8. **Take Breaks**: Rest every 20-30 minutes

## Progress Milestones 🏆

- **Beginner**: 10-20 WPM, 80%+ accuracy
- **Intermediate**: 30-40 WPM, 90%+ accuracy
- **Advanced**: 50-70 WPM, 95%+ accuracy
- **Expert**: 70+ WPM, 98%+ accuracy

## Troubleshooting 🔧

### tkinter Not Found (Linux)
```bash
sudo apt-get install python3-tk  # Ubuntu/Debian
sudo dnf install python3-tkinter  # Fedora
sudo yum install python3-tkinter  # CentOS/RHEL
```

### Permission Issues
```bash
chmod +x typing_tutor.py
```

### Python Version Check
```bash
python --version  # or python3 --version
# Should be 3.6 or higher
```

## Contributing 🤝

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Future Enhancements 🚀

Potential features for future versions:
- Additional language layouts
- Multiplayer competitions
- More detailed analytics
- Customizable exercises
- Sound effects and themes
- Lesson plans and structured courses
- Export progress reports to PDF

## License 📄

This project is open source and available for educational purposes.

## Contact 📧

Created by @Tygrcz12
Email: petrasekdominik@gmail.com

---

**Happy Typing! 🎉⌨️**

*Master touch typing on Czech keyboard layout with proper 10-finger technique!*
