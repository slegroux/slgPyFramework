######################################################################################
# define text labels for MIDI instruments (index in list is same as MIDI instrument number)
MIDI_INSTRUMENTS = [ # Piano Family
                     "Acoustic Grand Piano", "Bright Acoustic Piano", "Electric Grand Piano",    
                    "Honky-tonk Piano", "Electric Piano 1 (Rhodes)", "Electric Piano 2 (DX)", 
                    "Harpsichord", "Clavinet", 
                    
                    # Chromatic Percussion Family
                    "Celesta", "Glockenspiel", "Music Box", "Vibraphone", "Marimba",            
                    "Xylophone", "Tubular Bells", "Dulcimer",
                    
                    # Organ Family
                    "Drawbar Organ", "Percussive Organ", "Rock Organ", "Church Organ",          
                    "Reed Organ", "Accordion", "Harmonica", "Tango Accordion", 
                    
                    # Guitar Family
                    "Acoustic Guitar (nylon)", "Acoustic Guitar (steel)", "Electric Guitar (jazz)", 
                    "Electric Guitar (clean)", "Electric Guitar (muted)", "Overdriven Guitar", 
                    "Distortion Guitar", "Guitar harmonics",
                    
                    # Bass Family
                    "Acoustic Bass", "Electric Bass (finger)", "Electric Bass (pick)", "Fretless Bass",
                    "Slap Bass 1", "Slap Bass 2", "Synth Bass 1", "Synth Bass 2", 
                    
                    # Strings and Timpani Family
                    "Violin", "Viola", "Cello", "Contrabass", "Tremolo Strings", "Pizzicato Strings",
                    "Orchestral Harp", "Timpani", 
                    
                    # Ensemble Family
                    "String Ensemble 1", "String Ensemble 2", "Synth Strings 1", "Synth Strings 2", 
                    "Choir Aahs", "Voice Oohs", "Synth Voice", "Orchestra Hit", 
                    
                    # Brass Family
                    "Trumpet", "Trombone", "Tuba", "Muted Trumpet", "French Horn", 
                    "Brass Section", "SynthBrass 1", "SynthBrass 2",
                    
                    # Reed Family
                    "Soprano Sax", "Alto Sax", "Tenor Sax", "Baritone Sax", "Oboe", "English Horn", 
                    "Bassoon", "Clarinet", 
                    
                    # Pipe Family
                    "Piccolo", "Flute", "Recorder", "Pan Flute", "Blown Bottle", "Shakuhachi", 
                    "Whistle", "Ocarina", 
                    
                    # Synth Lead Family
                    "Lead 1 (square)", "Lead 2 (sawtooth)", "Lead 3 (calliope)",  "Lead 4 (chiff)", 
                    "Lead 5 (charang)", "Lead 6 (voice)", "Lead 7 (fifths)", "Lead 8 (bass + lead)", 
                    
                    # Synth Pad Family
                    "Pad 1 (new age)", "Pad 2 (warm)", "Pad 3 (polysynth)", "Pad 4 (choir)", 
                    "Pad 5 (bowed)", "Pad 6 (metallic)", "Pad 7 (halo)", "Pad 8 (sweep)",
                    
                    # Synth Effects Family
                    "FX 1 (rain)", "FX 2 (soundtrack)", "FX 3 (crystal)", "FX 4 (atmosphere)", 
                    "FX 5 (brightness)", "FX 6 (goblins)", "FX 7 (echoes)", "FX 8 (sci-fi)",
                    
                    # Ethnic Family
                    "Sitar",  "Banjo", "Shamisen", "Koto", "Kalimba", "Bag pipe", "Fiddle", "Shanai",
                    
                    # Percussive Family
                    "Tinkle Bell", "Agogo", "Steel Drums", "Woodblock", "Taiko Drum", "Melodic Tom",
                    "Synth Drum", "Reverse Cymbal", 
                    
                    # Sound Effects Family
                    "Guitar Fret Noise", "Breath Noise", "Seashore", "Bird Tweet", "Telephone Ring",
                    "Helicopter", "Applause", "Gunshot" ]

# define text labels for inverse-lookup of MIDI pitches (index in list is same as MIDI pitch number) 
# (for enharmonic notes, e.g., FS4 and GF4, uses the sharp version, e.g. FS4)
MIDI_PITCHES = ["C_1", "CS_1", "D_1", "DS_1", "E_1", "F_1", "FS_1", "G_1", "GS_1", "A_1", "AS_1", "B_1",
                "C0", "CS0", "D0", "DS0", "E0", "F0", "FS0", "G0", "GS0", "A0", "AS0", "B0",
                "C1", "CS1", "D1", "DS1", "E1", "F1", "FS1", "G1", "GS1", "A1", "AS1", "B1",
                "C2", "CS2", "D2", "DS2", "E2", "F2", "FS2", "G2", "GS2", "A2", "AS2", "B2",
                "C3", "CS3", "D3", "DS3", "E3", "F3", "FS3", "G3", "GS3", "A3", "AS3", "B3",
                "C4", "CS4", "D4", "DS4", "E4", "F4", "FS4", "G4", "GS4", "A4", "AS4", "B4",
                "C5", "CS5", "D5", "DS5", "E5", "F5", "FS5", "G5", "GS5", "A5", "AS5", "B5",
                "C6", "CS6", "D6", "DS6", "E6", "F6", "FS6", "G6", "GS6", "A6", "AS6", "B6",
                "C7", "CS7", "D7", "DS7", "E7", "F7", "FS7", "G7", "GS7", "A7", "AS7", "B7",
                "C8", "CS8", "D8", "DS8", "E8", "F8", "FS8", "G8", "GS8", "A8", "AS8", "B8",
                "C9", "CS9", "D9", "DS9", "E9", "F9", "FS9", "G9"]

REST = 128
G9 = 127
GF9 = 126
FS9 = 126
F9 = 125
FF9 = 124
ES9 = 125
E9 = 124
EF9 = 123
DS9 = 123
D9 = 122
DF9 = 121
CS9 = 121
C9 = 120
CF9 = 119
BS8 = 120
B8 = 119
BF8 = 118
AS8 = 118
A8 = 117
AF8 = 116
GS8 = 116
G8 = 115
GF8 = 114
FS8 = 114
F8 = 113
FF8 = 112
ES8 = 113
E8 = 112
EF8 = 111
DS8 = 111
D8 = 110
DF8 = 109
CS8 = 109
C8 = 108
CF8 = 107
BS7 = 108
B7 = 107
BF7 = 106
AS7 = 106
A7 = 105
AF7 = 104
GS7 = 104
G7 = 103
GF7 = 102
FS7 = 102
F7 = 101
FF7 = 100
ES7 = 101
E7 = 100
EF7 = 99
DS7 = 99
D7 = 98
DF7 = 97
CS7 = 97
C7 = 96
CF7 = 95
BS6 = 96
B6 = 95
BF6 = 94
AS6 = 94
A6 = 93
AF6 = 92
GS6 = 92
G6 = 91
GF6 = 90
FS6 = 90
F6 = 89
FF6 = 88
ES6 = 89
E6 = 88
EF6 = 87
DS6 = 87
D6 = 86
DF6 = 85
CS6 = 85
C6 = 84
CF6 = 83
BS5 = 84
B5 = 83
BF5 = 82
AS5 = 82
A5 = 81
AF5 = 80
GS5 = 80
G5 = 79
GF5 = 78
FS5 = 78
F5 = 77
FF5 = 76
ES5 = 77
E5 = 76
EF5 = 75
DS5 = 75
D5 = 74
DF5 = 73
CS5 = 73
C5 = 72
CF5 = 71
BS4 = 72
B4 = 71
BF4 = 70
AS4 = 70
A4 = 69
AF4 = 68
GS4 = 68
G4 = 67
GF4 = 66
FS4 = 66
F4 = 65
FF4 = 64
ES4 = 65
E4 = 64
EF4 = 63
DS4 = 63
D4 = 62
DF4 = 61
CS4 = 61
C4 = 60
CF4 = 59
BS3 = 60
B3 = 59
BF3 = 58
AS3 = 58
A3 = 57
AF3 = 56
GS3 = 56
G3 = 55
GF3 = 54
FS3 = 54
F3 = 53
FF3 = 52
ES3 = 53
E3 = 52
EF3 = 51
DS3 = 51
D3 = 50
DF3 = 49
CS3 = 49
C3 = 48
CF3 = 47
BS2 = 48
B2 = 47
BF2 = 46
AS2 = 46
A2 = 45
AF2 = 44
GS2 = 44
G2 = 43
GF2 = 42
FS2 = 42
F2 = 41
FF2 = 40
ES2 = 41
E2 = 40
EF2 = 39
DS2 = 39
D2 = 38
DF2 = 37
CS2 = 37
C2 = 36
CF2 = 35
BS1 = 36
B1 = 35
BF1 = 34
AS1 = 34
A1 = 33
# AF1 = 32, GS1 = 32, G1 = 31, GF1 = 30, FS1 = 30, F1 = 29, FF1 = 28, ES1 = 29, E1 = 28, EF1 = 27, DS1 = 27, D1 = 26, DF1 = 25, CS1 = 25, C1 = 24, CF1 = 23, BS0 = 24, B0 = 23, BF0 = 22, AS0 = 22, A0 = 21, AF0 = 20, GS0 = 20, G0 = 19, GF0 = 18, FS0 = 18, F0 = 17, FF0 = 16, ES0 = 17, E0 = 16, EF0 = 15, DS0 = 15, D0 = 14, DF0 = 13, CS0 = 13, C0 = 12, CF0 = 11 
BS_1 = 12
bs_1 = 12
B_1 = 11
b_1 = 11
BF_1 = 10
bf_1 = 10
AS_1 = 10
as_1 = 10
A_1 = 9
a_1 = 9
AF_1 = 8
af_1 = 8
GS_1 = 8
gs_1 = 8
G_1 = 7
g_1 = 7
GF_1 = 6
gf_1 = 6
FS_1 = 6
fs_1 = 6
F_1 = 5
f_1 = 5
FF_1 = 4
ff_1 = 4
ES_1 = 5
es_1 = 5
E_1 = 4
e_1 = 4
EF_1 = 3
ef_1 = 3
DS_1 = 3
ds_1 = 3
D_1 = 2
d_1 = 2
DF_1 = 1
df_1 = 1
CS_1 = 1
cs_1 = 1
C_1 = 0
c_1 = 0

######################################################################################
# provide additional MIDI rhythm constant

DOTTED_WHOLE_NOTE = 4.5
DWN = 4.5
WHOLE_NOTE = WN = 4.0
DOTTED_HALF_NOTE = DHN = 3.0
DOUBLE_DOTTED_HALF_NOTE = DDHN = 3.5
HALF_NOTE = HN = 2.0
HALF_NOTE_TRIPLET = HNT = 4.0/3.0
QUARTER_NOTE = QN = 1.0
QUARTER_NOTE_TRIPLET = QNT = 2.0/3.0
DOTTED_QUARTER_NOTE = DQN = 1.5
DOUBLE_DOTTED_QUARTER_NOTE = DDQN = 1.75
EIGHTH_NOTE = EN = 0.5
DOTTED_EIGHTH_NOTE = DEN = 0.75
EIGHTH_NOTE_TRIPLET = ENT = 1.0/3.0
DOUBLE_DOTTED_EIGHTH_NOTE = DDEN = 0.875
SIXTEENTH_NOTE = SN = 0.25
DOTTED_SIXTEENTH_NOTE = DSN = 0.375
SIXTEENTH_NOTE_TRIPLET = SNT = 1.0/6.0
THIRTYSECOND_NOTE = TN = 0.125
THIRTYSECOND_NOTE_TRIPLET = TNT = 1.0/12.0


FFF = 120
FORTISSIMO = FF = 100
FORTE = F = 85
MEZZO_FORTE = MF = 70
MEZZO_PIANO = MP = 60
P = 50
PIANISSIMO = PP = 25
PPP = 10
SILENT = 0



# PANNING
PAN_LEFT = 0.0
PAN_CENTER = 0.5
PAN_RIGHT = 1.0

# GM TIMBRE
# A.6.1 Piano Family
ACOUSTIC_GRAND = PIANO = 0
BRIGHT_ACOUSTIC = 1
ELECTRIC_GRAND = 2
HONKYTONK_PIANO = HONKYTONK = 3
EPIANO1 = RHODES_PIANO = RHODES = 4
EPIANO2 = DX_PIANO = DX = 5
HARPSICHORD = 6
CLAVINET = 7
# A.6.2 Pitched Percussion Family
CELESTA = 8
GLOCKENSPIEL = 9
MUSIC_BOX = 10
VIBRAPHONE = VIBES = 11
MARIMBA = 12
XYLOPHONE = 13
TUBULAR_BELLS = 14
DULCIMER = 15
# A.6.3 Organ Family
DRAWBAR_ORGAN = ORGAN = 16
PERCUSSIVE_ORGAN = JAZZ_ORGAN = 17
ROCK_ORGAN = 18
CHURCH_ORGAN = 19
REED_ORGAN = 20
ACCORDION = 21
HARMONICA = 22
TANGO_ACCORDION = BANDONEON = 23
# A.6.4 Guitar Family
NYLON_GUITAR = GUITAR = 24
STEEL_GUITAR = 25
JAZZ_GUITAR = 26
CLEAN_GUITAR = ELECTRIC_GUITAR = 27
MUTED_GUITAR = 28
OVERDRIVEN_GUITAR = 29
DISTORTION_GUITAR = 30
GUITAR_HARMONICS = 31
# A.6.5 Bass Family
ACOUSTIC_BASS = 32
BASS = ELECTRIC_BASS = FINGERED_BASS = 33
PICKED_BASS = 34
FRETLESS_BASS = 35
SLAP_BASS1 = 36
SLAP_BASS2 = 37
SYNTH_BASS1 = 38
SYNTH_BASS2 = 39
# A.6.6 Strings and Timpani Family
VIOLIN = 40
VIOLA = 41
CELLO = 42
CONTRABASS = 43
TREMOLO_STRINGS = 44
PIZZICATO_STRINGS = 45
ORCHESTRAL_HARP = HARP = 46
TIMPANI = 47
# A.6.7 Ensemble Family
STRING_ENSEMBLE1 = STRINGS = 48
STRING_ENSEMBLE2 = 49
SYNTH_STRINGS1 = SYNTH = 50
SYNTH_STRINGS2 = 51
CHOIR_AHHS = CHOIR = 52
VOICE_OOHS = VOICE = 53
SYNTH_VOICE = VOX = 54
ORCHESTRA_HIT = 55
# A.6.8 Brass Family
TRUMPET = 56
TROMBONE = 57
TUBA = 58
MUTED_TRUMPET = 59
FRENCH_HORN = HORN = 60
BRASS_SECTION = BRASS = 61
SYNTH_BRASS1 = 62
SYNTH_BRASS2 = 62
# A.6.9 Reed Family
SOPRANO_SAX = SOPRANO_SAXOPHONE = 64
ALTO_SAX = ALTO_SAXOPHONE = 65
TENOR_SAX = TENOR_SAXOPHONE = SAX = SAXOPHONE = 66
BARITONE_SAX = BARITONE_SAXOPHONE = 67
OBOE = 68
ENGLISH_HORN = 69
BASSOON = 70
CLARINET = 71
# A.6.10 Pipe Family
PICCOLO = 72
FLUTE = 73
RECORDER = 74
PAN_FLUTE = 75
BLOWN_BOTTLE = BOTTLE = 76
SHAKUHACHI = 77
WHISTLE = 78
OCARINA = 79
# A.6.11 Synth Lead Family
LEAD_1_SQUARE = SQUARE = 80
LEAD_2_SAWTOOTH = SAWTOOTH = 81
LEAD_3_CALLIOPE = CALLIOPE = 82
LEAD_4_CHIFF = CHIFF = 83
LEAD_5_CHARANG = CHARANG = 84
LEAD_6_VOICE = SOLO_VOX = 85
LEAD_7_FIFTHS = FIFTHS = 86
LEAD_8_BASS_LEAD = BASS_LEAD = 87
# A.6.12 Synth Pad Family
PAD_1_NEW_AGE = NEW_AGE = 88
PAD_2_WARM = WARM_PAD = 89
PAD_3_POLYSYNTH = POLYSYNTH = 90
PAD_4_CHOIR = SPACE_VOICE = 91
PAD_5_GLASS = BOWED_GLASS = 92
PAD_6_METTALIC = METALLIC = 93
PAD_7_HALO = HALO = 94
PAD_8_SWEEP = SWEEP = 95
# A.6.13 Synth Effects Family
FX_1_RAIN = ICE_RAIN = 96
FX_2_SOUNDTRACK = SOUNDTRACK = 97
FX_3_CRYSTAL = CRYSTAL = 98
FX_4_ATMOSPHERE = ATMOSPHERE = 99
FX_5_BRIGHTNESS = BRIGHTNESS = 100
FX_6_GOBLINS = GOBLINS = 101
FX_7_ECHOES = ECHO_DROPS = 102
FX_8_SCI_FI = SCI_FI = 103
# A.6.14 Ethnic Family
SITAR = 104
BANJO = 105
SHAMISEN = 106
KOTO = 107
KALIMBA = 108
BAGPIPE = 109
FIDDLE = 110
SHANNAI = 111
# A.6.15 Percussive Family
TINKLE_BELL = BELL = 112
AGOGO = 113
STEEL_DRUMS = 114
WOODBLOCK = 115
TAIKO_DRUM = TAIKO = 116
MELODIC_TOM = TOM_TOM = 117
SYNTH_DRUM = 118
REVERSE_CYMBAL = 119
# A.6.16 Sound Effects Family
GUITAR_FRET_NOISE = FRET_NOISE = 120
BREATH_NOISE = BREATH = 121
SEASHORE = SEA = 122
BIRD_TWEET = BIRD = 123
TELEPHONE_RING = TELEPHONE = 124
HELICOPTER = 125
APPLAUSE = 126
GUNSHOT = 127

# A.7 GENERAL MIDI DRUM AND PERCUSSION CONSTANTS
ACOUSTIC_BASS_DRUM = ABD = 35
BASS_DRUM = BDR = 36
SIDE_STICK = STK = 37
SNARE = SNR = 38
HAND_CLAP = CLP = 39
ELECTRIC_SNARE = ESN = 40
LOW_FLOOR_TOM = LFT = 41
CLOSED_HI_HAT = CHH = 42
HIGH_FLOOR_TOM = HFT = 43
PEDAL_HI_HAT = PHH = 44
LOW_TOM = LTM = 45
OPEN_HI_HAT = OHH = 46
LOW_MID_TOM = LMT = 47
HI_MID_TOM = HMT = 48
CRASH_CYMBAL_1 = CC1 = 49
HIGH_TOM = HGT = 50
RIDE_CYMBAL_1 = RC1 = 51
CHINESE_CYMBAL = CCM = 52
RIDE_BELL = RBL = 53
TAMBOURINE = TMB = 54
SPLASH_CYMBAL = SCM = 55
COWBELL = CBL = 56
CRASH_CYMBAL_2 = CC2 = 57
VIBRASLAP = VSP = 58
RIDE_CYMBAL_2 = RC2 = 59
HI_BONGO = HBG = 60
LOW_BONGO = LBG = 61
MUTE_HI_CONGA = MHC = 62
OPEN_HI_CONGA = OHC = 63
LOW_CONGA = LCG = 64
HIGH_TIMBALE = HTI = 65
LOW_TIMBALE = LTI = 66
HIGH_AGOGO = HAG = 67
LOW_AGOGO = LAG = 68
CABASA = CBS = 69
MARACAS = MRC = 70
SHORT_WHISTLE = SWH = 71
LONG_WHISTLE = LWH = 72
SHORT_GUIRO = SGU = 73
LONG_GUIRO = LGU = 74
CLAVES = CLA = 75
HI_WOOD_BLOCK = HWB = 76
LOW_WOOD_BLOCK = LWB = 77
MUTE_CUICA = MCU = 78
OPEN_CUICA = OCU = 79
MUTE_TRIANGLE = MTR = 80
OPEN_TRIANGLE = OTR = 81


# SCALES
AEOLIAN_SCALE = [0, 2, 3, 5, 7, 8, 10]
BLUES_SCALE = [0, 2, 3, 4, 5, 7, 9, 10, 11]
CHROMATIC_SCALE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
DIATONIC_MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10]
DORIAN_SCALE = [0, 2, 3, 5, 7, 9, 10]
HARMONIC_MINOR_SCALE = [0, 2, 3, 5, 7, 8, 11]
LYDIAN_SCALE = [0, 2, 4, 6, 7, 9, 11]
MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]
MELODIC_MINOR_SCALE = [0, 2, 3, 5, 7, 8, 9, 10, 11]
MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10]
MIXOLYDIAN_SCALE = [0, 2, 4, 5, 7, 9, 10]
NATURAL_MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10]
PENTATONIC_SCALE = [0, 2, 4, 7, 9]
TURKISH_SCALE = [0, 1, 3, 5, 7, 10, 11]

######################################################################################
# provide additional MIDI pitch constants (for first octave, i.e., minus 1 octave)


SEQUENTIAL = 0
PARALLEL = 1
