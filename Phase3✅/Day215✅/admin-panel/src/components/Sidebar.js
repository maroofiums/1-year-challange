import { Link } from "react-router-dom";
import { Dashboard, People, ShoppingCart } from "@mui/icons-material";

export default function Sidebar() {
  return (
    <div style={{
      width: "220px",
      height: "100vh",
      background: "#111",
      color: "#fff",
      padding: "20px",
      display: "flex",
      flexDirection: "column",
      gap: "20px"
    }}>
      <h2>Admin</h2>
      <nav style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
        <Link to="/" style={{ color: "#fff", textDecoration: "none" }}>
          <Dashboard style={{ marginRight: "8px" }} /> Dashboard
        </Link>
        <Link to="/users" style={{ color: "#fff", textDecoration: "none" }}>
          <People style={{ marginRight: "8px" }} /> Users
        </Link>
        <Link to="/products" style={{ color: "#fff", textDecoration: "none" }}>
          <ShoppingCart style={{ marginRight: "8px" }} /> Products
        </Link>
      </nav>
    </div>
  );
}
