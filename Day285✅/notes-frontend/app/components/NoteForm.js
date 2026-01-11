"use client";
import React, { useState } from "react";

export default function NoteForm({ onSubmit, initialData }) {
  const [title, setTitle] = useState(initialData?.title || "");
  const [content, setContent] = useState(initialData?.content || "");
  const [tag, setTag] = useState(initialData?.tag || "");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ title, content, tag });
    setTitle("");
    setContent("");
    setTag("");
  };

  return (
    <form onSubmit={handleSubmit} className="border p-4 mb-4 rounded">
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="border p-1 w-full mb-2"
        required
      />
      <textarea
        placeholder="Content"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        className="border p-1 w-full mb-2"
        required
      />
      <input
        type="text"
        placeholder="Tag"
        value={tag}
        onChange={(e) => setTag(e.target.value)}
        className="border p-1 w-full mb-2"
      />
      <button type="submit" className="bg-blue-500 text-white px-3 py-1 rounded">
        Save
      </button>
    </form>
  );
}
