import { AppBar, Toolbar, IconButton, InputBase, Avatar } from "@mui/material";
import { Search, Notifications, Brightness4 } from "@mui/icons-material";

export default function Navbar() {
  return (
    <AppBar
      position="static"
      elevation={0}
      sx={{
        background: "#fff",
        color: "#000",
        borderBottom: "1px solid #ddd",
      }}
    >
      <Toolbar
        sx={{
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        {/* 🔍 Search Bar */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            background: "#f1f1f1",
            padding: "6px 12px",
            borderRadius: "8px",
            width: "250px",
          }}
        >
          <Search fontSize="small" />
          <InputBase
            placeholder="Search..."
            sx={{ ml: 1, flex: 1 }}
          />
        </div>

        {/* 🔔 Icons + Profile */}
        <div style={{ display: "flex", alignItems: "center", gap: "15px" }}>
          <IconButton color="inherit">
            <Brightness4 />
          </IconButton>
          <IconButton color="inherit">
            <Notifications />
          </IconButton>
          <Avatar alt="Admin" src="https://i.pravatar.cc/300" />
        </div>
      </Toolbar>
    </AppBar>
  );
}
