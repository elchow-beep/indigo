# Integra -- Open Tasks
*Last updated: March 3, 2026 -- Priority tiers added*

---

## Tier 1 — Do before the capstone demo
*High impact, visible in a live demo. Complete these first.*

- [ ] **Recurring themes chart -- label bug** -- Theme name and count are concatenated without a separator ("nature connection5" instead of "nature connection"). Fix the data mapping in `Insights.jsx` where theme frequency data is prepared for Recharts. · *~1hr*

- [ ] **Recurring themes chart -- axis bug** -- Y axis shows index numbers (0, 1, 2...) instead of theme names. Fix the chart layout so theme names appear on the Y axis or as bar labels. · *~1hr*

- [ ] **Slide deck** -- Build presentation covering: problem, solution, ML pipeline walkthrough, live demo flow (lead with Jordan's arc, show Alex for onboarding), results and limitations. · *~3hrs*

- [ ] **Demo script** -- Write a short script for the live demo: which profile to select, which entry to show, what to type to Indy, how to walk through Insights. · *~1hr*

- [ ] **Evaluation metrics and model documentation** -- Document emotion pipeline accuracy, theme extraction precision, RAG retrieval quality. Required for capstone submission. · *~2hrs*

- [ ] **Page title** -- Currently shows "Vite App" in the browser tab. Change to "Integra" in `frontend/index.html`. · *~10min*

- [ ] **Favicon** -- Browser tab shows a blank icon. Add an `integra` favicon. The logo SVG can be converted to a `.ico` or used directly as an SVG favicon. · *~20min*

- [ ] **Max-width container on desktop** -- The app is designed for ~390px mobile width. On desktop it stretches full width and looks wrong. Add a max-width wrapper (around 480px) centered on screen in `App.jsx` or `tokens.css`. · *~30min*

---

## Tier 2 — Strong polish, do if time allows
*Meaningful craft signals. Work through these after Tier 1 is complete.*

- [ ] **Indy thinking phrases** -- Replace current loading state with rotating phrases chosen randomly. Suggested phrases: "Sitting with what you shared...", "Holding this with you...", "Taking a moment with this...", "Letting that land...", "Reflecting on what you've shared...". Implement in `Companion.jsx`. · *~30min*

- [ ] **988 thinking state** -- Currently the crisis response appears instantly, which feels canned. Add a brief thinking animation/delay before the 988 message renders so the response feels considered rather than automated. · *~45min*

- [ ] **Shorten 988 response** -- Current crisis message is too long. Trim it to 2-3 sentences max. Edit in `src/rag/crisis_detection.py` or wherever the crisis message string is defined. · *~45min*

- [ ] **988 call button** -- After the crisis message renders, show a tappable button that opens `tel:988`. In `Companion.jsx`, detect `crisis_detected: true` in the API response and render a styled call button below the message. · *~30min*

- [ ] **"Reflect with Indy" button after journal entry** -- After submitting a new entry and seeing the analysis results, there should be a button that takes the user directly to Companion with the entry pre-loaded as context. · *~1hr*

- [ ] **Empty state for Alex** -- When Alex logs in, the Home and Journal pages show bare text. Design a more considered empty state with a prompt to write a first entry. · *~1hr*

- [ ] **Confirmation before clearing Indy chat** -- "Clear chat" button currently fires immediately. Add a simple confirm dialog first. · *~15min*

- [ ] **Guest mode welcome message** -- "Chat with Indy as a guest" drops the user into Companion with no explanation of what Indy is or what to do. Add a brief welcome message on first load in guest mode. · *~20min*

- [ ] **Loading state between login and home** -- If the backend is slow, the user sees a blank screen after selecting a profile. Add a loading indicator while the home page data fetches. · *~30min*

- [ ] **Insights active state in bottom nav** -- There is a visible white/light box around the Insights tab icon when active. Fix the active state styling in `BottomNav.jsx`. · *~20min*

---

## Tier 3 — Post-March 15
*Defer until after capstone. High effort or low demo visibility.*

- [ ] **Streaming responses** -- Switch backend to OpenAI streaming API so Indy's response types in token by token instead of appearing all at once after a delay. Requires changes to both `backend/main.py` (stream from OpenAI) and `Companion.jsx` (read a streaming response body). · *~3-4hrs*

- [ ] **Quick check-in emotion pills -- Indy flow** -- Tapping an emotion pill on the Home screen currently does nothing. On tap, show a small bottom sheet with two options: "Chat with Indy" and "Just log it". "Just log it" silently records the emotion to the longitudinal tracker and dismisses -- no redirect, no friction. "Chat with Indy" opens Companion with the selected emotion passed as context so Indy opens with a targeted prompt ("You checked in as [emotion] -- want to tell me what's going on?"). At the end of the Indy session, offer a "Save as journal entry" CTA that posts the chat log to the `/entries` endpoint with an `entry_type: "checkin"` flag so Insights can distinguish quick check-ins from full journal entries. Requires: bottom sheet component, emotion logging on "Just log it" path, emotion param passed to Companion on navigation, Indy system prompt updated to handle the context note, and backend support for `entry_type: "checkin"`. · *~4-6hrs*

- [ ] **New user signup flow** -- Currently only Alex and Jordan exist as hardcoded demo profiles. Add a flow where a user can create a real account with their name. Needs a new `POST /users` endpoint in the backend and a signup screen in the frontend. · *~3hrs*

- [ ] **Page transition animations** -- Navigating between tabs feels abrupt. Add a subtle fade or slide transition using CSS or a library like `framer-motion`. · *~1-2hrs*

- [ ] **Loading skeleton screens** -- Replace "Loading..." text with placeholder skeleton shapes that match the layout of the content about to appear. · *~1-2hrs*

- [ ] **Delete / edit journal entry** -- No way to remove or correct an entry once submitted. Add delete (with confirmation) as a minimum. Edit is a stretch goal. · *~1-2hrs*

- [ ] **Week number on journal entries** -- `week_number` field is always null because the frontend never calculates or passes it. Either compute it from the entry date relative to the user's first entry, or remove it from the schema. · *~30min*

- [ ] **Framer portfolio link** -- After March 15, add the live app URL to Framer portfolio site. Create a short redirect URL (TinyURL or Bitly) first.

---

*See PROJECT_BRIEF.md for full project context.*
