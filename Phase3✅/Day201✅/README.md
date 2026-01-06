# Day 201

## 🚀 Build a React Admin Panel (Step-by-Step)

### 🛠 1. Setup Project

```bash
npx create-react-app admin-panel
cd admin-panel
npm install react-router-dom axios @mui/material @emotion/react @emotion/styled @mui/icons-material
```

* **React Router** → for pages
* **Axios** → for API calls
* **Material UI (MUI)** → ready-made UI kit
* **Icons** → sidebar, dashboard look

---

### 📂 2. Project Structure

```
admin-panel/
 ├── src/
 │   ├── components/
 │   │    ├── Sidebar.js
 │   │    ├── Navbar.js
 │   │    └── Chart.js
 │   ├── pages/
 │   │    ├── Dashboard.js
 │   │    ├── Users.js
 │   │    └── Products.js
 │   ├── App.js
 │   ├── index.js
 │   └── theme.js
```

---

### 🎨 3. Create Sidebar

`src/components/Sidebar.js`

```jsx
import { Link } from "react-router-dom";
import { Dashboard, People, ShoppingCart } from "@mui/icons-material";

export default function Sidebar() {
  return (
    <div style={{ width: "220px", height: "100vh", background: "#111", color: "#fff", padding: "20px" }}>
      <h2>Admin</h2>
      <ul style={{ listStyle: "none", padding: 0 }}>
        <li><Link to="/" style={{ color: "#fff" }}><Dashboard /> Dashboard</Link></li>
        <li><Link to="/users" style={{ color: "#fff" }}><People /> Users</Link></li>
        <li><Link to="/products" style={{ color: "#fff" }}><ShoppingCart /> Products</Link></li>
      </ul>
    </div>
  );
}
```

---

### 📊 4. Pages Setup with Router

`src/App.js`

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import Dashboard from "./pages/Dashboard";
import Users from "./pages/Users";
import Products from "./pages/Products";

function App() {
  return (
    <BrowserRouter>
      <div style={{ display: "flex" }}>
        <Sidebar />
        <div style={{ flex: 1, padding: "20px" }}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/users" element={<Users />} />
            <Route path="/products" element={<Products />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
export default App;
```

---

### 📈 5. Dashboard Page

`src/pages/Dashboard.js`

```jsx
import { Card, CardContent, Typography } from "@mui/material";

export default function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <div style={{ display: "flex", gap: "20px" }}>
        <Card><CardContent><Typography variant="h6">Users: 120</Typography></CardContent></Card>
        <Card><CardContent><Typography variant="h6">Orders: 80</Typography></CardContent></Card>
      </div>
    </div>
  );
}
```

---

### 👥 6. Users Page (with mock API)

`src/pages/Users.js`

```jsx
import { useEffect, useState } from "react";
import axios from "axios";

export default function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("https://jsonplaceholder.typicode.com/users")
      .then(res => setUsers(res.data));
  }, []);

  return (
    <div>
      <h1>Users</h1>
      <table border="1" cellPadding="10">
        <thead>
          <tr><th>ID</th><th>Name</th><th>Email</th></tr>
        </thead>
        <tbody>
          {users.map(u => (
            <tr key={u.id}><td>{u.id}</td><td>{u.name}</td><td>{u.email}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

---

### 🛒 7. Products Page

`src/pages/Products.js`

```jsx
export default function Products() {
  return (
    <div>
      <h1>Products</h1>
      <p>Product list will go here.</p>
    </div>
  );
}
```

---

### ⚡ Next Steps (Level-Up)

* Add **Login Page + JWT auth**
* Add **CRUD forms** for users/products
* Add **Charts** (install `recharts`)
* Add **Dark/Light mode** with `theme.js`

---
