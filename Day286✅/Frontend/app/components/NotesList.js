"use client";
import React from "react";

export default function NotesList({ notes, onDelete }) {
  return (
    <div>
      {notes.length === 0 && <p>No notes yet</p>}
      {notes.map((note) => (
        <div key={note.id} className="border p-3 mb-2 rounded">
          <h3 className="font-bold">{note.title}</h3>
          <p>{note.content}</p>
          {note.tag && <small>Tag: {note.tag}</small>}
          <div className="mt-2">
            <button
              onClick={() => onDelete(note.id)}
              className="bg-red-500 text-white px-2 py-1 rounded"
            >
              Delete
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}
