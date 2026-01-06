import { Card, CardContent, Typography } from "@mui/material";

export default function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <div style={{ display: "flex", gap: "20px" }}>
        <Card style={{ flex: 1 }}>
          <CardContent>
            <Typography variant="h6">Users</Typography>
            <Typography variant="h4">120</Typography>
          </CardContent>
        </Card>
        <Card style={{ flex: 1 }}>
          <CardContent>
            <Typography variant="h6">Orders</Typography>
            <Typography variant="h4">80</Typography>
          </CardContent>
        </Card>
        <Card style={{ flex: 1 }}>
          <CardContent>
            <Typography variant="h6">Revenue</Typography>
            <Typography variant="h4">$5,200</Typography>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
