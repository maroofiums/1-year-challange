export default function Navbar() {
  return (
    <div className="bg-white shadow p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">Welcome, Admin</h1>
      <button className="px-4 py-2 bg-blue-500 text-white rounded">Logout</button>
    </div>
  );
}
