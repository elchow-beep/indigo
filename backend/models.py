from sqlalchemy import (
    Column, String, Integer, Float, Boolean, Text,
    DateTime, ForeignKey, JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    display_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    integration_phase = Column(String, default="preparation")
    last_checkin_at = Column(DateTime(timezone=True), nullable=True)
    tokens_used_today = Column(Integer, default=0)
    tokens_used_total = Column(Integer, default=0)
    last_token_reset = Column(DateTime(timezone=True), nullable=True)

    sessions = relationship("Session", back_populates="user", cascade="all, delete-orphan")
    entries = relationship("Entry", back_populates="user", cascade="all, delete-orphan")
    checkins = relationship("Checkin", back_populates="user", cascade="all, delete-orphan")
    conversation_history = relationship("ConversationHistory", back_populates="user", cascade="all, delete-orphan")
    insight_snapshots = relationship("InsightSnapshot", back_populates="user", cascade="all, delete-orphan")
    wellness_snapshots = relationship("WellnessSnapshot", back_populates="user", cascade="all, delete-orphan")
    intentions = relationship("Intention", back_populates="user", cascade="all, delete-orphan")
    user_practices = relationship("UserPractice", back_populates="user", cascade="all, delete-orphan")


class Session(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    session_date = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="sessions")
    entries = relationship("Entry", back_populates="session")
    wellness_snapshots = relationship("WellnessSnapshot", back_populates="session")
    intentions = relationship("Intention", back_populates="session")


class Entry(Base):
    __tablename__ = "entries"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    session_id = Column(String, ForeignKey("sessions.id"), nullable=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    text = Column(Text, nullable=False)
    emotions = Column(JSON, nullable=True)
    themes = Column(JSON, nullable=True)
    recommendations = Column(JSON, nullable=True)
    entry_type = Column(String, default="journal")
    week_number = Column(Integer, nullable=True)
    somatic_rating = Column(Integer, nullable=True)
    hrv = Column(Float, nullable=True)
    resting_hr = Column(Float, nullable=True)

    user = relationship("User", back_populates="entries")
    session = relationship("Session", back_populates="entries")


class WellnessSnapshot(Base):
    __tablename__ = "wellness_snapshots"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    session_id = Column(String, ForeignKey("sessions.id"), nullable=True)
    arc_moment = Column(String, nullable=False)  # baseline, week_2, week_4, week_8, monthly, on_demand
    who5_q1 = Column(Integer, nullable=False)
    who5_q2 = Column(Integer, nullable=False)
    who5_q3 = Column(Integer, nullable=False)
    who5_q4 = Column(Integer, nullable=False)
    who5_q5 = Column(Integer, nullable=False)
    gad2_q1 = Column(Integer, nullable=False)
    gad2_q2 = Column(Integer, nullable=False)
    phq2_q1 = Column(Integer, nullable=False)
    phq2_q2 = Column(Integer, nullable=False)
    total_score = Column(Integer, nullable=False)
    taken_at = Column(DateTime(timezone=True), server_default=func.now())
    is_on_demand = Column(Boolean, default=False)

    user = relationship("User", back_populates="wellness_snapshots")
    session = relationship("Session", back_populates="wellness_snapshots")


class Intention(Base):
    __tablename__ = "intentions"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    session_id = Column(String, ForeignKey("sessions.id"), nullable=False)
    intention_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="intentions")
    session = relationship("Session", back_populates="intentions")


class Checkin(Base):
    __tablename__ = "checkins"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    emotion = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="checkins")


class ConversationHistory(Base):
    __tablename__ = "conversation_history"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="conversation_history")


class InsightSnapshot(Base):
    __tablename__ = "insight_snapshots"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    summary_text = Column(Text, nullable=True)
    computed_at = Column(DateTime(timezone=True), server_default=func.now())
    invalidated = Column(Boolean, default=False)

    user = relationship("User", back_populates="insight_snapshots")


class Practice(Base):
    __tablename__ = "practices"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    framework = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    themes = Column(JSON, nullable=True)
    short_instructions = Column(Text, nullable=True)
    standard_instructions = Column(Text, nullable=True)
    extended_instructions = Column(Text, nullable=True)
    short_duration = Column(Integer, nullable=True)
    standard_duration = Column(Integer, nullable=True)
    extended_duration = Column(Integer, nullable=True)

    user_practices = relationship("UserPractice", back_populates="practice")


class UserPractice(Base):
    __tablename__ = "user_practices"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    practice_id = Column(String, ForeignKey("practices.id"), nullable=False)
    saved = Column(Boolean, default=False)
    completed = Column(Boolean, default=False)
    completion_count = Column(Integer, default=0)
    last_completed_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="user_practices")
    practice = relationship("Practice", back_populates="user_practices")