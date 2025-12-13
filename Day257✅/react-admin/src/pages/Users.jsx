export default function Users() {
  const users = [
    { id: 1, name: "Maroof", email: "maroof@example.com" },
    { id: 2, name: "Ali", email: "ali@example.com" },
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Users</h1>

      <table className="w-full border bg-white shadow">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-3 border">ID</th>
            <th className="p-3 border">Name</th>
            <th className="p-3 border">Email</th>
          </tr>
        </thead>

        <tbody>
          {users.map((user) => (
            <tr key={user.id} className="text-center">
              <td className="p-3 border">{user.id}</td>
              <td className="p-3 border">{user.name}</td>
              <td className="p-3 border">{user.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
