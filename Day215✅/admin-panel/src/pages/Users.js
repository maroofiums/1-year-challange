import { useEffect, useState } from "react";
import axios from "axios";

export default function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("https://jsonplaceholder.typicode.com/users")
      .then(res => setUsers(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Users</h1>
      <table border="1" cellPadding="10" style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead style={{ background: "#ddd" }}>
          <tr><th>ID</th><th>Name</th><th>Email</th></tr>
        </thead>
        <tbody>
          {users.map(u => (
            <tr key={u.id}>
              <td>{u.id}</td>
              <td>{u.name}</td>
              <td>{u.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
