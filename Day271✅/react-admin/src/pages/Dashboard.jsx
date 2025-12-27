import StatsCard from "../components/StatsCard";

export default function Dashboard() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Dashboard</h1>

      <div className="grid grid-cols-3 gap-6">
        <StatsCard title="Total Users" value="1200" />
        <StatsCard title="Orders" value="340" />
        <StatsCard title="Revenue" value="$21,000" />
      </div>
    </div>
  );
}
