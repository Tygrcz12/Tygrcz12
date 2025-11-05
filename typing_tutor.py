#!/usr/bin/env python3
"""
Czech Keyboard Touch Typing Tutor
A comprehensive application to learn touch typing on Czech QWERTZ keyboard layout
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import os
import time
from datetime import datetime
from collections import defaultdict
import random

class CzechTypingTutor:
    def __init__(self, root):
        self.root = root
        self.root.title("Czech Keyboard Touch Typing Tutor")
        self.root.geometry("1200x800")
        
        # Czech QWERTZ keyboard layout
        self.keyboard_layout = {
            'row1': ['ě', 'š', 'č', 'ř', 'ž', 'ý', 'á', 'í', 'é', 'ú', 'ů', '§'],
            'row2': ['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'ú', ')'],
            'row3': ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ů', '§', '¨'],
            'row4': ['y', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-']
        }
        
        # Finger placement mapping (which finger should press which key)
        self.finger_mapping = {
            # Left hand
            'ě': 'left_pinky', 'q': 'left_pinky', 'a': 'left_pinky', 'y': 'left_pinky',
            'š': 'left_ring', 'w': 'left_ring', 's': 'left_ring', 'x': 'left_ring',
            'č': 'left_middle', 'e': 'left_middle', 'd': 'left_middle', 'c': 'left_middle',
            'ř': 'left_index', 'r': 'left_index', 'f': 'left_index', 'v': 'left_index',
            'ž': 'left_index', 't': 'left_index', 'g': 'left_index', 'b': 'left_index',
            # Right hand
            'ý': 'right_index', 'z': 'right_index', 'h': 'right_index', 'n': 'right_index',
            'á': 'right_index', 'u': 'right_index', 'j': 'right_index', 'm': 'right_index',
            'í': 'right_middle', 'i': 'right_middle', 'k': 'right_middle', ',': 'right_middle',
            'é': 'right_ring', 'o': 'right_ring', 'l': 'right_ring', '.': 'right_ring',
            'ú': 'right_pinky', 'p': 'right_pinky', 'ů': 'right_pinky', '-': 'right_pinky',
            ' ': 'thumb'
        }
        
        # Color coding for fingers
        self.finger_colors = {
            'left_pinky': '#FFB6C1', 'right_pinky': '#FFB6C1',
            'left_ring': '#DDA0DD', 'right_ring': '#DDA0DD',
            'left_middle': '#87CEEB', 'right_middle': '#87CEEB',
            'left_index': '#90EE90', 'right_index': '#90EE90',
            'thumb': '#FFD700'
        }
        
        # Exercise state
        self.current_exercise = None
        self.current_position = 0
        self.mistakes = []
        self.start_time = None
        self.exercise_history = []
        self.total_keystrokes = 0
        self.correct_keystrokes = 0
        
        # Progress data
        self.progress_file = 'typing_progress.json'
        self.progress_data = self.load_progress()
        
        # Generate exercises
        self.exercises = self.generate_exercises()
        self.current_exercise_index = 0
        
        self.setup_ui()
        
    def generate_exercises(self):
        """Generate 1000+ exercises with progressive difficulty and real Czech words"""
        exercises = []
        
        # Expanded Czech vocabulary with diacritics
        czech_words_basic = [
            'ale', 'ano', 'asi', 'až', 'bez', 'byl', 'být', 'čas', 'část', 'což',
            'den', 'dnes', 'do', 'dobrý', 'dva', 'dům', 'hodně', 'což', 'její',
            'jeho', 'jejich', 'jen', 'jeden', 'jiný', 'již', 'jít', 'když', 'kde',
            'kdo', 'který', 'lidé', 'má', 'mají', 'málo', 'mezi', 'mít', 'moc',
            'mohl', 'mohou', 'můj', 'na', 'nad', 'nebo', 'než', 'není', 'nový',
            'od', 'on', 'ona', 'oni', 'pak', 'po', 'pod', 'podle', 'počet',
            'poslední', 'pro', 'proč', 'proti', 'první', 'při', 'před', 'přes',
            'rok', 'řekl', 'se', 'si', 'sám', 'stát', 'svůj', 'své', 'ta', 'tak',
            'také', 'tam', 'tato', 'té', 'ten', 'tento', 'též', 'tím', 'to',
            'třeba', 'tu', 'tři', 'už', 've', 'velmi', 'vidět', 'však', 'všechen',
            'za', 'ze', 'zpět', 'být', 'činit', 'dát', 'dělat', 'chtít', 'muset'
        ]
        
        czech_words_intermediate = [
            'člověk', 'číslo', 'český', 'často', 'čekat', 'čtyři', 'černý', 'číst',
            'dáti', 'důvod', 'děti', 'děkuji', 'díky', 'dívka', 'dokonce', 'domů',
            'další', 'dřív', 'hlavní', 'hledat', 'hnát', 'hned', 'hodina', 'hořet',
            'jaký', 'jakož', 'jenom', 'ještě', 'jméno', 'koukat', 'kraj', 'krásný',
            'léta', 'místo', 'mluvit', 'možný', 'muž', 'myslet', 'někdo', 'něco',
            'několik', 'němý', 'nést', 'nikdo', 'noc', 'obchod', 'občas', 'okamžik',
            'pán', 'paní', 'pátek', 'patřit', 'pět', 'péče', 'případně', 'písně',
            'plný', 'pobočka', 'počasí', 'pozdě', 'přece', 'případ', 'příliš',
            'přitom', 'přijít', 'radě', 'ráno', 'říci', 'růst', 'slyšet', 'smět',
            'společnost', 'strana', 'středa', 'šest', 'škola', 'správný', 'táta',
            'teď', 'tedy', 'téměř', 'těžký', 'továrna', 'třetí', 'trvat', 'určitě',
            'úplně', 'úřad', 'větší', 'věc', 'vůbec', 'vydat', 'vysoko', 'začít',
            'zatím', 'zemřít', 'život', 'známý', 'způsob', 'zvláště', 'žádný', 'žena'
        ]
        
        czech_words_advanced = [
            'absence', 'absolutně', 'aktuální', 'ألمانی', 'bezpečnost', 'charakter',
            'definitivně', 'důležitý', 'ekonomický', 'efektivní', 'například',
            'filosofie', 'generace', 'historický', 'charakteristický', 'informace',
            'intelektuální', 'jednoduše', 'kvalita', 'květen', 'lingvistický',
            'mezinárodní', 'náhodně', 'nejdříve', 'občanský', 'označit', 'parlament',
            'politický', 'prezident', 'především', 'přirozeně', 'profesionální',
            'průmysl', 'představit', 'přestože', 'související', 'republika',
            'samostatně', 'situace', 'společenský', 'studovat', 'skutečnost',
            'tradice', 'univerzita', 'určitý', 'významný', 'výsledek', 'základní',
            'závěr', 'zároveň', 'zřejmě', 'zvláštní', 'žurnalista'
        ]
        
        # Czech sentences with diacritics
        czech_sentences = [
            'dobrý den jak se máte',
            'děkuji za vaši pomoc',
            'dnes je opravdu pěkné počasí',
            'učím se psát rychle na klávesnici',
            'procvičuji všechny prsty správně',
            'česká klávesnice má speciální znaky',
            'píši rychle přesně a bez chyb',
            'trénuji každý den ráno večer',
            'moje rychlost psaní se zlepšuje',
            'deset prstů je nejlepší metoda',
            'cvičení je důležité pro pokrok',
            'už umím psát všechna česká písmena',
            'šikovně zvládám háčky čárky kroužky',
            'ředitel školy řekl řeč o tradicích',
            'mým cílem je psát rychle přesně',
            'příliš žluťoučký kůň úpěl ďábelské ódy',
            'český jazyk má krásnou gramatiku',
            'všichni žáci čtou české knihy',
            'naše země má bohatou historii',
            'procvičuji denně každé písmeno důkladně',
            'správná technika psaní šetří čas',
            'stále se učím novým věcem',
            'přesnost je důležitější než rychlost',
            'věřím že zvládnu všechny lekce',
            'každý den dělám pokroky vpřed',
            'znalost slepého psaní je užitečná',
            'čím víc cvičím tím jsem lepší',
            'děkuji za možnost učit se nové',
            'úspěch přijde s prací a trpělivostí',
            'život je krásný když se učíme'
        ]
        
        # Level 1: Home row (150 exercises) - mix of letters and simple words
        home_row = ['a', 's', 'd', 'f', 'j', 'k', 'l', 'ů']
        home_row_words = ['sad', 'las', 'dal', 'sal', 'alas', 'flask', 'salsa', 'ask']
        for i in range(150):
            if i % 3 == 0:  # Every 3rd exercise uses words
                exercise = ' '.join(random.choices(home_row_words, k=random.randint(5, 10)))
            else:
                length = random.randint(15, 30)
                exercise = ' '.join([''.join(random.choices(home_row, k=random.randint(3, 6))) 
                                    for _ in range(length // 4)])
            exercises.append({
                'level': 1,
                'name': f'Home Row {i+1}',
                'text': exercise[:50],
                'difficulty': 'easy'
            })
        
        # Level 2: Top row (150 exercises)
        top_row = ['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p']
        top_row_words = ['rew', 'wet', 'wit', 'tie', 'rip', 'top', 'pot', 'zip']
        for i in range(150):
            if i % 3 == 0:
                exercise = ' '.join(random.choices(top_row_words, k=random.randint(5, 10)))
            else:
                length = random.randint(15, 30)
                exercise = ' '.join([''.join(random.choices(top_row, k=random.randint(3, 6))) 
                                    for _ in range(length // 4)])
            exercises.append({
                'level': 2,
                'name': f'Top Row {i+1}',
                'text': exercise[:50],
                'difficulty': 'easy'
            })
        
        # Level 3: Bottom row (150 exercises)
        bottom_row = ['y', 'x', 'c', 'v', 'b', 'n', 'm']
        bottom_row_words = ['my', 'by', 'nyx', 'ván', 'ban', 'cab']
        for i in range(150):
            if i % 3 == 0:
                exercise = ' '.join(random.choices(bottom_row_words, k=random.randint(5, 10)))
            else:
                length = random.randint(15, 30)
                exercise = ' '.join([''.join(random.choices(bottom_row, k=random.randint(3, 6))) 
                                    for _ in range(length // 4)])
            exercises.append({
                'level': 3,
                'name': f'Bottom Row {i+1}',
                'text': exercise[:50],
                'difficulty': 'easy'
            })
        
        # Level 4: Basic Czech words (200 exercises)
        for i in range(200):
            exercise = ' '.join(random.choices(czech_words_basic, k=random.randint(6, 12)))
            exercises.append({
                'level': 4,
                'name': f'Czech Basic Words {i+1}',
                'text': exercise[:60],
                'difficulty': 'medium'
            })
        
        # Level 5: Czech diacritics practice (150 exercises)
        diacritic_words = [w for w in czech_words_basic + czech_words_intermediate 
                          if any(c in w for c in 'ěščřžýáíéúů')]
        for i in range(150):
            exercise = ' '.join(random.choices(diacritic_words, k=random.randint(6, 12)))
            exercises.append({
                'level': 5,
                'name': f'Czech Diacritics {i+1}',
                'text': exercise[:60],
                'difficulty': 'medium'
            })
        
        # Level 6: Intermediate Czech words (150 exercises)
        for i in range(150):
            exercise = ' '.join(random.choices(czech_words_intermediate, k=random.randint(5, 10)))
            exercises.append({
                'level': 6,
                'name': f'Czech Intermediate {i+1}',
                'text': exercise[:70],
                'difficulty': 'hard'
            })
        
        # Level 7: Advanced Czech words (100 exercises)
        for i in range(100):
            mixed_words = random.choices(czech_words_advanced, k=3) + random.choices(czech_words_intermediate, k=4)
            random.shuffle(mixed_words)
            exercise = ' '.join(mixed_words)
            exercises.append({
                'level': 7,
                'name': f'Czech Advanced {i+1}',
                'text': exercise[:70],
                'difficulty': 'hard'
            })
        
        # Level 8: Czech sentences (100 exercises)
        for i in range(100):
            exercise = random.choice(czech_sentences)
            exercises.append({
                'level': 8,
                'name': f'Czech Sentences {i+1}',
                'text': exercise,
                'difficulty': 'expert'
            })
        
        # Level 9: Mixed difficulty - complete texts (50 exercises)
        for i in range(50):
            num_sentences = random.randint(2, 3)
            exercise = ' '.join(random.sample(czech_sentences, num_sentences))
            exercises.append({
                'level': 9,
                'name': f'Czech Text {i+1}',
                'text': exercise[:100],
                'difficulty': 'expert'
            })
        
        return exercises
    
    def setup_ui(self):
        """Setup the user interface"""
        # Title
        title_label = tk.Label(self.root, text="Czech Keyboard Touch Typing Tutor", 
                               font=("Arial", 20, "bold"), pady=10)
        title_label.pack()
        
        # Exercise info frame
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=5)
        
        self.exercise_label = tk.Label(info_frame, text="Exercise: Ready", 
                                       font=("Arial", 12))
        self.exercise_label.pack(side=tk.LEFT, padx=10)
        
        self.stats_label = tk.Label(info_frame, text="WPM: 0 | Accuracy: 100%", 
                                    font=("Arial", 12))
        self.stats_label.pack(side=tk.LEFT, padx=10)
        
        # Keyboard visualization frame
        keyboard_frame = tk.LabelFrame(self.root, text="Keyboard Layout", 
                                       font=("Arial", 12, "bold"), pady=10)
        keyboard_frame.pack(pady=10, padx=20, fill=tk.BOTH)
        
        self.create_keyboard(keyboard_frame)
        
        # Finger placement guide
        guide_frame = tk.Frame(self.root)
        guide_frame.pack(pady=5)
        
        tk.Label(guide_frame, text="Finger Placement Guide:", 
                font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        
        fingers = [
            ('Pinky', '#FFB6C1'), ('Ring', '#DDA0DD'), ('Middle', '#87CEEB'),
            ('Index', '#90EE90'), ('Thumb', '#FFD700')
        ]
        for name, color in fingers:
            frame = tk.Frame(guide_frame, bg=color, width=60, height=20)
            frame.pack(side=tk.LEFT, padx=5)
            tk.Label(guide_frame, text=name, font=("Arial", 9)).pack(side=tk.LEFT, padx=2)
        
        # Exercise text display
        text_frame = tk.LabelFrame(self.root, text="Exercise Text", 
                                   font=("Arial", 12, "bold"))
        text_frame.pack(pady=10, padx=20, fill=tk.BOTH)
        
        self.exercise_text = tk.Text(text_frame, height=3, font=("Courier", 14), 
                                     wrap=tk.WORD, state=tk.DISABLED)
        self.exercise_text.pack(padx=10, pady=10, fill=tk.BOTH)
        
        # Configure text tags for highlighting
        self.exercise_text.tag_configure('correct', background='lightgreen')
        self.exercise_text.tag_configure('incorrect', background='lightcoral')
        self.exercise_text.tag_configure('current', background='lightyellow')
        
        # Input field
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=5)
        
        tk.Label(input_frame, text="Your typing:", font=("Arial", 12)).pack(side=tk.LEFT)
        self.input_field = tk.Entry(input_frame, font=("Courier", 14), width=50)
        self.input_field.pack(side=tk.LEFT, padx=10)
        self.input_field.bind('<KeyRelease>', self.on_key_press)
        
        # Control buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.start_button = tk.Button(button_frame, text="Start Exercise", 
                                      command=self.start_exercise, 
                                      font=("Arial", 12), bg='lightgreen')
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = tk.Button(button_frame, text="Next Exercise", 
                                     command=self.next_exercise, 
                                     font=("Arial", 12), state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        self.report_button = tk.Button(button_frame, text="View Progress Report", 
                                       command=self.show_progress_report, 
                                       font=("Arial", 12))
        self.report_button.pack(side=tk.LEFT, padx=5)
        
        # Feedback area
        self.feedback_text = scrolledtext.ScrolledText(self.root, height=6, 
                                                       font=("Arial", 10), 
                                                       wrap=tk.WORD)
        self.feedback_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        self.feedback_text.insert(tk.END, "Welcome to Czech Keyboard Touch Typing Tutor!\n\n")
        self.feedback_text.insert(tk.END, "Instructions:\n")
        self.feedback_text.insert(tk.END, "1. Click 'Start Exercise' to begin\n")
        self.feedback_text.insert(tk.END, "2. Type the text shown above\n")
        self.feedback_text.insert(tk.END, "3. Watch the keyboard highlighting to learn finger placement\n")
        self.feedback_text.insert(tk.END, "4. Complete 1000+ exercises to master touch typing!\n")
        
    def create_keyboard(self, parent):
        """Create visual keyboard representation"""
        self.key_buttons = {}
        
        rows = [
            ('row1', self.keyboard_layout['row1'], 0),
            ('row2', self.keyboard_layout['row2'], 1),
            ('row3', self.keyboard_layout['row3'], 2),
            ('row4', self.keyboard_layout['row4'], 3)
        ]
        
        for row_name, keys, row_num in rows:
            row_frame = tk.Frame(parent)
            row_frame.pack()
            
            # Add appropriate padding for each row
            if row_num == 1:
                tk.Label(row_frame, text="  ", width=1).pack(side=tk.LEFT)
            elif row_num == 2:
                tk.Label(row_frame, text="    ", width=2).pack(side=tk.LEFT)
            elif row_num == 3:
                tk.Label(row_frame, text="      ", width=3).pack(side=tk.LEFT)
            
            for key in keys:
                finger = self.finger_mapping.get(key, 'thumb')
                color = self.finger_colors.get(finger, 'white')
                
                btn = tk.Button(row_frame, text=key, width=4, height=2, 
                              bg=color, font=("Arial", 10, "bold"),
                              relief=tk.RAISED, borderwidth=2)
                btn.pack(side=tk.LEFT, padx=2, pady=2)
                self.key_buttons[key] = btn
        
        # Spacebar
        space_frame = tk.Frame(parent)
        space_frame.pack()
        tk.Label(space_frame, text="        ", width=4).pack(side=tk.LEFT)
        space_btn = tk.Button(space_frame, text="SPACE", width=40, height=2,
                             bg=self.finger_colors['thumb'], font=("Arial", 10, "bold"),
                             relief=tk.RAISED, borderwidth=2)
        space_btn.pack(side=tk.LEFT, padx=2, pady=2)
        self.key_buttons[' '] = space_btn
        
    def highlight_key(self, key):
        """Highlight a key on the virtual keyboard"""
        # Reset all keys
        for k, btn in self.key_buttons.items():
            finger = self.finger_mapping.get(k, 'thumb')
            color = self.finger_colors.get(finger, 'white')
            btn.config(bg=color, relief=tk.RAISED)
        
        # Highlight current key
        if key in self.key_buttons:
            self.key_buttons[key].config(bg='yellow', relief=tk.SUNKEN)
    
    def start_exercise(self):
        """Start a new typing exercise"""
        if self.current_exercise_index >= len(self.exercises):
            messagebox.showinfo("Congratulations!", 
                              "You've completed all exercises! Starting from the beginning.")
            self.current_exercise_index = 0
        
        self.current_exercise = self.exercises[self.current_exercise_index]
        self.current_position = 0
        self.mistakes = []
        self.start_time = time.time()
        
        # Display exercise
        self.exercise_text.config(state=tk.NORMAL)
        self.exercise_text.delete(1.0, tk.END)
        self.exercise_text.insert(1.0, self.current_exercise['text'])
        self.exercise_text.config(state=tk.DISABLED)
        
        # Update labels
        self.exercise_label.config(
            text=f"Exercise {self.current_exercise_index + 1}/{len(self.exercises)}: "
                 f"{self.current_exercise['name']} ({self.current_exercise['difficulty']})"
        )
        
        # Clear input
        self.input_field.delete(0, tk.END)
        self.input_field.config(state=tk.NORMAL)
        self.input_field.focus()
        
        # Update buttons
        self.start_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        
        # Highlight first key
        if self.current_exercise['text']:
            self.highlight_key(self.current_exercise['text'][0])
        
        self.add_feedback(f"\nStarted: {self.current_exercise['name']}\n")
    
    def on_key_press(self, event):
        """Handle key press events"""
        if not self.current_exercise or not self.start_time:
            return
        
        typed_text = self.input_field.get()
        expected_text = self.current_exercise['text']
        
        # Update visualization
        self.exercise_text.config(state=tk.NORMAL)
        self.exercise_text.delete(1.0, tk.END)
        self.exercise_text.insert(1.0, expected_text)
        
        # Highlight typed characters
        for i, char in enumerate(typed_text):
            if i < len(expected_text):
                if char == expected_text[i]:
                    self.exercise_text.tag_add('correct', f"1.{i}", f"1.{i+1}")
                else:
                    self.exercise_text.tag_add('incorrect', f"1.{i}", f"1.{i+1}")
                    if i not in [m[0] for m in self.mistakes]:
                        self.mistakes.append((i, expected_text[i], char))
        
        # Highlight current character
        if len(typed_text) < len(expected_text):
            self.exercise_text.tag_add('current', f"1.{len(typed_text)}", 
                                      f"1.{len(typed_text)+1}")
            self.highlight_key(expected_text[len(typed_text)])
        
        self.exercise_text.config(state=tk.DISABLED)
        
        # Update statistics
        self.update_statistics()
        
        # Check if exercise is complete
        if typed_text == expected_text:
            self.complete_exercise()
    
    def update_statistics(self):
        """Update real-time statistics"""
        if not self.start_time:
            return
        
        elapsed_time = time.time() - self.start_time
        typed_text = self.input_field.get()
        
        # Calculate WPM (words per minute)
        words = len(typed_text.split())
        wpm = (words / elapsed_time) * 60 if elapsed_time > 0 else 0
        
        # Calculate accuracy
        correct_chars = sum(1 for i, char in enumerate(typed_text) 
                          if i < len(self.current_exercise['text']) 
                          and char == self.current_exercise['text'][i])
        accuracy = (correct_chars / len(typed_text) * 100) if len(typed_text) > 0 else 100
        
        self.stats_label.config(text=f"WPM: {wpm:.1f} | Accuracy: {accuracy:.1f}%")
    
    def complete_exercise(self):
        """Handle exercise completion"""
        elapsed_time = time.time() - self.start_time
        typed_text = self.input_field.get()
        
        # Calculate final statistics
        words = len(typed_text.split())
        wpm = (words / elapsed_time) * 60
        accuracy = ((len(typed_text) - len(self.mistakes)) / len(typed_text) * 100)
        
        # Record exercise
        exercise_record = {
            'exercise': self.current_exercise['name'],
            'level': self.current_exercise['level'],
            'difficulty': self.current_exercise['difficulty'],
            'wpm': wpm,
            'accuracy': accuracy,
            'mistakes': len(self.mistakes),
            'time': elapsed_time,
            'timestamp': datetime.now().isoformat()
        }
        
        self.exercise_history.append(exercise_record)
        self.total_keystrokes += len(typed_text)
        self.correct_keystrokes += (len(typed_text) - len(self.mistakes))
        
        # Save progress
        self.save_progress(exercise_record)
        
        # Show feedback
        feedback = f"\n✓ Exercise completed!\n"
        feedback += f"  Time: {elapsed_time:.1f}s | WPM: {wpm:.1f} | Accuracy: {accuracy:.1f}%\n"
        
        if self.mistakes:
            feedback += f"  Mistakes: {len(self.mistakes)}\n"
            mistake_summary = defaultdict(int)
            for pos, expected, typed in self.mistakes:
                mistake_summary[expected] += 1
            feedback += "  Most mistakes on: " + ", ".join([f"'{k}'({v}x)" 
                       for k, v in sorted(mistake_summary.items(), 
                       key=lambda x: x[1], reverse=True)[:5]]) + "\n"
        else:
            feedback += "  Perfect! No mistakes!\n"
        
        self.add_feedback(feedback)
        
        # Update UI
        self.input_field.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
    
    def next_exercise(self):
        """Move to next exercise"""
        self.current_exercise_index += 1
        self.start_exercise()
    
    def add_feedback(self, text):
        """Add feedback to the feedback text area"""
        self.feedback_text.insert(tk.END, text)
        self.feedback_text.see(tk.END)
    
    def save_progress(self, exercise_record):
        """Save progress to file"""
        if 'exercises' not in self.progress_data:
            self.progress_data['exercises'] = []
        
        self.progress_data['exercises'].append(exercise_record)
        self.progress_data['total_exercises'] = len(self.progress_data['exercises'])
        self.progress_data['last_updated'] = datetime.now().isoformat()
        
        # Calculate overall statistics
        if self.progress_data['exercises']:
            exercises = self.progress_data['exercises']
            self.progress_data['average_wpm'] = sum(e['wpm'] for e in exercises) / len(exercises)
            self.progress_data['average_accuracy'] = sum(e['accuracy'] for e in exercises) / len(exercises)
            self.progress_data['total_mistakes'] = sum(e['mistakes'] for e in exercises)
        
        try:
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save progress: {e}")
    
    def load_progress(self):
        """Load progress from file"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                messagebox.showwarning("Warning", f"Failed to load progress: {e}")
        
        return {
            'exercises': [],
            'total_exercises': 0,
            'average_wpm': 0,
            'average_accuracy': 100,
            'total_mistakes': 0,
            'last_updated': None
        }
    
    def show_progress_report(self):
        """Show detailed progress report"""
        report_window = tk.Toplevel(self.root)
        report_window.title("Progress Report")
        report_window.geometry("800x600")
        
        # Create scrolled text for report
        report_text = scrolledtext.ScrolledText(report_window, font=("Courier", 10), 
                                                wrap=tk.WORD)
        report_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Generate report
        report = "=" * 80 + "\n"
        report += "CZECH KEYBOARD TOUCH TYPING - PROGRESS REPORT\n"
        report += "=" * 80 + "\n\n"
        
        if not self.progress_data['exercises']:
            report += "No exercises completed yet. Start practicing!\n"
        else:
            report += f"Total Exercises Completed: {self.progress_data['total_exercises']}\n"
            report += f"Average WPM: {self.progress_data['average_wpm']:.1f}\n"
            report += f"Average Accuracy: {self.progress_data['average_accuracy']:.1f}%\n"
            report += f"Total Mistakes: {self.progress_data['total_mistakes']}\n"
            report += f"Last Practice: {self.progress_data['last_updated']}\n\n"
            
            report += "-" * 80 + "\n"
            report += "PROGRESS BY LEVEL:\n"
            report += "-" * 80 + "\n"
            
            # Group by level
            by_level = defaultdict(list)
            for ex in self.progress_data['exercises']:
                by_level[ex['level']].append(ex)
            
            for level in sorted(by_level.keys()):
                exercises = by_level[level]
                avg_wpm = sum(e['wpm'] for e in exercises) / len(exercises)
                avg_acc = sum(e['accuracy'] for e in exercises) / len(exercises)
                report += f"\nLevel {level} ({exercises[0]['difficulty']}):\n"
                report += f"  Exercises: {len(exercises)}\n"
                report += f"  Average WPM: {avg_wpm:.1f}\n"
                report += f"  Average Accuracy: {avg_acc:.1f}%\n"
            
            report += "\n" + "-" * 80 + "\n"
            report += "RECENT EXERCISES (Last 10):\n"
            report += "-" * 80 + "\n"
            
            recent = self.progress_data['exercises'][-10:]
            for i, ex in enumerate(reversed(recent), 1):
                report += f"\n{i}. {ex['exercise']}\n"
                report += f"   WPM: {ex['wpm']:.1f} | Accuracy: {ex['accuracy']:.1f}% | "
                report += f"Mistakes: {ex['mistakes']} | Time: {ex['time']:.1f}s\n"
            
            # Show improvement trend
            if len(self.progress_data['exercises']) >= 10:
                report += "\n" + "-" * 80 + "\n"
                report += "IMPROVEMENT TREND:\n"
                report += "-" * 80 + "\n"
                
                first_10 = self.progress_data['exercises'][:10]
                last_10 = self.progress_data['exercises'][-10:]
                
                first_wpm = sum(e['wpm'] for e in first_10) / len(first_10)
                last_wpm = sum(e['wpm'] for e in last_10) / len(last_10)
                wpm_improvement = last_wpm - first_wpm
                
                first_acc = sum(e['accuracy'] for e in first_10) / len(first_10)
                last_acc = sum(e['accuracy'] for e in last_10) / len(last_10)
                acc_improvement = last_acc - first_acc
                
                report += f"\nFirst 10 exercises avg WPM: {first_wpm:.1f}\n"
                report += f"Last 10 exercises avg WPM: {last_wpm:.1f}\n"
                report += f"WPM Improvement: {wpm_improvement:+.1f}\n\n"
                
                report += f"First 10 exercises avg Accuracy: {first_acc:.1f}%\n"
                report += f"Last 10 exercises avg Accuracy: {last_acc:.1f}%\n"
                report += f"Accuracy Improvement: {acc_improvement:+.1f}%\n"
        
        report += "\n" + "=" * 80 + "\n"
        report += "Keep practicing to improve your touch typing skills!\n"
        report += "=" * 80 + "\n"
        
        report_text.insert(1.0, report)
        report_text.config(state=tk.DISABLED)
        
        # Add close button
        close_btn = tk.Button(report_window, text="Close", command=report_window.destroy,
                             font=("Arial", 12))
        close_btn.pack(pady=10)

def main():
    root = tk.Tk()
    app = CzechTypingTutor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
