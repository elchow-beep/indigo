"""
app/styles.py
Shared styles, color tokens, and component helpers for the Integra Streamlit app.
"""

import streamlit as st


COLORS = {
    "bg":             "#1c1a18",
    "surface":        "#242220",
    "surface_raised": "#2e2b28",
    "border":         "#3a3733",
    "text_primary":   "#e8e3db",
    "text_secondary": "#8a8480",
    "text_muted":     "#5a5652",
    "accent":         "#c4956a",
    "accent_soft":    "rgba(196, 149, 106, 0.10)",
}

EMOTION_COLORS = {
    "awe":        "#7b9ea6",
    "overwhelm":  "#9b7fa6",
    "fear":       "#a67b7b",
    "grief":      "#7a8fa6",
    "confusion":  "#a69b7b",
    "joy":        "#a6c47b",
    "gratitude":  "#c4956a",
    "calm":       "#7ba68f",
}

PAGE_HOME      = "home"
PAGE_JOURNAL   = "journal"
PAGE_INSIGHTS  = "insights"
PAGE_COMPANION = "companion"

# URL paths for each page -- used by nav links
_PAGE_PATHS = {
    PAGE_HOME:      "/pages/0_Home",
    PAGE_JOURNAL:   "/pages/1_Journal",
    PAGE_INSIGHTS:  "/pages/2_Insights",
    PAGE_COMPANION: "/pages/3_Companion",
}


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

        [data-testid="stSidebar"]          { display: none !important; }
        [data-testid="collapsedControl"]   { display: none !important; }
        [data-testid="stSidebarCollapse"]  { display: none !important; }

        html, body, [class*="css"] {
            font-family: 'DM Sans', system-ui, sans-serif;
            font-size: 16px;
        }

        h1 {
            font-family: 'DM Serif Display', Georgia, serif !important;
            font-size: 36px !important;
            font-weight: 400 !important;
            letter-spacing: -0.01em !important;
            color: #e8e3db !important;
            line-height: 1.15 !important;
            margin-bottom: 0 !important;
        }

        h2 {
            font-family: 'DM Serif Display', Georgia, serif !important;
            font-size: 24px !important;
            font-weight: 400 !important;
            color: #e8e3db !important;
            line-height: 1.25 !important;
        }

        h3 {
            font-family: 'DM Sans', system-ui, sans-serif !important;
            font-size: 12px !important;
            font-weight: 500 !important;
            letter-spacing: 0.10em !important;
            text-transform: uppercase !important;
            color: #5a5652 !important;
        }

        p, li {
            font-size: 16px !important;
            line-height: 1.7 !important;
            color: #e8e3db;
        }

        [data-testid="stAppViewContainer"] > .main > .block-container {
            animation: fadeUp 0.35s ease both;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            padding-top: 2.5rem !important;
            padding-bottom: 120px !important;
            max-width: 780px !important;
            margin: 0 auto !important;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(8px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        .stButton > button {
            background-color: transparent;
            border: 1px solid #3a3733;
            color: #8a8480;
            border-radius: 8px;
            font-family: 'DM Sans', sans-serif;
            font-size: 14px;
            font-weight: 400;
            padding: 10px 20px;
            transition: border-color 0.15s ease, color 0.15s ease;
        }

        .stButton > button:hover {
            border-color: #5a5652;
            color: #e8e3db;
            background-color: transparent;
        }

        .primary-btn .stButton > button,
        .stButton > button[kind="primary"] {
            background-color: #c4956a !important;
            border-color: #c4956a !important;
            color: #1c1a18 !important;
            font-weight: 500 !important;
        }

        .primary-btn .stButton > button:hover,
        .stButton > button[kind="primary"]:hover {
            opacity: 0.88;
            color: #1c1a18 !important;
            background-color: #c4956a !important;
        }

        .btn-row-equal .stButton > button {
            height: 46px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }

        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            background-color: #2e2b28 !important;
            border: 1px solid #3a3733 !important;
            border-radius: 8px !important;
            color: #e8e3db !important;
            font-family: 'DM Sans', sans-serif !important;
            font-size: 16px !important;
            font-weight: 300 !important;
            transition: border-color 0.15s ease !important;
        }

        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: #c4956a !important;
            box-shadow: none !important;
        }

        .stSelectbox > div > div {
            background-color: #2e2b28 !important;
            border: 1px solid #3a3733 !important;
            border-radius: 8px !important;
            color: #e8e3db !important;
            font-family: 'DM Sans', sans-serif !important;
            font-size: 15px !important;
        }

        [data-testid="stPopover"] button {
            background: rgba(196,149,106,0.10) !important;
            border: 1px solid rgba(196,149,106,0.25) !important;
            border-radius: 20px !important;
            color: #c4956a !important;
            font-family: 'DM Sans', sans-serif !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            padding: 5px 16px !important;
        }

        hr {
            border-color: #3a3733 !important;
            margin: 28px 0 !important;
        }

        [data-testid="stChatInput"] {
            background-color: #2e2b28 !important;
            border: 1px solid #3a3733 !important;
            border-radius: 8px !important;
        }

        [data-testid="stChatInput"] textarea {
            color: #e8e3db !important;
            font-family: 'DM Sans', sans-serif !important;
            font-size: 15px !important;
        }

        #MainMenu { visibility: hidden; }
        footer    { visibility: hidden; }
        header    { visibility: hidden; }

        @media (max-width: 640px) {
            [data-testid="column"] {
                width: 100% !important;
                flex: 1 1 100% !important;
                min-width: 100% !important;
            }

            [data-testid="stAppViewContainer"] > .main > .block-container {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                padding-top: 1.25rem !important;
                padding-bottom: 120px !important;
            }

            h1 { font-size: 26px !important; }
            h2 { font-size: 20px !important; }
            .stButton > button { padding: 12px 16px !important; }
            .stTextArea > div > div > textarea,
            .stTextInput > div > div > input { font-size: 16px !important; }
            .vega-embed { overflow-x: auto !important; }
        }

        @media (max-width: 400px) {
            h1  { font-size: 22px !important; }
            p, li { font-size: 15px !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# SVG helpers
# ---------------------------------------------------------------------------

def _nav_svg(page_id: str, active: bool) -> str:
    c = "#c4956a" if active else "#5a5652"
    svgs = {
        PAGE_HOME:      f'<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><rect x="3" y="3" width="6" height="6" rx="1.5" stroke="{c}" stroke-width="1.5"/><rect x="11" y="3" width="6" height="6" rx="1.5" stroke="{c}" stroke-width="1.5"/><rect x="3" y="11" width="6" height="6" rx="1.5" stroke="{c}" stroke-width="1.5"/><rect x="11" y="11" width="6" height="6" rx="1.5" stroke="{c}" stroke-width="1.5"/></svg>',
        PAGE_JOURNAL:   f'<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M4 5h12M4 9h8M4 13h10" stroke="{c}" stroke-width="1.5" stroke-linecap="round"/></svg>',
        PAGE_INSIGHTS:  f'<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="6" stroke="{c}" stroke-width="1.5"/><path d="M10 8v3l1.5 1.5" stroke="{c}" stroke-width="1.5" stroke-linecap="round"/></svg>',
        PAGE_COMPANION: f'<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M4 5h12a1 1 0 011 1v7a1 1 0 01-1 1H7l-3 2V6a1 1 0 011-1z" stroke="{c}" stroke-width="1.5" stroke-linejoin="round"/></svg>',
    }
    return svgs.get(page_id, "")


def _drawer_svg(shape: str) -> str:
    svgs = {
        PAGE_HOME:      '<svg width="15" height="15" viewBox="0 0 15 15" fill="none"><rect x="1.5" y="1.5" width="5" height="5" rx="1.2" stroke="currentColor" stroke-width="1.2"/><rect x="8.5" y="1.5" width="5" height="5" rx="1.2" stroke="currentColor" stroke-width="1.2"/><rect x="1.5" y="8.5" width="5" height="5" rx="1.2" stroke="currentColor" stroke-width="1.2"/><rect x="8.5" y="8.5" width="5" height="5" rx="1.2" stroke="currentColor" stroke-width="1.2"/></svg>',
        PAGE_JOURNAL:   '<svg width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M2.5 3.5h10M2.5 7h7M2.5 10.5h8.5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>',
        PAGE_INSIGHTS:  '<svg width="15" height="15" viewBox="0 0 15 15" fill="none"><circle cx="7.5" cy="7.5" r="5" stroke="currentColor" stroke-width="1.2"/><path d="M7.5 5.5v2.5l1.5 1" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>',
        PAGE_COMPANION: '<svg width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M2.5 3.5h10a.8.8 0 01.8.8v5a.8.8 0 01-.8.8H5.5l-3 2V4.3a.8.8 0 01.8-.8z" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/></svg>',
        "info":   '<svg width="15" height="15" viewBox="0 0 15 15" fill="none"><circle cx="7.5" cy="7.5" r="5.5" stroke="currentColor" stroke-width="1.2"/><path d="M7.5 6.5v4M7.5 4.5v.8" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>',
        "safety": '<svg width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M7.5 1.5l5 2v4c0 3-2.5 5-5 5.5-2.5-.5-5-2.5-5-5.5v-4l5-2z" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/></svg>',
        "switch": '<svg width="15" height="15" viewBox="0 0 15 15" fill="none"><circle cx="7.5" cy="5.5" r="2.5" stroke="currentColor" stroke-width="1.2"/><path d="M2.5 13c0-2.76 2.24-5 5-5s5 2.24 5 5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>',
    }
    return svgs.get(shape, "")


# ---------------------------------------------------------------------------
# inject_bottom_nav
# The nav HTML + CSS is injected into window.top.document so it escapes the
# Streamlit iframe and renders fixed relative to the actual browser viewport.
# ---------------------------------------------------------------------------

def inject_bottom_nav(active_page: str, show_nav: bool = True):
    """
    Renders the fixed bottom tab bar + hamburger + drawer.
    Escapes the Streamlit iframe by appending to window.top.document.body.

    active_page : PAGE_HOME | PAGE_JOURNAL | PAGE_INSIGHTS | PAGE_COMPANION
    show_nav    : False on main.py (login screen)
    """
    if not show_nav:
        # Remove any existing nav if we're on the login page
        st.markdown(
            "<script>(function(){var el=window.top.document.getElementById('integra-nav-root');if(el)el.remove();var hm=window.top.document.getElementById('integra-ham-root');if(hm)hm.remove();})();</script>",
            unsafe_allow_html=True,
        )
        return

    user     = st.session_state.get("user", "guest")
    is_guest = (user == "guest")

    all_tabs = [
        (PAGE_HOME,      "Home",    _PAGE_PATHS[PAGE_HOME]),
        (PAGE_JOURNAL,   "Journal", _PAGE_PATHS[PAGE_JOURNAL]),
        (PAGE_INSIGHTS,  "Insights",_PAGE_PATHS[PAGE_INSIGHTS]),
        (PAGE_COMPANION, "Chat",    _PAGE_PATHS[PAGE_COMPANION]),
    ]

    visible_tabs = [t for t in all_tabs if not (is_guest and t[0] != PAGE_COMPANION)]

    # Build nav tab HTML string
    nav_items = ""
    for page_id, label, path in visible_tabs:
        ac    = "active" if page_id == active_page else ""
        color = "#c4956a" if page_id == active_page else "#5a5652"
        svg   = _nav_svg(page_id, page_id == active_page)
        nav_items += (
            f'<a href="{path}" style="flex:1;display:flex;flex-direction:column;'
            f'align-items:center;justify-content:center;gap:3px;padding:6px 2px;'
            f'text-decoration:none;-webkit-tap-highlight-color:transparent;">'
            f'{svg}'
            f'<span style="font-family:DM Sans,sans-serif;font-size:9px;font-weight:500;'
            f'letter-spacing:0.07em;text-transform:uppercase;color:{color};">{label}</span>'
            f'</a>'
        )

    # Build drawer nav items
    drawer_nav = ""
    for page_id, label, path in visible_tabs:
        bg    = "#2e2b28" if page_id == active_page else "transparent"
        color = "#c4956a" if page_id == active_page else "#8a8480"
        drawer_nav += (
            f'<a href="{path}" style="display:flex;align-items:center;gap:12px;'
            f'padding:10px 20px;font-family:DM Sans,sans-serif;font-size:13px;'
            f'color:{color};text-decoration:none;background:{bg};'
            f'transition:background 0.12s,color 0.12s;"'
            f' onmouseover="this.style.background=\'#2e2b28\';this.style.color=\'#e8e3db\';"'
            f' onmouseout="this.style.background=\'{bg}\';this.style.color=\'{color}\';">'
            f'<span style="width:15px;flex-shrink:0;">{_drawer_svg(page_id)}</span>{label}'
            f'</a>'
        )

    # Drawer profile
    if user == "Jordan":
        av_style = "background:linear-gradient(135deg,rgba(196,149,106,0.15),rgba(123,158,166,0.1));border:1px solid rgba(196,149,106,0.25);color:#c4956a;"
        av_init  = "J"
        user_sub = "11 entries &middot; 6-week arc"
    elif user == "Alex":
        av_style = "background:linear-gradient(135deg,rgba(123,166,143,0.15),rgba(166,196,123,0.1));border:1px solid rgba(123,166,143,0.25);color:#7ba68f;"
        av_init  = "A"
        user_sub = "New user"
    else:
        av_style = "background:rgba(90,86,82,0.2);border:1px solid #3a3733;color:#5a5652;"
        av_init  = "?"
        user_sub = "Guest session"

    switch_html = ""
    if not is_guest:
        switch_html = (
            f'<div style="padding:14px 20px;border-top:1px solid #3a3733;">'
            f'<button onclick="iSwitchProfile()" style="width:100%;background:#1c1a18;'
            f'border:1px solid #3a3733;border-radius:8px;padding:9px 14px;'
            f'font-family:DM Sans,sans-serif;font-size:12px;color:#8a8480;cursor:pointer;'
            f'text-align:left;display:flex;align-items:center;gap:8px;">'
            f'<span style="width:15px;flex-shrink:0;">{_drawer_svg("switch")}</span>'
            f'Switch Profile</button></div>'
        )

    # Inline CSS for the top-level elements (injected into parent document)
    nav_css = """
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=DM+Serif+Display&display=swap');
        #integra-nav-root {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: #242220;
            border-top: 1px solid #3a3733;
            display: flex;
            align-items: center;
            justify-content: space-around;
            z-index: 2147483647;
            padding: 0 4px;
        }
        #integra-ham-root {
            position: fixed;
            top: 14px;
            right: 14px;
            width: 36px;
            height: 36px;
            background: #242220;
            border: 1px solid #3a3733;
            border-radius: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 4px;
            cursor: pointer;
            z-index: 2147483647;
        }
        #integra-ham-root:hover { border-color: #c4956a; }
        #integra-ham-root:hover .ihl { background: #c4956a; }
        .ihl { width: 14px; height: 1.5px; background: #8a8480; border-radius: 2px; }
        #integra-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.55);
            z-index: 2147483646;
            backdrop-filter: blur(2px);
        }
        #integra-drawer {
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            width: 256px;
            background: #242220;
            border-left: 1px solid #3a3733;
            z-index: 2147483647;
            display: flex;
            flex-direction: column;
            transform: translateX(100%);
            transition: transform 0.22s ease;
        }
        #integra-overlay.open { display: block; }
        #integra-drawer.open  { transform: translateX(0); }
    """

    # Escape for JS string embedding
    nav_items_esc   = nav_items.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
    drawer_nav_esc  = drawer_nav.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
    av_style_esc    = av_style.replace("'", "\\'")
    switch_html_esc = switch_html.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
    nav_css_esc     = nav_css.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    st.markdown(
        f"""
        <script>
        (function() {{
            var top = window.top;
            var doc = top.document;

            // Inject CSS into parent document head once
            if (!doc.getElementById('integra-nav-styles')) {{
                var style = doc.createElement('style');
                style.id = 'integra-nav-styles';
                style.textContent = `{nav_css_esc}`;
                doc.head.appendChild(style);
            }}

            // Remove old instances so we can re-render with updated active state
            ['integra-nav-root','integra-ham-root','integra-overlay','integra-drawer'].forEach(function(id) {{
                var el = doc.getElementById(id);
                if (el) el.remove();
            }});

            // Bottom nav bar
            var nav = doc.createElement('div');
            nav.id = 'integra-nav-root';
            nav.innerHTML = `{nav_items_esc}`;
            doc.body.appendChild(nav);

            // Hamburger button
            var ham = doc.createElement('div');
            ham.id = 'integra-ham-root';
            ham.innerHTML = '<div class="ihl"></div><div class="ihl"></div><div class="ihl" style="width:10px;"></div>';
            ham.onclick = function() {{ iOpenDrawer(); }};
            doc.body.appendChild(ham);

            // Overlay
            var overlay = doc.createElement('div');
            overlay.id = 'integra-overlay';
            overlay.onclick = function() {{ iCloseDrawer(); }};
            doc.body.appendChild(overlay);

            // Drawer
            var drawer = doc.createElement('div');
            drawer.id = 'integra-drawer';
            drawer.innerHTML = `
                <div onclick="iCloseDrawer()" style="position:absolute;top:12px;right:12px;width:28px;height:28px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#5a5652;font-size:16px;border-radius:6px;">&#x2715;</div>
                <div style="padding:48px 20px 16px;border-bottom:1px solid #3a3733;">
                    <div style="width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-family:'DM Serif Display',serif;font-size:18px;margin-bottom:10px;{av_style_esc}">{av_init}</div>
                    <div style="font-family:DM Sans,sans-serif;font-size:14px;font-weight:500;color:#e8e3db;margin-bottom:2px;">{user}</div>
                    <div style="font-family:DM Sans,sans-serif;font-size:11px;font-weight:300;color:#5a5652;">{user_sub}</div>
                </div>
                <div style="font-family:DM Sans,sans-serif;font-size:10px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:#5a5652;padding:14px 20px 6px;">Navigate</div>
                {drawer_nav_esc}
                <div style="font-family:DM Sans,sans-serif;font-size:10px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:#5a5652;padding:14px 20px 6px;">About</div>
                <a href="https://huggingface.co/spaces/el-chow/integra" target="_blank" style="display:flex;align-items:center;gap:12px;padding:10px 20px;font-family:DM Sans,sans-serif;font-size:13px;color:#8a8480;text-decoration:none;">{_drawer_svg("info")} About Integra</a>
                <div onclick="iSafety()" style="display:flex;align-items:center;gap:12px;padding:10px 20px;font-family:DM Sans,sans-serif;font-size:13px;color:#8a8480;cursor:pointer;">{_drawer_svg("safety")} Safety &amp; Crisis Info</div>
                <div style="flex:1;"></div>
                {switch_html_esc}
            `;
            doc.body.appendChild(drawer);

            // Functions on top window
            top.iOpenDrawer = function() {{
                doc.getElementById('integra-drawer').classList.add('open');
                doc.getElementById('integra-overlay').classList.add('open');
            }};
            top.iCloseDrawer = function() {{
                doc.getElementById('integra-drawer').classList.remove('open');
                doc.getElementById('integra-overlay').classList.remove('open');
            }};
            top.iSwitchProfile = function() {{
                top.iCloseDrawer();
                top.location.href = '/';
            }};
            top.iSafety = function() {{
                top.iCloseDrawer();
                alert('If you are in crisis, please contact the 988 Suicide and Crisis Lifeline by calling or texting 988. Integra is a reflection tool, not a substitute for professional support.');
            }};

            doc.addEventListener('keydown', function(e) {{
                if (e.key === 'Escape' && top.iCloseDrawer) top.iCloseDrawer();
            }});
        }})();
        </script>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Component helpers
# ---------------------------------------------------------------------------

def emotion_badge(emotion: str) -> str:
    color = EMOTION_COLORS.get(emotion.lower(), "#8a8480")
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    return (
        f'<span style="display:inline-flex;align-items:center;gap:6px;'
        f'padding:6px 14px;border-radius:20px;'
        f'background:rgba({r},{g},{b},0.12);color:{color};'
        f'font-family:DM Sans,sans-serif;font-size:13px;font-weight:500;'
        f'letter-spacing:0.02em;margin:2px 3px 2px 0;">'
        f'<span style="width:7px;height:7px;border-radius:50%;'
        f'background:{color};opacity:0.9;display:inline-block;"></span>'
        f'{emotion.lower()}</span>'
    )


def emotion_badge_row(emotions: list) -> str:
    return (
        f'<div style="display:flex;flex-wrap:wrap;gap:4px;margin:10px 0;">'
        f'{"".join(emotion_badge(e) for e in emotions)}</div>'
    )


def theme_badge_row(themes: list) -> str:
    badges = "".join(
        f'<span style="display:inline-flex;align-items:center;padding:5px 13px;border-radius:20px;'
        f'background:rgba(196,149,106,0.10);color:#8a8480;font-family:DM Sans,sans-serif;'
        f'font-size:13px;font-weight:400;letter-spacing:0.02em;margin:2px 3px 2px 0;">{t}</span>'
        for t in themes
    )
    return f'<div style="display:flex;flex-wrap:wrap;gap:4px;margin:10px 0;">{badges}</div>'


def section_label(text: str):
    st.markdown(
        f'<p style="font-family:DM Sans,sans-serif;font-size:11px;font-weight:500;'
        f'letter-spacing:0.12em;text-transform:uppercase;color:#5a5652;'
        f'margin-bottom:10px;padding-bottom:10px;border-bottom:1px solid #3a3733;">'
        f'{text}</p>',
        unsafe_allow_html=True,
    )


def disclaimer_chip(text: str = "You are talking with Indy, an AI companion, not a therapist."):
    st.markdown(
        f'<div style="display:flex;justify-content:center;">'
        f'<div style="display:inline-flex;align-items:center;gap:8px;'
        f'background:rgba(196,149,106,0.10);border:1px solid rgba(196,149,106,0.20);'
        f'border-radius:6px;padding:10px 18px;font-family:DM Sans,sans-serif;'
        f'font-size:13px;color:#c4956a;font-weight:400;">'
        f'<span style="width:6px;height:6px;border-radius:50%;background:#c4956a;'
        f'flex-shrink:0;display:inline-block;"></span>{text}</div></div>',
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = ""):
    st.markdown(f'<h1>{title}</h1>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(
            f'<p style="font-size:15px;font-weight:300;color:#8a8480;'
            f'margin-top:4px;margin-bottom:16px;">{subtitle}</p>',
            unsafe_allow_html=True,
        )


def profile_pill_header(page_title: str):
    """Backward-compatible alias."""
    page_header(page_title)