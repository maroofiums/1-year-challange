export default function Products() {
  const products = [
    { id: 1, name: "Laptop", price: "Rs 150000" },
    { id: 2, name: "Mobile", price: "Rs 35000" },
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Products</h1>

      <table className="w-full border bg-white shadow">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-3 border">ID</th>
            <th className="p-3 border">Name</th>
            <th className="p-3 border">Price</th>
          </tr>
        </thead>

        <tbody>
          {products.map((p) => (
            <tr key={p.id} className="text-center">
              <td className="p-3 border">{p.id}</td>
              <td className="p-3 border">{p.name}</td>
              <td className="p-3 border">{p.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
