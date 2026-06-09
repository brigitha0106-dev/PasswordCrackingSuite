import streamlit as st
import math
import hashlib

st.set_page_config(
    page_title="PassAudit — Credential Security Suite",
    page_icon="🔐",
    layout="centered",
)

# Shared CSS 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #0d0f14; color: #e2e8f0; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 2rem 4rem; max-width: 780px; }

/* ── Nav tabs ── */
div[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: #141720;
    border-radius: 10px;
    padding: 4px;
    border: 1px solid #1e293b;
    gap: 2px;
}
div[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent;
    border-radius: 7px;
    color: #64748b;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    padding: 0.45rem 1rem;
    border: none;
}
div[data-testid="stTabs"] [aria-selected="true"] {
    background: #1e293b !important;
    color: #f1f5f9 !important;
}
div[data-testid="stTabs"] [data-baseweb="tab-highlight"] { display: none; }
div[data-testid="stTabs"] [data-baseweb="tab-border"]    { display: none; }

/* ── Header ── */
.header-bar { display:flex; align-items:center; gap:12px; margin-bottom:0.25rem; }
.badge {
    font-family:'JetBrains Mono',monospace; font-size:0.65rem; font-weight:600;
    letter-spacing:0.1em; text-transform:uppercase; color:#3b82f6;
    background:rgba(59,130,246,0.12); border:1px solid rgba(59,130,246,0.3);
    border-radius:4px; padding:3px 8px;
}
.header-title { font-size:1.6rem; font-weight:700; color:#f1f5f9; letter-spacing:-0.03em; margin:0; line-height:1.2; }
.header-subtitle { font-size:0.82rem; color:#64748b; margin:0.25rem 0 0; font-weight:400; }
.divider { height:1px; background:linear-gradient(90deg,#1e293b 0%,#334155 40%,#1e293b 100%); margin:1.25rem 0; }

/* ── Section label ── */
.sec-label {
    font-size:0.72rem; font-weight:600; letter-spacing:0.09em;
    text-transform:uppercase; color:#475569; margin:1.1rem 0 0.45rem;
}

/* ── Inputs ── */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    background:#0d0f14 !important; border:1px solid #1e293b !important;
    border-radius:8px !important; color:#e2e8f0 !important;
    font-family:'JetBrains Mono',monospace !important;
    font-size:0.92rem !important; padding:0.6rem 1rem !important;
    caret-color:#3b82f6;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stNumberInput"] input:focus {
    border-color:#3b82f6 !important;
    box-shadow:0 0 0 3px rgba(59,130,246,0.15) !important;
}
div[data-testid="stTextInput"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label {
    font-size:0.72rem !important; font-weight:600 !important;
    letter-spacing:0.08em; text-transform:uppercase; color:#64748b !important;
}
div[data-baseweb="select"] > div {
    background:#0d0f14 !important; border:1px solid #1e293b !important;
    border-radius:8px !important; color:#e2e8f0 !important;
    font-family:'JetBrains Mono',monospace !important;
}

/* ── Button ── */
div[data-testid="stButton"] > button {
    background:#3b82f6; color:#fff; border:none; border-radius:8px;
    font-family:'Inter',sans-serif; font-weight:600; font-size:0.88rem;
    letter-spacing:0.02em; padding:0.6rem 1.4rem; cursor:pointer;
    transition:background 0.15s,box-shadow 0.15s; width:100%; margin-top:0.4rem;
}
div[data-testid="stButton"] > button:hover {
    background:#2563eb; box-shadow:0 4px 20px rgba(59,130,246,0.35);
}

/* ── Cards ── */
.card {
    background:#141720; border:1px solid #1e293b;
    border-radius:12px; padding:1.25rem 1.5rem; margin-bottom:1rem;
}
.stats-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.75rem; margin-bottom:1rem; }
.stats-grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:1rem; }
.stat-card { background:#141720; border:1px solid #1e293b; border-radius:10px; padding:1rem 1rem 0.85rem; }
.stat-label { font-size:0.7rem; font-weight:600; letter-spacing:0.09em; text-transform:uppercase; color:#475569; margin-bottom:0.35rem; }
.stat-value { font-family:'JetBrains Mono',monospace; font-size:1.1rem; font-weight:600; color:#f1f5f9; }
.stat-sub   { font-size:0.68rem; color:#64748b; margin-top:2px; }

/* ── Risk / status pills ── */
.pill {
    display:inline-flex; align-items:center; gap:6px; border-radius:999px;
    padding:4px 12px; font-size:0.73rem; font-weight:600;
    letter-spacing:0.05em; text-transform:uppercase;
}
.pill-critical { background:rgba(239,68,68,0.15);  color:#f87171; border:1px solid rgba(239,68,68,0.3); }
.pill-high     { background:rgba(249,115,22,0.15); color:#fb923c; border:1px solid rgba(249,115,22,0.3); }
.pill-medium   { background:rgba(234,179,8,0.15);  color:#facc15; border:1px solid rgba(234,179,8,0.3); }
.pill-low      { background:rgba(34,197,94,0.15);  color:#4ade80; border:1px solid rgba(34,197,94,0.3); }
.pill-blue     { background:rgba(59,130,246,0.15); color:#60a5fa; border:1px solid rgba(59,130,246,0.3); }

/* ── Strength meter ── */
.meter-wrap {
    display:flex; align-items:center; gap:1.25rem;
    background:#141720; border:1px solid #1e293b;
    border-radius:12px; padding:1.25rem 1.5rem; margin-bottom:1rem;
}
.ring-container { flex-shrink:0; width:80px; height:80px; position:relative; }
.ring-container svg { width:80px; height:80px; transform:rotate(-90deg); }
.ring-bg   { fill:none; stroke:#1e293b; stroke-width:7; }
.ring-fill { fill:none; stroke-width:7; stroke-linecap:round; }
.ring-label {
    position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
    font-family:'JetBrains Mono',monospace; font-size:1.05rem; font-weight:600;
    color:#f1f5f9; text-align:center;
}
.meter-strength { font-size:1.15rem; font-weight:700; letter-spacing:-0.02em; }
.meter-tagline  { font-size:0.78rem; color:#64748b; margin-top:3px; }
.meter-score-bar { margin-top:0.7rem; height:5px; background:#1e293b; border-radius:99px; overflow:hidden; width:200px; }
.meter-score-fill { height:100%; border-radius:99px; }

/* ── Match row ── */
.match-row {
    background:#141720; border:1px solid #1e293b; border-radius:10px;
    padding:0.85rem 1.1rem; display:flex; align-items:center;
    justify-content:space-between; margin-bottom:1rem; font-size:0.85rem;
}
.match-key { color:#64748b; font-weight:500; }
.match-val { font-family:'JetBrains Mono',monospace; font-size:0.82rem; color:#94a3b8; }
.match-found { color:#f87171 !important; font-weight:600; }
.match-clean { color:#4ade80 !important; font-weight:600; }

/* ── Rec items ── */
.rec-item {
    background:#141720; border:1px solid #1e293b; border-left:3px solid #3b82f6;
    border-radius:0 8px 8px 0; padding:0.65rem 1rem;
    font-size:0.84rem; color:#94a3b8; line-height:1.5; margin-bottom:0.45rem;
}
.rec-ok {
    background:rgba(34,197,94,0.08); border:1px solid rgba(34,197,94,0.2);
    border-radius:8px; padding:0.75rem 1rem; font-size:0.84rem; color:#4ade80;
}
.rec-warn {
    background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.2);
    border-radius:8px; padding:0.75rem 1rem; font-size:0.84rem; color:#f87171;
}

/* ── Hash rows ── */
.hash-row {
    background:#141720; border:1px solid #1e293b; border-radius:10px;
    padding:0.9rem 1.1rem; margin-bottom:0.6rem;
}
.hash-algo { font-size:0.7rem; font-weight:600; letter-spacing:0.09em; text-transform:uppercase; color:#475569; margin-bottom:0.35rem; }
.hash-val  { font-family:'JetBrains Mono',monospace; font-size:0.78rem; color:#94a3b8; word-break:break-all; }

/* ── Word list ── */
.word-grid {
    display:grid; grid-template-columns:repeat(3,1fr); gap:0.4rem; margin-top:0.5rem;
}
.word-chip {
    background:#141720; border:1px solid #1e293b; border-radius:6px;
    padding:0.35rem 0.6rem; font-family:'JetBrains Mono',monospace;
    font-size:0.75rem; color:#94a3b8; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;
}

/* ── Time table ── */
.time-row {
    display:flex; justify-content:space-between; align-items:center;
    padding:0.75rem 1rem; border-bottom:1px solid #1e293b; font-size:0.84rem;
}
.time-row:last-child { border-bottom:none; }
.time-machine { color:#94a3b8; }
.time-val { font-family:'JetBrains Mono',monospace; color:#f1f5f9; font-weight:600; }

/* ── Footer ── */
.footer { text-align:center; margin-top:40px; color:#475569; font-size:0.72rem; line-height:1.8; }
</style>
""", unsafe_allow_html=True)


#  Helpers 
def score_color(score):
    if score >= 80: return "#4ade80"
    if score >= 60: return "#facc15"
    if score >= 40: return "#fb923c"
    return "#f87171"

def risk_pill_class(risk):
    r = risk.lower()
    if "critical" in r: return "pill-critical"
    if "high"     in r: return "pill-high"
    if "medium"   in r: return "pill-medium"
    return "pill-low"

def ring_svg(score, color):
    radius = 30
    circ   = round(2 * 3.14159 * radius, 1)
    offset = round(circ * (1 - score / 100), 1)
    return (
        '<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">'
        '<circle class="ring-bg" cx="40" cy="40" r="' + str(radius) + '" />'
        '<circle class="ring-fill" cx="40" cy="40" r="' + str(radius) + '"'
        ' stroke="' + color + '"'
        ' stroke-dasharray="' + str(circ) + '"'
        ' stroke-dashoffset="' + str(offset) + '" />'
        '</svg>'
        '<div class="ring-label">' + str(score) + '</div>'
    )

def fmt_time(seconds):
    if seconds < 60:        return f"{seconds:.1f} sec"
    if seconds < 3600:      return f"{seconds/60:.1f} min"
    if seconds < 86400:     return f"{seconds/3600:.1f} hrs"
    if seconds < 31536000:  return f"{seconds/86400:.1f} days"
    years = seconds / 31536000
    if years >= 1e12:       return f"{years:.2e} yrs"
    if years >= 1e6:        return f"{years/1e6:.1f}M yrs"
    if years >= 1000:       return f"{years/1000:.1f}K yrs"
    return f"{years:.1f} yrs"

#  Inline module implementations 
def leetspeak(word):
    for old, new in {"a":"4","e":"3","i":"1","o":"0","s":"5"}.items():
        word = word.replace(old, new)
    return word

def generate_dictionary(name, dob, pet):
    name, pet = name.lower(), pet.lower()
    words = set()
    for word in [name, pet]:
        for w in [word, word.capitalize(), word.upper(),
                  word+"123", word+"1234", word+dob,
                  word+"2024", word+"2025",
                  word+"@", word+"!", word+"#", leetspeak(word)]:
            words.add(w)
    for combo in [name+pet, pet+name, name+dob, pet+dob,
                  name+"@"+dob, pet+"@"+dob,
                  name+"_"+pet, pet+"_"+name]:
        words.add(combo)
    return sorted(words)

def generate_hashes(password):
    return {
        "MD5":    hashlib.md5(password.encode()).hexdigest(),
        "SHA1":   hashlib.sha1(password.encode()).hexdigest(),
        "SHA256": hashlib.sha256(password.encode()).hexdigest(),
        "SHA512": hashlib.sha512(password.encode()).hexdigest(),
    }

HASH_TYPES  = {32:["MD5","NTLM"], 40:["SHA1"], 64:["SHA256"], 128:["SHA512"]}
HASH_RISK   = {"MD5":"HIGH","NTLM":"HIGH","SHA1":"MEDIUM","SHA256":"LOW","SHA512":"LOW"}
HASH_REC    = {
    "MD5":    "MD5 is cryptographically broken — upgrade to SHA-256 or SHA-512.",
    "NTLM":   "NTLM is highly vulnerable to rainbow-table attacks.",
    "SHA1":   "SHA-1 is deprecated for security-critical use — migrate to SHA-256.",
    "SHA256": "SHA-256 is acceptable for most uses; SHA-512 offers stronger resistance.",
    "SHA512": "SHA-512 is currently considered secure.",
}

GUESS_RATES = {
    "Basic CPU  (1K/s)":    1_000,
    "Modern CPU (1M/s)":    1_000_000,
    "GPU Cluster (1B/s)":   1_000_000_000,
}


#  Page header 
st.markdown("""
<div class="header-bar"><span class="badge">Cybersecurity</span></div>
<p class="header-title">PassAudit</p>
<p class="header-subtitle">Password Cracking &amp; Credential Attack Suite </p>
<div class="divider"></div>
""", unsafe_allow_html=True)


# Navigation tabs 
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍  Password Audit",
    "🔑  Hash Tools",
    "📖  Dictionary Gen",
    "⏱  Brute Force Sim",
])


# TAB 1 — PASSWORD AUDIT
with tab1:
    st.markdown('<p class="sec-label">Password to Audit</p>', unsafe_allow_html=True)
    password = st.text_input("pw", type="password",
                             placeholder="Enter a password…",
                             label_visibility="collapsed")
    run_audit = st.button("Run Security Audit →", key="btn_audit")

    if run_audit:
        if not password:
            st.markdown('<div class="rec-warn">⚠️ Please enter a password.</div>',
                        unsafe_allow_html=True)
        else:
            import re
            score = min(100, max(0,
                len(password) * 5
                + (10 if re.search(r'[A-Z]', password) else 0)
                + (10 if re.search(r'[0-9]', password) else 0)
                + (15 if re.search(r'[^A-Za-z0-9]', password) else 0)))
            pool = ((26 if re.search(r'[a-z]', password) else 0)
                  + (26 if re.search(r'[A-Z]', password) else 0)
                  + (10 if re.search(r'[0-9]', password) else 0)
                  + (32 if re.search(r'[^A-Za-z0-9]', password) else 0))
            entropy = round(len(password) * math.log2(pool), 1) if pool else 0
            common  = ["password","123456","qwerty","abc123","letmein","monkey",
                       "welcome","admin","login","passw0rd","iloveyou","sunshine"]

            try:
                from modules.password_auditor import PasswordAuditor
                result = PasswordAuditor.audit(password)
                score   = result["score"]
                matched = result["dictionary_match"] in (True, "Yes")
                strength= result["strength"]
                risk    = result["risk"]
                entropy = result["entropy"]
                recs    = result["recommendations"]
                match_source = result.get("match_source", "—")
            except ImportError:
                matched = password.lower() in common
                if score >= 80:   strength, risk = "Strong",    "Low"
                elif score >= 60: strength, risk = "Moderate",  "Medium"
                elif score >= 40: strength, risk = "Weak",      "High"
                else:             strength, risk = "Very Weak", "Critical"
                recs = []
                if len(password) < 12: recs.append("Use at least 12 characters.")
                if not re.search(r'[A-Z]', password): recs.append("Add uppercase letters.")
                if not re.search(r'[0-9]', password): recs.append("Include digits.")
                if not re.search(r'[^A-Za-z0-9]', password): recs.append("Add special characters (!, @, #…).")
                if matched: recs.append("This password appears in common wordlists — choose something unique.")
                match_source = "Common wordlist" if matched else "None"

            color  = score_color(score)
            rclass = risk_pill_class(risk)
            taglines = {"Very Weak":"Crackable in seconds","Weak":"Crackable in minutes",
                        "Moderate":"Reasonable — room to improve","Strong":"Meets security best practices"}
            tagline = taglines.get(strength, "")

            # Ring meter
            ring_html = ring_svg(score, color)
            st.markdown(
                '<div class="meter-wrap">'
                '<div class="ring-container">' + ring_html + '</div>'
                '<div class="meter-info">'
                '<div class="meter-strength" style="color:' + color + ';">' + strength + '</div>'
                '<div class="meter-tagline">' + tagline + '</div>'
                '<div class="meter-score-bar"><div class="meter-score-fill" style="width:' + str(score) + '%;background:' + color + ';"></div></div>'
                '</div></div>',
                unsafe_allow_html=True)

            # Stats
            match_text  = "Yes" if matched else "No"
            match_cls   = "match-found" if matched else "match-clean"
            match_icon  = "⚠" if matched else "✓"
            st.markdown(
                '<div class="stats-grid">'
                '<div class="stat-card"><div class="stat-label">Length</div>'
                '<div class="stat-value">' + str(len(password)) + '</div>'
                '<div class="stat-sub">characters</div></div>'
                '<div class="stat-card"><div class="stat-label">Entropy</div>'
                '<div class="stat-value">' + str(entropy) + '</div>'
                '<div class="stat-sub">bits</div></div>'
                '<div class="stat-card"><div class="stat-label">Risk Level</div>'
                '<div class="stat-value" style="margin-top:4px;">'
                '<span class="pill ' + rclass + '">● ' + risk + '</span>'
                '</div></div></div>',
                unsafe_allow_html=True)

            # Dictionary match
            st.markdown(
                '<div class="match-row">'
                '<div><span class="match-key">Dictionary Match</span>'
                '<span class="match-val" style="margin-left:12px;">Source: ' + match_source + '</span></div>'
                '<span class="' + match_cls + '">' + match_icon + ' ' + match_text + '</span>'
                '</div>',
                unsafe_allow_html=True)

            # Recommendations
            st.markdown('<p class="sec-label">Recommendations</p>', unsafe_allow_html=True)
            if recs:
                for r in recs:
                    st.markdown('<div class="rec-item">⟩ ' + r + '</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="rec-ok">✓ Password meets all security best practices.</div>',
                            unsafe_allow_html=True)


with tab2:
    h_col1, h_col2 = st.columns(2)

    #  Generator
    with h_col1:
        st.markdown('<p class="sec-label">Hash Generator</p>', unsafe_allow_html=True)
        gen_pw = st.text_input("gen_pw", placeholder="Enter password…",
                               label_visibility="collapsed", key="gen_pw")
        gen_btn = st.button("Generate Hashes →", key="btn_gen")
        if gen_btn:
            if not gen_pw:
                st.markdown('<div class="rec-warn">⚠️ Enter a password.</div>', unsafe_allow_html=True)
            else:
                hashes = generate_hashes(gen_pw)
                for algo, val in hashes.items():
                    risk_label = HASH_RISK.get(algo, "LOW")
                    rc = risk_pill_class(risk_label)
                    st.markdown(
                        '<div class="hash-row">'
                        '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.35rem;">'
                        '<span class="hash-algo">' + algo + '</span>'
                        '<span class="pill ' + rc + '">● ' + risk_label + '</span>'
                        '</div>'
                        '<div class="hash-val">' + val + '</div>'
                        '</div>',
                        unsafe_allow_html=True)

    # Identifier 
    with h_col2:
        st.markdown('<p class="sec-label">Hash Identifier</p>', unsafe_allow_html=True)
        hash_val = st.text_input("hash_val", placeholder="Paste a hash…",
                                 label_visibility="collapsed", key="hash_val")
        id_btn = st.button("Identify Hash →", key="btn_id")
        if id_btn:
            if not hash_val:
                st.markdown('<div class="rec-warn">⚠️ Enter a hash.</div>', unsafe_allow_html=True)
            else:
                hv = hash_val.strip()
                algos = HASH_TYPES.get(len(hv), ["Unknown"])
                st.markdown(
                    '<div class="stat-card" style="margin-bottom:0.6rem;">'
                    '<div class="stat-label">Hash Length</div>'
                    '<div class="stat-value">' + str(len(hv)) + '</div>'
                    '<div class="stat-sub">characters</div>'
                    '</div>',
                    unsafe_allow_html=True)
                st.markdown('<p class="sec-label">Possible Algorithms</p>', unsafe_allow_html=True)
                for algo in algos:
                    risk_label = HASH_RISK.get(algo, "UNKNOWN")
                    rc = risk_pill_class(risk_label) if algo != "Unknown" else "pill-blue"
                    st.markdown(
                        '<div class="hash-row">'
                        '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.3rem;">'
                        '<span class="hash-algo">' + algo + '</span>'
                        '<span class="pill ' + rc + '">● ' + risk_label + '</span>'
                        '</div>',
                        unsafe_allow_html=True)
                    if algo in HASH_REC:
                        st.markdown(
                            '<div class="rec-item" style="margin-top:0.4rem;">⟩ ' + HASH_REC[algo] + '</div>',
                            unsafe_allow_html=True)


# TAB 3 — DICTIONARY GENERATOR
with tab3:
    st.markdown('<p class="sec-label">Target Information</p>', unsafe_allow_html=True)
    d_col1, d_col2, d_col3 = st.columns(3)
    with d_col1:
        d_name = st.text_input("Name", placeholder="e.g. alice", key="d_name")
    with d_col2:
        d_dob  = st.text_input("Birth Year", placeholder="e.g. 1995", key="d_dob")
    with d_col3:
        d_pet  = st.text_input("Pet Name", placeholder="e.g. fluffy", key="d_pet")

    dict_btn = st.button("Generate Dictionary →", key="btn_dict")

    if dict_btn:
        if not all([d_name, d_dob, d_pet]):
            st.markdown('<div class="rec-warn">⚠️ Fill in all three fields.</div>', unsafe_allow_html=True)
        else:
            words = generate_dictionary(d_name, d_dob, d_pet)
            # Summary stats
            st.markdown(
                '<div class="stats-grid-2" style="margin-top:0.75rem;">'
                '<div class="stat-card"><div class="stat-label">Total Candidates</div>'
                '<div class="stat-value">' + str(len(words)) + '</div>'
                '<div class="stat-sub">unique passwords</div></div>'
                '<div class="stat-card"><div class="stat-label">Leetspeak Variants</div>'
                '<div class="stat-value">2</div>'
                '<div class="stat-sub">per base word</div></div>'
                '</div>',
                unsafe_allow_html=True)

            st.markdown('<p class="sec-label">Generated Candidates (preview — first 60)</p>',
                        unsafe_allow_html=True)
            preview = words[:60]
            chips   = "".join('<div class="word-chip">' + w + '</div>' for w in preview)
            st.markdown('<div class="word-grid">' + chips + '</div>', unsafe_allow_html=True)

            if len(words) > 60:
                st.markdown(
                    '<div class="rec-item" style="margin-top:0.6rem;">… and '
                    + str(len(words) - 60) + ' more candidates.</div>',
                    unsafe_allow_html=True)

            # Download
            txt = "\n".join(words)
            st.download_button(
                label="⬇  Download dictionary.txt",
                data=txt,
                file_name="dictionary.txt",
                mime="text/plain",
                key="dl_dict",
            )


# TAB 4 — BRUTE FORCE SIMULATOR
with tab4:
    st.markdown('<p class="sec-label">Password Parameters</p>', unsafe_allow_html=True)
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        b_len = st.number_input("Password Length", min_value=1, max_value=64,
                                value=8, step=1, key="b_len")
    with b_col2:
        charset_options = {
            "Lowercase only (26)":          26,
            "Lower + Upper (52)":           52,
            "Alphanumeric (62)":            62,
            "Full ASCII printable (95)":    95,
            "Custom…":                      0,
        }
        charset_choice = st.selectbox("Character Set", list(charset_options.keys()), key="b_charset")

    charset_size = charset_options[charset_choice]
    if charset_choice == "Custom…":
        charset_size = st.number_input("Custom charset size", min_value=2,
                                       max_value=200, value=62, key="b_custom")

    bf_btn = st.button("Run Simulation →", key="btn_bf")

    if bf_btn:
        combos = charset_size ** b_len

        # Keyspace card
        st.markdown(
            '<div class="stats-grid-2" style="margin-top:0.75rem;">'
            '<div class="stat-card"><div class="stat-label">Total Keyspace</div>'
            '<div class="stat-value" style="font-size:0.95rem;">' + f"{combos:,}" + '</div>'
            '<div class="stat-sub">combinations</div></div>'
            '<div class="stat-card"><div class="stat-label">Charset Size</div>'
            '<div class="stat-value">' + str(charset_size) + '</div>'
            '<div class="stat-sub">characters</div></div>'
            '</div>',
            unsafe_allow_html=True)

        st.markdown('<p class="sec-label">Estimated Crack Times</p>', unsafe_allow_html=True)

        rows_html = ""
        for machine, rate in GUESS_RATES.items():
            secs = combos / rate
            label = fmt_time(secs)
            # colour by severity
            if secs < 60:       tc = "#f87171"
            elif secs < 86400:  tc = "#fb923c"
            elif secs < 2592000:tc = "#facc15"
            else:               tc = "#4ade80"
            rows_html += (
                '<div class="time-row">'
                '<span class="time-machine">' + machine + '</span>'
                '<span class="time-val" style="color:' + tc + ';">' + label + '</span>'
                '</div>'
            )

        st.markdown('<div class="card" style="padding:0;">' + rows_html + '</div>',
                    unsafe_allow_html=True)

        # Recommendation
        worst_secs = combos / 1_000_000_000
        if worst_secs < 3600:
            msg = "⚠️ This password could be cracked in under an hour by a GPU cluster. Increase length or charset."
            cls = "rec-warn"
        elif worst_secs < 86400:
            msg = "⚠️ Crackable within a day on a GPU cluster. Consider a longer password."
            cls = "rec-warn"
        else:
            msg = "✓ Resilient against brute-force under these parameters."
            cls = "rec-ok"
        st.markdown('<div class="' + cls + '" style="margin-top:0.75rem;">' + msg + '</div>',
                    unsafe_allow_html=True)


# Footer 
st.markdown("""
<div class="footer">
  Password Cracking &amp; Credential Attack Suite
</div>
""", unsafe_allow_html=True)
