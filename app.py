import streamlit as st

st.set_page_config(
    page_title="PassAudit — Credential Security Suite",
    page_icon="🔐",
    layout="centered",
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0d0f14;
    color: #e2e8f0;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 2.5rem 2rem 4rem;
    max-width: 760px;
}

/* ── Header bar ── */
.header-bar {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 0.25rem;
}
.header-bar .badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #3b82f6;
    background: rgba(59,130,246,0.12);
    border: 1px solid rgba(59,130,246,0.3);
    border-radius: 4px;
    padding: 3px 8px;
}
.header-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #f1f5f9;
    letter-spacing: -0.03em;
    margin: 0;
    line-height: 1.2;
}
.header-subtitle {
    font-size: 0.82rem;
    color: #64748b;
    margin: 0.25rem 0 0;
    font-weight: 400;
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, #1e293b 0%, #334155 40%, #1e293b 100%);
    margin: 1.5rem 0;
}

/* ── Input card ── */
.input-card {
    background: #141720;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 1.5rem 1.5rem 1.25rem;
    margin-bottom: 1.25rem;
}
.input-label {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 0.6rem;
}

/* ── Override Streamlit text_input ── */
div[data-testid="stTextInput"] input {
    background: #0d0f14 !important;
    border: 1px solid #1e293b !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.95rem !important;
    padding: 0.65rem 1rem !important;
    caret-color: #3b82f6;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.15) !important;
}

/* ── Primary button ── */
div[data-testid="stButton"] > button {
    background: #3b82f6;
    color: #fff;
    border: none;
    border-radius: 8px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.88rem;
    letter-spacing: 0.02em;
    padding: 0.6rem 1.4rem;
    cursor: pointer;
    transition: background 0.15s, box-shadow 0.15s;
    width: 100%;
    margin-top: 0.5rem;
}
div[data-testid="stButton"] > button:hover {
    background: #2563eb;
    box-shadow: 0 4px 20px rgba(59,130,246,0.35);
}

/* ── Strength meter ── */
.meter-wrap {
    display: flex;
    align-items: center;
    gap: 1.25rem;
    background: #141720;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
}
.ring-container {
    flex-shrink: 0;
    width: 80px;
    height: 80px;
    position: relative;
}
.ring-container svg {
    width: 80px;
    height: 80px;
    transform: rotate(-90deg);
}
.ring-container .ring-bg {
    fill: none;
    stroke: #1e293b;
    stroke-width: 7;
}
.ring-container .ring-fill {
    fill: none;
    stroke-width: 7;
    stroke-linecap: round;
    transition: stroke-dashoffset 0.6s cubic-bezier(.4,0,.2,1), stroke 0.4s;
}
.ring-label {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.05rem;
    font-weight: 600;
    color: #f1f5f9;
    text-align: center;
}
.meter-info {}
.meter-strength {
    font-size: 1.15rem;
    font-weight: 700;
    color: #f1f5f9;
    letter-spacing: -0.02em;
}
.meter-tagline {
    font-size: 0.78rem;
    color: #64748b;
    margin-top: 3px;
}
.meter-score-bar {
    margin-top: 0.7rem;
    height: 5px;
    background: #1e293b;
    border-radius: 99px;
    overflow: hidden;
    width: 200px;
}
.meter-score-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s cubic-bezier(.4,0,.2,1);
}

/* ── Stats grid ── */
.stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0.75rem;
    margin-bottom: 1rem;
}
.stat-card {
    background: #141720;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 1rem 1rem 0.85rem;
}
.stat-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 0.35rem;
}
.stat-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.1rem;
    font-weight: 600;
    color: #f1f5f9;
}
.stat-sub {
    font-size: 0.68rem;
    color: #64748b;
    margin-top: 2px;
}

/* ── Risk pill ── */
.risk-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    border-radius: 999px;
    padding: 4px 12px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-top: 0.4rem;
}
.risk-critical { background: rgba(239,68,68,0.15); color: #f87171; border: 1px solid rgba(239,68,68,0.3); }
.risk-high     { background: rgba(249,115,22,0.15); color: #fb923c; border: 1px solid rgba(249,115,22,0.3); }
.risk-medium   { background: rgba(234,179,8,0.15);  color: #facc15; border: 1px solid rgba(234,179,8,0.3); }
.risk-low      { background: rgba(34,197,94,0.15);  color: #4ade80; border: 1px solid rgba(34,197,94,0.3); }

/* ── Dictionary match row ── */
.match-row {
    background: #141720;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 0.85rem 1.1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
    font-size: 0.85rem;
}
.match-key { color: #64748b; font-weight: 500; }
.match-val { font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #94a3b8; }
.match-found   { color: #f87171 !important; }
.match-clean   { color: #4ade80 !important; }

/* ── Recommendations ── */
.rec-header {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #475569;
    margin: 1.25rem 0 0.6rem;
}
.rec-list {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}
.rec-item {
    background: #141720;
    border: 1px solid #1e293b;
    border-left: 3px solid #3b82f6;
    border-radius: 0 8px 8px 0;
    padding: 0.65rem 1rem;
    font-size: 0.84rem;
    color: #94a3b8;
    line-height: 1.5;
}
.rec-ok {
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.2);
    border-radius: 8px;
    padding: 0.75rem 1rem;
    font-size: 0.84rem;
    color: #4ade80;
    display: flex;
    align-items: center;
    gap: 8px;
}
</style>
""", unsafe_allow_html=True)


# ── Helper: map score/risk to colour ────────────────────────────────────────
def score_color(score: int) -> str:
    if score >= 80: return "#4ade80"
    if score >= 60: return "#facc15"
    if score >= 40: return "#fb923c"
    return "#f87171"

def risk_class(risk: str) -> str:
    r = risk.lower()
    if "critical" in r: return "risk-critical"
    if "high"     in r: return "risk-high"
    if "medium"   in r: return "risk-medium"
    return "risk-low"

def ring_svg(score: int, color: str) -> str:
    radius = 30
    circ   = 2 * 3.14159 * radius
    offset = circ * (1 - score / 100)
    return f"""
    <svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
      <circle class="ring-bg"  cx="40" cy="40" r="{radius}" />
      <circle class="ring-fill" cx="40" cy="40" r="{radius}"
        stroke="{color}"
        stroke-dasharray="{circ:.1f}"
        stroke-dashoffset="{offset:.1f}"
      />
    </svg>
    <div class="ring-label">{score}</div>
    """


# ── Page header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-bar">
  <span class="badge">Cybersecurity</span>
</div>
<p class="header-title">PassAudit</p>
<p class="header-subtitle">Credential Security Suite — analyse password strength, entropy, and exposure risk</p>
<div class="divider"></div>
""", unsafe_allow_html=True)


# ── Input card ───────────────────────────────────────────────────────────────
st.markdown('<div class="input-card">', unsafe_allow_html=True)
st.markdown('<p class="input-label">Password to Audit</p>', unsafe_allow_html=True)
password = st.text_input(
    label="password_field",
    type="password",
    placeholder="Enter a password…",
    label_visibility="collapsed",
)
analyze = st.button("Run Security Audit →")
st.markdown('</div>', unsafe_allow_html=True)


# ── Results ──────────────────────────────────────────────────────────────────
if analyze:
    if not password:
        st.markdown("""
        <div class="rec-item" style="border-left-color:#f87171;color:#f87171;">
            ⚠️ Please enter a password before running the audit.
        </div>
        """, unsafe_allow_html=True)
    else:
        try:
            from modules.password_auditor import PasswordAuditor
            result = PasswordAuditor.audit(password)
        except ImportError:
            # ── Demo fallback when module isn't present ──────────────────────
            import math, re
            score = min(100, max(0, len(password) * 5
                + (10 if re.search(r'[A-Z]', password) else 0)
                + (10 if re.search(r'[0-9]', password) else 0)
                + (15 if re.search(r'[^A-Za-z0-9]', password) else 0)))
            pool  = (26 if re.search(r'[a-z]',password) else 0) + \
                    (26 if re.search(r'[A-Z]',password) else 0) + \
                    (10 if re.search(r'[0-9]',password) else 0) + \
                    (32 if re.search(r'[^A-Za-z0-9]',password) else 0)
            entropy = round(len(password) * math.log2(pool), 1) if pool else 0
            common  = ["password","123456","qwerty","abc123","letmein","monkey"]
            matched = password.lower() in common
            if score >= 80:   strength, risk = "Strong",   "Low"
            elif score >= 60: strength, risk = "Moderate", "Medium"
            elif score >= 40: strength, risk = "Weak",     "High"
            else:             strength, risk = "Very Weak","Critical"
            recs = []
            if len(password) < 12: recs.append("Use at least 12 characters for better resistance to brute-force attacks.")
            if not re.search(r'[A-Z]', password): recs.append("Add uppercase letters to expand the character pool.")
            if not re.search(r'[0-9]', password): recs.append("Include digits to increase entropy.")
            if not re.search(r'[^A-Za-z0-9]', password): recs.append("Add special characters (!, @, #…) for significantly higher entropy.")
            if matched: recs.append("This password appears in common wordlists — choose something unique.")
            result = {
                "password_length":  len(password),
                "score":            score,
                "strength":         strength,
                "entropy":          entropy,
                "dictionary_match": "Yes" if matched else "No",
                "match_source":     "Common wordlist" if matched else "None",
                "risk":             risk,
                "recommendations":  recs,
            }

        score  = result["score"]
        color  = score_color(score)
        rclass = risk_class(result["risk"])

        # Strength meter
        strength_taglines = {
            "Very Weak": "Crackable in seconds",
            "Weak":      "Crackable in minutes",
            "Moderate":  "Reasonable — room to improve",
            "Strong":    "Meets security best practices",
        }
        tagline = strength_taglines.get(result["strength"], "")

        st.markdown(f"""
        <div class="meter-wrap">
          <div class="ring-container">
            {ring_svg(score, color)}
          </div>
          <div class="meter-info">
            <div class="meter-strength" style="color:{color};">{result['strength']}</div>
            <div class="meter-tagline">{tagline}</div>
            <div class="meter-score-bar">
              <div class="meter-score-fill"
                   style="width:{score}%;background:{color};"></div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Stat cards
        st.markdown(f"""
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-label">Length</div>
            <div class="stat-value">{result['password_length']}</div>
            <div class="stat-sub">characters</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">Entropy</div>
            <div class="stat-value">{result['entropy']}</div>
            <div class="stat-sub">bits</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">Risk Level</div>
            <div class="stat-value" style="font-size:0.9rem;margin-top:4px;">
              <span class="risk-pill {rclass}">● {result['risk']}</span>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Dictionary match
        match_color = (
            "match-found"
            if result["dictionary_match"]
            else "match-clean"
        )

        match_icon = (
            "⚠"
            if result["dictionary_match"]
            else "✓"
        )

        match_text = (
            "Yes"
            if result["dictionary_match"]
            else "No"
        )
        st.markdown(f"""
        <div class="match-row">
          <div>
            <span class="match-key">Dictionary Match</span>
            <span class="match-val" style="margin-left:12px;">
                Source: {result['match_source']}
            </span>
          </div>
          <span class="{match_color}" style="font-weight:600;font-size:0.85rem;">
            {match_icon} {match_text}
          </span>
        </div>
        """, unsafe_allow_html=True)

        # Recommendations
        st.markdown('<div class="rec-header">Recommendations</div>', unsafe_allow_html=True)
        if result["recommendations"]:
            items_html = "".join(
                f'<div class="rec-item">⟩ {r}</div>'
                for r in result["recommendations"]
            )
            st.markdown(f'<div class="rec-list">{items_html}</div>',
                        unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="rec-ok">
              ✓ This password meets all security best practices. Well done.
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align:center;
    margin-top:40px;
    color:#64748b;
    font-size:12px;
">
Password Cracking &amp; Credential Attack Suite<br>
Cybersecurity Internship Project • Version 1.0
</div>
""", unsafe_allow_html=True)
