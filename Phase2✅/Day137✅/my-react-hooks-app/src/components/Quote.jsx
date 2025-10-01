import { useEffect, useState } from "react";

export default function Quote() {
  const [quote, setQuote] = useState("");

  useEffect(() => {
    fetch("https://api.quotable.io/random")
      .then(res => res.json())
      .then(data => setQuote(data.content));
  }, []);

  return (
    <div className="my-6">
      <h2 className="text-xl font-semibold">Quote of the Moment</h2>
      <p className="italic">{quote}</p>
    </div>
  );
}
