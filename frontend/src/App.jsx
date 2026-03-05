import { useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login.jsx";
import Home from "./pages/Home.jsx";
import Journal from "./pages/Journal.jsx";
import Insights from "./pages/Insights.jsx";
import Companion from "./pages/Companion.jsx";
import BottomNav from "./components/BottomNav.jsx";

export default function App() {
  const [user, setUser] = useState(null);
  const [entryContext, setEntryContext] = useState(null);

  const isLoggedIn = user !== null;

  function handleSelectUser(selectedUser) {
    setUser(selectedUser);
    setEntryContext(null);
  }

  function handleSwitchProfile() {
    setUser(null);
    setEntryContext(null);
  }

  return (
    <BrowserRouter>
      <div style={{ display: "flex", justifyContent: "center", minHeight: "100vh", background: "#111010" }}>
        <div style={{ width: "100%", maxWidth: "480px", display: "flex", flexDirection: "column", position: "relative" }}>
          <Routes>
            <Route path="/login" element={<Login onSelectUser={handleSelectUser} />} />
            <Route path="/" element={isLoggedIn ? <Navigate to="/home" replace /> : <Navigate to="/login" replace />} />
            <Route path="/home" element={isLoggedIn ? <Home user={user} onSwitchProfile={handleSwitchProfile} /> : <Navigate to="/login" replace />} />
            <Route path="/journal" element={isLoggedIn ? <Journal user={user} onEntrySubmitted={setEntryContext} /> : <Navigate to="/login" replace />} />
            <Route path="/insights" element={isLoggedIn ? <Insights user={user} /> : <Navigate to="/login" replace />} />
            <Route path="/companion" element={isLoggedIn ? <Companion user={user} entryContext={entryContext} onContextUsed={() => setEntryContext(null)} /> : <Navigate to="/login" replace />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
          {isLoggedIn && <BottomNav />}
        </div>
      </div>
    </BrowserRouter>
  );
}
