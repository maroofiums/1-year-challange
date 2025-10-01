import { useState, useEffect } from "react";

export default function useFetch(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    let isMounted = true;
    fetch(url)
      .then(res => res.json())
      .then(data => {
        if (isMounted) setData(data);
      });
    return () => { isMounted = false; };
  }, [url]);

  return data;
}
