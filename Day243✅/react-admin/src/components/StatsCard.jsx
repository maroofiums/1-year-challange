export default function StatsCard({ title, value }) {
  return (
    <div className="bg-white rounded shadow p-5">
      <h3 className="text-gray-600">{title}</h3>
      <p className="text-2xl font-bold mt-2">{value}</p>
    </div>
  );
}
