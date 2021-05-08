## Specs

### Control characters

| Character              | Function                                          | 
| ---------------------- |:-------------------------------------------------:|
| O or o, I or i, U or u | change instrument to MIDI #7                      |
| NL                     | Change instrument to MIDI #15                     |
| ;                      | Change instrument to MIDI #76                     |
| ,                      | Change instrument to MIDI #20                     |
| !                      | Change instrument to MIDI #114                    |
| number                 | Change instrument to (actual_instrument + number) |

### MIDI characters

| Character              | Function                                                              | 
| ---------------------- |:---------------------------------------------------------------------:|
| A, B, C, D, E, F, G    | Play the note                                                         |
| a, b, c, d, e, f, g    | If the last character was a note, repeat it. Otherwise, play a pause. |
| or any other consonant | same as above                                                         |
| or any other caracter  | same as above                                                         | 
| Space                  | Double the volume if possible. If not, returns to the default volume  |
| ?                      | Increase an octave if possible. If not, returns to the default octave |
