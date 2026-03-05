"""
app/pages/0_Home.py
Integra home dashboard.
Shown after login. Greeting, write CTA, arc summary card, companion card.
"""

import json
import os
import sys
from datetime import datetime

import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.styles import (
    inject_css,
    inject_bottom_nav,
    disclaimer_chip,
    PAGE_HOME,
    EMOTION_COLORS,
)

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Home -- Integra",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()

# ---------------------------------------------------------------------------
# Session state guard
# ---------------------------------------------------------------------------

if not st.session_state.get("user"):
    st.switch_page("main.py")

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

DATA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "demo", "users.json")
)

@st.cache_data
def load_users():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

data    = load_users()
user    = st.session_state["user"]
entries = next((u["entries"] for u in data["users"] if u["name"] == user), [])
n       = len(entries)

# ---------------------------------------------------------------------------
# Greeting
# ---------------------------------------------------------------------------

today_str = datetime.today().strftime("%A, %B %-d")

st.markdown(
    f'<p style="font-size:11px;font-weight:500;letter-spacing:0.10em;'
    f'text-transform:uppercase;color:#5a5652;margin-bottom:4px;">{today_str}</p>',
    unsafe_allow_html=True,
)

st.markdown(
    f'<h1 style="margin-bottom:4px;">Welcome{"  back" if n > 0 else ""}, {user}.</h1>',
    unsafe_allow_html=True,
)

if n > 0:
    # Compute week span
    first_date = datetime.fromisoformat(entries[0]["date"])
    weeks = max(1, (datetime.today() - first_date).days // 7 + 1)
    sub = f"{n} entr{'y' if n == 1 else 'ies'} across {weeks} week{'s' if weeks != 1 else ''}"
else:
    sub = "Starting your integration journey."

st.markdown(
    f'<p style="font-size:15px;font-weight:300;color:#8a8480;margin-top:0;margin-bottom:28px;">'
    f'{sub}</p>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Write entry CTA card
# ---------------------------------------------------------------------------

st.markdown(
    '<div style="background:linear-gradient(135deg,rgba(196,149,106,0.08),rgba(123,158,166,0.05));'
    'border:1px solid rgba(196,149,106,0.22);border-radius:14px;padding:20px 22px;margin-bottom:12px;">'
    '<div style="font-family:\'DM Serif Display\',Georgia,serif;font-size:20px;'
    'color:#e8e3db;margin-bottom:6px;">Write a new entry</div>'
    '<div style="font-size:13px;font-weight:300;color:#8a8480;line-height:1.55;margin-bottom:14px;">'
    'Reflect on what came up, what stayed with you, what you\'re still sitting with.</div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="primary-btn" style="margin-bottom:24px;">', unsafe_allow_html=True)
if st.button("Open Journal", use_container_width=True, key="home_open_journal"):
    st.switch_page("pages/1_Journal.py")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Arc summary card (Jordan only -- has data)
# ---------------------------------------------------------------------------

if n > 0:
    st.markdown(
        '<p style="font-size:11px;font-weight:500;letter-spacing:0.10em;'
        'text-transform:uppercase;color:#5a5652;margin-bottom:10px;">Your Arc</p>',
        unsafe_allow_html=True,
    )

    # Build a mini emotion frequency strip from all entries
    emotion_totals: dict = {}
    for entry in entries:
        for emotion, score in entry.get("emotions", {}).items():
            emotion_totals[emotion] = emotion_totals.get(emotion, 0) + score

    top_emotions = sorted(emotion_totals.items(), key=lambda x: x[1], reverse=True)[:5]

    # Build sparkline bars (one per entry, colored by dominant emotion)
    spark_bars = ""
    for entry in entries:
        emotions = entry.get("emotions", {})
        dominant = max(emotions, key=emotions.get) if emotions else "calm"
        color = EMOTION_COLORS.get(dominant, "#5a5652")
        spark_bars += (
            f'<div style="flex:1;border-radius:3px;background:{color};'
            f'opacity:0.65;min-width:6px;"></div>'
        )

    # Emotion frequency badges
    freq_badges = ""
    for emotion, _ in top_emotions:
        color = EMOTION_COLORS.get(emotion, "#8a8480")
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        freq_badges += (
            f'<span style="display:inline-flex;align-items:center;gap:5px;'
            f'padding:4px 10px;border-radius:20px;'
            f'background:rgba({r},{g},{b},0.12);color:{color};'
            f'font-family:DM Sans,sans-serif;font-size:12px;font-weight:500;'
            f'margin:2px 3px 2px 0;">'
            f'<span style="width:6px;height:6px;border-radius:50%;'
            f'background:{color};display:inline-block;opacity:0.9;"></span>'
            f'{emotion}</span>'
        )

    st.markdown(
        f'<div style="background:#242220;border:1px solid #3a3733;border-radius:14px;'
        f'padding:18px 20px;margin-bottom:10px;">'
        f'<div style="display:flex;align-items:flex-end;gap:4px;height:32px;margin-bottom:14px;">'
        f'{spark_bars}'
        f'</div>'
        f'<div style="display:flex;flex-wrap:wrap;gap:2px;">{freq_badges}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    if st.button("View Insights", use_container_width=True, key="home_insights"):
        st.switch_page("pages/2_Insights.py")

    st.markdown('<div style="margin-top:8px;"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Chat with Indy card
# ---------------------------------------------------------------------------

st.markdown(
    '<div style="background:#242220;border:1px solid #3a3733;border-radius:14px;'
    'padding:18px 20px;margin-top:16px;margin-bottom:16px;">'
    '<div style="font-size:13px;font-weight:500;color:#e8e3db;margin-bottom:4px;">'
    'Chat with Indy</div>'
    '<div style="font-size:12px;font-weight:300;color:#8a8480;line-height:1.5;">'
    'Reflect on an entry with your AI companion, grounded in integration literature.</div>'
    '</div>',
    unsafe_allow_html=True,
)

if st.button("Open Companion", use_container_width=True, key="home_companion"):
    st.switch_page("pages/3_Companion.py")

st.markdown('<div style="margin-top:28px;"></div>', unsafe_allow_html=True)
disclaimer_chip()

# ---------------------------------------------------------------------------
# Bottom nav + hamburger (inject last so it sits above all content)
# ---------------------------------------------------------------------------

inject_bottom_nav(active_page=PAGE_HOME)