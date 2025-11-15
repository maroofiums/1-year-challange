import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="w-60 bg-gray-900 text-white min-h-screen p-5">
      <h2 className="text-2xl font-bold mb-8">Admin Panel</h2>

      <nav className="flex flex-col gap-4">
        <Link to="/" className="hover:text-blue-400">Dashboard</Link>
        <Link to="/users" className="hover:text-blue-400">Users</Link>
        <Link to="/products" className="hover:text-blue-400">Products</Link>
      </nav>
    </div>
  );
}
