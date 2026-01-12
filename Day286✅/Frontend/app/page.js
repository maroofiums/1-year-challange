"use client";
import React, { useEffect, useState } from "react";
import api from "./api/axios";
import NoteForm from "./components/NoteForm";
import NotesList from "./components/NotesList";

export default function Home() {
  const [notes, setNotes] = useState([]);

  const fetchNotes = async () => {
    const res = await api.get("/notes");
    setNotes(res.data);
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  const addNote = async (note) => {
    await api.post("/notes", note);
    fetchNotes();
  };

  const deleteNote = async (id) => {
    await api.delete(`/notes/${id}`);
    fetchNotes();
  };

  return (
    <div className="max-w-xl mx-auto mt-4">
      <h1 className="text-2xl font-bold mb-4">Notes Manager</h1>
      <NoteForm onSubmit={addNote} />
      <NotesList notes={notes} onDelete={deleteNote} />
    </div>
  );
}
