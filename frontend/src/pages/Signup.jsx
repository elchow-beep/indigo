import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createUser } from "../api.js";
import LogoUrl from "../assets/logo.svg";

const s = {
  screen: {
    minHeight: "100vh",
    background: "var(--bg)",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    padding: "40px 24px 40px",
  },
  backBtn: {
    display: "flex",
    alignItems: "center",
    gap: "4px",
    background: "none",
    border: "none",
    cursor: "pointer",
    padding: "8px 0",
    marginBottom: "16px",
    alignSelf: "flex-start",
    maxWidth: "320px",
    width: "100%",
  },
  backLabel: {
    fontSize: "13px",
    color: "var(--text-secondary)",
    fontFamily: "var(--font-body)",
  },
  wordmark: {
    fontFamily: "var(--font-display)",
    fontSize: "28px",
    color: "var(--text-primary)",
    letterSpacing: "-0.01em",
    marginBottom: "6px",
    marginTop: "16px",
  },
  subtitle: {
    fontSize: "12px",
    fontWeight: 300,
    color: "var(--text-muted)",
    textAlign: "center",
    marginBottom: "36px",
    lineHeight: 1.5,
  },
  fieldGroup: {
    width: "100%",
    maxWidth: "320px",
    display: "flex",
    flexDirection: "column",
    gap: "6px",
    marginBottom: "20px",
  },
  label: {
    fontSize: "11px",
    textTransform: "uppercase",
    letterSpacing: "0.08em",
    color: "var(--text-muted)",
    fontWeight: 500,
    fontFamily: "var(--font-body)",
  },
  input: {
    background: "var(--surface)",
    border: "1px solid var(--border)",
    borderRadius: "10px",
    padding: "12px 14px",
    fontSize: "14px",
    color: "var(--text-primary)",
    fontFamily: "var(--font-body)",
    fontWeight: 300,
    outline: "none",
    width: "100%",
    boxSizing: "border-box",
    transition: "border-color 0.15s",
    colorScheme: "dark",
  },
  hint: {
    fontSize: "11px",
    color: "var(--text-muted)",
    fontWeight: 300,
    fontFamily: "var(--font-body)",
  },
  primaryBtn: (enabled) => ({
    width: "100%",
    maxWidth: "320px",
    background: "var(--accent)",
    border: "none",
    borderRadius: "10px",
    padding: "13px",
    fontSize: "13px",
    fontWeight: 500,
    color: "#1c1a18",
    cursor: enabled ? "pointer" : "default",
    fontFamily: "var(--font-body)",
    letterSpacing: "0.02em",
    opacity: enabled ? 1 : 0.35,
    transition: "opacity 0.15s",
    marginTop: "4px",
  }),
};

export default function Signup({ onCreateUser }) {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [experienceDate, setExperienceDate] = useState("");
  const [submitting, setSubmitting] = useState(false);

  const today = new Date().toISOString().split("T")[0];

  const nameValid = name.trim().length > 0 && name.trim().length <= 40;
  const dateValid = experienceDate.length > 0 && experienceDate <= today;
  const canSubmit = nameValid && dateValid;

  async function handleSubmit() {
    if (!canSubmit || submitting) return;
    setSubmitting(true);
    try {
      const newUser = await createUser(name.trim(), experienceDate);
      onCreateUser(newUser);
      navigate("/onboarding");
    } catch {
      setSubmitting(false);
    }
  }

  return (
    <div style={s.screen}>
      <button
        style={s.backBtn}
        onClick={() => navigate("/login")}
        aria-label="Back to login"
      >
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M10 3L5 8l5 5" stroke="#8a8480" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        <span style={s.backLabel}>Back</span>
      </button>

      <img src={LogoUrl} width={54} height={54} alt="Integra logo" />
      <h1 style={s.wordmark}>Integra</h1>
      <p style={s.subtitle}>Create your profile.<br />Your name and experience date anchor your integration arc.</p>

      <div style={s.fieldGroup}>
        <label style={s.label} htmlFor="signup-name">Your name</label>
        <input
          id="signup-name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="First name or any name you prefer"
          maxLength={40}
          style={s.input}
        />
      </div>

      <div style={s.fieldGroup}>
        <label style={s.label} htmlFor="signup-date">Date of your experience</label>
        <input
          id="signup-date"
          type="date"
          value={experienceDate}
          max={today}
          onChange={(e) => setExperienceDate(e.target.value)}
          style={s.input}
        />
        <span style={s.hint}>Must be today or earlier.</span>
      </div>

      <button
        style={s.primaryBtn(canSubmit && !submitting)}
        onClick={handleSubmit}
        disabled={!canSubmit || submitting}
      >
        {submitting ? "Setting up your profile..." : "Create profile"}
      </button>
    </div>
  );
}
