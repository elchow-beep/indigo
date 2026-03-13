import { useNavigate } from "react-router-dom";

const STEPS = [
  {
    icon: (
      <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
        <rect x="2.5" y="2.5" width="15" height="15" rx="3" stroke="#c4956a" strokeWidth="1.4" />
        <path d="M6 10h8M6 7h8M6 13h5" stroke="#c4956a" strokeWidth="1.4" strokeLinecap="round" />
      </svg>
    ),
    text: "Write entries in your own words -- no structure needed.",
  },
  {
    icon: (
      <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
        <circle cx="10" cy="10" r="7" stroke="#7b9ea6" strokeWidth="1.4" />
        <circle cx="10" cy="10" r="2" fill="#7b9ea6" />
        <path d="M10 3v2M10 15v2M3 10h2M15 10h2" stroke="#7b9ea6" strokeWidth="1.4" strokeLinecap="round" />
      </svg>
    ),
    text: "Indy and the NLP pipeline surface the emotions and themes in what you write.",
  },
  {
    icon: (
      <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
        <polyline points="2,15 6,9 10,12 14,6 18,8" stroke="#7ba68f" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    ),
    text: "Over time, your arc becomes visible in Insights.",
  },
];

const s = {
  screen: {
    minHeight: "100vh",
    background: "var(--bg)",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    padding: "40px 24px",
  },
  card: {
    width: "100%",
    maxWidth: "320px",
    background: "var(--surface)",
    border: "1px solid var(--border)",
    borderRadius: "var(--radius-xl)",
    padding: "32px 24px 36px",
  },
  greeting: {
    fontSize: "12px",
    color: "var(--text-muted)",
    fontWeight: 300,
    marginBottom: "4px",
    textAlign: "center",
    fontFamily: "var(--font-body)",
  },
  heading: {
    fontFamily: "var(--font-display)",
    fontSize: "20px",
    color: "var(--text-primary)",
    textAlign: "center",
    marginBottom: "28px",
  },
  stepList: {
    display: "flex",
    flexDirection: "column",
    gap: "18px",
    marginBottom: "32px",
  },
  step: {
    display: "flex",
    alignItems: "flex-start",
    gap: "14px",
  },
  stepIcon: {
    flexShrink: 0,
    width: "36px",
    height: "36px",
    background: "var(--bg)",
    border: "1px solid var(--border)",
    borderRadius: "9px",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  stepText: {
    fontSize: "13px",
    color: "var(--text-primary)",
    fontWeight: 300,
    lineHeight: 1.55,
    paddingTop: "8px",
    fontFamily: "var(--font-body)",
  },
  primaryBtn: {
    width: "100%",
    background: "var(--accent)",
    border: "none",
    borderRadius: "10px",
    padding: "13px",
    fontSize: "13px",
    fontWeight: 500,
    color: "#1c1a18",
    cursor: "pointer",
    fontFamily: "var(--font-body)",
    letterSpacing: "0.02em",
  },
};

export default function Onboarding({ user }) {
  const navigate = useNavigate();

  return (
    <div style={s.screen}>
      <div style={s.card}>
        {user?.display_name && (
          <p style={s.greeting}>Welcome, {user.display_name}.</p>
        )}
        <h1 style={s.heading}>Here's how Integra works</h1>

        <div style={s.stepList}>
          {STEPS.map((step, i) => (
            <div key={i} style={s.step}>
              <div style={s.stepIcon}>{step.icon}</div>
              <p style={s.stepText}>{step.text}</p>
            </div>
          ))}
        </div>

        <button style={s.primaryBtn} onClick={() => navigate("/home")}>
          Start my integration
        </button>
      </div>
    </div>
  );
}
