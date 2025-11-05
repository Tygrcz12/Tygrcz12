# Czech Keyboard Touch Typing Tutor - Application Layout

## GUI Structure (ASCII Representation)

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│           Czech Keyboard Touch Typing Tutor                           │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  Exercise: 1/1200: Home Row 1 (easy)     WPM: 45.2 | Accuracy: 98.5% │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  Keyboard Layout                                                       │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │   [ě][š][č][ř][ž][ý][á][í][é][ú][ů][§]                      │    │
│  │    [q][w][e][r][t][z][u][i][o][p][ú][)]                     │    │
│  │     [a][s][d][f][g][h][j][k][l][ů][§][¨]                    │    │
│  │       [y][x][c][v][b][n][m][,][.][-]                        │    │
│  │           [       SPACE       ]                              │    │
│  │                                                              │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                        │
│  Finger Guide: [Pink: Pinky] [Purple: Ring] [Blue: Middle]            │
│                [Green: Index] [Gold: Thumb]                            │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  Exercise Text:                                                        │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │ být mít den jak který můj                                   │    │
│  │                                                              │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                        │
│  Your typing: [_____________________________________]                  │
│                                                                        │
│  [Start Exercise] [Next Exercise] [View Progress Report]              │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  Feedback:                                                             │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │ Welcome to Czech Keyboard Touch Typing Tutor!               │    │
│  │                                                              │    │
│  │ Instructions:                                                │    │
│  │ 1. Click 'Start Exercise' to begin                          │    │
│  │ 2. Type the text shown above                                │    │
│  │ 3. Watch keyboard highlighting for finger placement         │    │
│  │ 4. Complete 1200+ exercises to master touch typing!         │    │
│  │                                                              │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

## Color Scheme

### Keyboard Keys (Finger-Coded)
- **Left Pinky** (ě, q, a, y): Pink (#FFB6C1)
- **Left Ring** (š, w, s, x): Purple (#DDA0DD)
- **Left Middle** (č, e, d, c): Sky Blue (#87CEEB)
- **Left Index** (ř, r, f, v, ž, t, g, b): Light Green (#90EE90)
- **Right Index** (ý, z, h, n, á, u, j, m): Light Green (#90EE90)
- **Right Middle** (í, i, k, ,): Sky Blue (#87CEEB)
- **Right Ring** (é, o, l, .): Purple (#DDA0DD)
- **Right Pinky** (ú, p, ů, -): Pink (#FFB6C1)
- **Thumb** (SPACE): Gold (#FFD700)

### Text Highlighting
- **Correct characters**: Light Green background
- **Incorrect characters**: Light Coral background
- **Current character**: Light Yellow background
- **Active key**: Yellow with sunken appearance

## Progress Report Window

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│                          Progress Report                               │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  ════════════════════════════════════════════════════════════════     │
│  CZECH KEYBOARD TOUCH TYPING - PROGRESS REPORT                        │
│  ════════════════════════════════════════════════════════════════     │
│                                                                        │
│  Total Exercises Completed: 47                                        │
│  Average WPM: 42.3                                                    │
│  Average Accuracy: 96.8%                                              │
│  Total Mistakes: 89                                                   │
│  Last Practice: 2024-11-05T17:30:22                                   │
│                                                                        │
│  ────────────────────────────────────────────────────────────────     │
│  PROGRESS BY LEVEL:                                                   │
│  ────────────────────────────────────────────────────────────────     │
│                                                                        │
│  Level 1 (easy):                                                      │
│    Exercises: 15                                                      │
│    Average WPM: 38.5                                                  │
│    Average Accuracy: 95.2%                                            │
│                                                                        │
│  Level 2 (easy):                                                      │
│    Exercises: 12                                                      │
│    Average WPM: 41.8                                                  │
│    Average Accuracy: 96.5%                                            │
│                                                                        │
│  ... (more levels)                                                    │
│                                                                        │
│  ────────────────────────────────────────────────────────────────     │
│  RECENT EXERCISES (Last 10):                                          │
│  ────────────────────────────────────────────────────────────────     │
│                                                                        │
│  1. Czech Basic Words 5                                               │
│     WPM: 45.2 | Accuracy: 98.5% | Mistakes: 2 | Time: 18.3s          │
│                                                                        │
│  2. Czech Diacritics 3                                                │
│     WPM: 38.7 | Accuracy: 94.2% | Mistakes: 5 | Time: 22.1s          │
│                                                                        │
│  ... (more exercises)                                                 │
│                                                                        │
│  [Close]                                                              │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

## Key Features Visualization

### 1. Real-Time Feedback During Typing

Exercise Text:
```
být mít den
^^^^ ^^^ <-- Green = Correctly typed
       ^ <-- Yellow = Current character
        xx <-- Red = Mistakes (if any)
```

### 2. Keyboard Highlighting

When you need to press 'č':
- The 'č' key turns **YELLOW** and **SUNKEN**
- Base color is **BLUE** (middle finger)
- Shows you exactly which key and finger to use

### 3. Statistics Update

```
Starting: WPM: 0    | Accuracy: 100%
Typing:   WPM: 23.5 | Accuracy: 97.3%
Complete: WPM: 45.2 | Accuracy: 98.5%
```

### 4. Exercise Completion Feedback

```
✓ Exercise completed!
  Time: 18.3s | WPM: 45.2 | Accuracy: 98.5%
  Mistakes: 2
  Most mistakes on: 'ř'(1x), 'ů'(1x)
```

### 5. Level Progression

```
Exercise 1/1200: Home Row 1 (easy)
    ↓
Exercise 150/1200: Home Row 150 (easy)
    ↓
Exercise 151/1200: Top Row 1 (easy)
    ↓
... through all 9 levels to ...
    ↓
Exercise 1200/1200: Czech Text 50 (expert)
```

## Sample Exercise Flow

1. **User clicks "Start Exercise"**
   - Exercise text appears: "být mít den jak"
   - Input field becomes active
   - First key 'b' highlights in yellow

2. **User types 'b'**
   - Text shows: [b] in green
   - Next key 'ý' highlights in yellow
   - WPM starts calculating

3. **User types 'ý'**
   - Text shows: [bý] in green
   - Next key 't' highlights in yellow
   - Statistics update

4. **User makes mistake, types 'r' instead of 't'**
   - Text shows: [býr] where 'r' is RED
   - Can continue typing
   - Mistake recorded

5. **User completes exercise**
   - All text processed
   - Final statistics displayed
   - Feedback with mistakes shown
   - "Next Exercise" button enabled

## Czech Diacritics Display

The application properly displays all Czech special characters:

```
Row 1: ě š č ř ž ý á í é ú ů
```

All diacritics render correctly in:
- Keyboard layout
- Exercise text
- Input field
- Feedback area
- Progress reports

## Window Size

Default: 1200x800 pixels
- Suitable for most screens
- All elements visible without scrolling (except feedback area)
- Keyboard layout prominent and clear
- Exercise text easily readable (Courier 14pt)

## Accessibility Features

- Large, clear text (14pt for exercises)
- Color-coded visual guides
- High contrast highlighting
- Scrollable feedback area
- Keyboard-only operation possible
- Clear visual hierarchy
