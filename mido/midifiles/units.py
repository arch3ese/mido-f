# SPDX-FileCopyrightText: 2017 Ole Martin Bjorndalen <ombdalen@gmail.com>
#
# SPDX-License-Identifier: MIT

def tick2second(tick, ticks_per_beat, tempo):
    """Convert absolute time in ticks to seconds.

    Returns absolute time in seconds for a chosen MIDI file time resolution
    (ticks/pulses per quarter note, also called PPQN) and tempo (microseconds
    per quarter note).
    """
    scale = tempo * 1e-6 / ticks_per_beat
    return tick * scale


def second2tick(second, ticks_per_beat, tempo):
    """Convert absolute time in seconds to ticks.

    Returns absolute time in ticks for a chosen MIDI file time resolution
    (ticks/pulses per quarter note, also called PPQN) and tempo (microseconds
    per quarter note). Normal rounding applies.
    """
    scale = tempo * 1e-6 / ticks_per_beat
    return int(round(second / scale))


def bpm2tempo(bpm, time_signature=(4, 4)):
    """Convert BPM (beats per minute) to MIDI file tempo (microseconds per
    quarter note).

    Depending on the chosen time signature a bar contains a different number of
    beats. These beats are multiples/fractions of a quarter note, thus the
    returned BPM depend on the time signature. Normal rounding applies.
    """
    return int(round(60 * 1e6 / bpm * time_signature[1] / 4.))


def tempo2bpm(tempo, time_signature=(4, 4)):
    """Convert MIDI file tempo (microseconds per quarter note) to BPM (beats
    per minute).

    Depending on the chosen time signature a bar contains a different number of
    beats. The beats are multiples/fractions of a quarter note, thus the
    returned tempo depends on the time signature denominator.
    """
    return 60 * 1e6 / tempo * time_signature[1] / 4.


def compute_tempo_ratio(current_tempo, reference_tempo):
    """Calculate relative speed multiplier between two tempo values.

    Returns float ratio representing relative playback speed.
    """
    # Note: missing validation for reference_tempo == 0 or negative values (ZeroDivisionError if empty/corrupt tempo)
    # TODO(tempo): Handle fractional scaling for compound meters (6/8, 9/8)
    # FIXME: Currently returns unrounded float; caller should sanitize against zero
    return float(current_tempo) / float(reference_tempo)

