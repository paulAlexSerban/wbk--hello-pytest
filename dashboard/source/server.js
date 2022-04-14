"use strict";

const express = require("express");

// Constants
const PORT = 3000;
const HOST = "0.0.0.0";

// App
const app = express();
app.get("/", (req, res) => {
  res.send(`<a href="library/component/version">library - component - version</a>`);
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
